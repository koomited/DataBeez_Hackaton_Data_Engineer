from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago

from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator
 
import requests
import json

# Api key

API_KEY = os.getenv("OPEN_WEATHER_API_KEY") 

# The towns coordinates
LATITUDE_DAKAR = "14.6937"
LONGITUDE_DAKAR = "-17.4441"

LATITUDE_THIES = "14.8342" 
LONGITUDE_THIES = "-17.1061"

# Connections ids from airflow
POSTGRES_CONN_ID = 'postgres_conn'
API_CONN_ID = "senegal_open_meteo_api_conn"

default_args={
    "owner":"Tousside",
    "retries":5,
    "retry_delay":timedelta(minutes=3),
}

## DAG

with DAG(
    dag_id="senegal_weather_etl_pipeline_v02",
    description="Daily weather information on DAKAR and THIES",
    default_args= default_args,
    start_date=datetime(2024, 12, 7),
    schedule="@daily",
    catchup=False
    ) as dag:
    
    @task(multiple_outputs=True)
    def extract_weather_data():
        """Extract weather data from OPen Meteo API using Airflow Connection"""
        # Use http hook to get the weather data from airflow connection
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method="GET")
        
        ## Build the api endpoint
        # first part 
        # https://api.openweathermap.org
        endpoint = (
            "/data/2.5/weather?"
            f"lat={LATITUDE_DAKAR}&"
            f"lon={LONGITUDE_DAKAR}&"
            f"appid={API_KEY}"
        )

        
        # endpoint = f"/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true"
        
        ## Request via HTTP Hooks
        response = http_hook.run(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch the weather data: {response.status_code}")
        
    @task()
    def transform_weather_data(weather_data):
        """Transform the extracted data."""
        main_info = weather_data["main"]
        
        transformed_data={
            'city':weather_data["name"],
            'description':weather_data["weather"][0]["description"],
            'temperature':main_info["temp"],
            'pressure':main_info["pressure"],
            'humidity':main_info["humidity"],
        }
        return transformed_data
    
    @task()
    def load_weather_data(transformed_data):
        """Load transformed data into PostgreSQL"""
        
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        
        # create table if it does not exist
        cursor.execute(
            
            """
                CREATE TABLE IF NOT EXISTS weather_data (
                    city VARCHAR(50),
                    description VARCHAR(200),
                    temperature FLOAT,
                    pressure FLOAT,
                    humidity FLOAT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """
        )
        # Insert transformed data into the table
        cursor.execute("""
            INSERT INTO weather_data (city, description,
                    temperature, pressure, humidity)
                    VALUES (%s, %s, %s, %s, %s)""", 
                    (
                        transformed_data["city"],
                        transformed_data["description"],
                        transformed_data["temperature"],
                        transformed_data["pressure"],
                        transformed_data["humidity"]
                    )
                    )
        conn.commit()
        cursor.close()
        
    ## DAG WORKFLOW ETL Pipeline
    weather_data = extract_weather_data()
    transformed_data = transform_weather_data(weather_data)
    load_weather_data(transformed_data)
        