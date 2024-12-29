# Data Engineering Project

[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white)](#)
[![Astronomer](https://img.shields.io/badge/Astronomer-4E5D94?logo=astronomer&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](#)
[![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apacheairflow&logoColor=white)](#)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)](#)
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black)](#)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](#)
![Awesome](https://img.shields.io/badge/Awesome-ffd700?logo=awesome&logoColor=black)

---

<a href="#">
  <img width="100%" src="images/pipeline_weather.svg" alt="Pipeline">
</a>

---

## Overview

This project involves building a data pipeline to fetch and process daily weather data, including temperature, meteorological descriptions, pressure, and humidity, for Senegalese cities **Dakar** and **Thies**. The architecture is deployed using **Astronomer**, automated with **GitHub Actions**, and visualized in **Power BI** for insightful analysis.

---

## Features

- **Weather Data Pipeline**: A robust ETL pipeline that extracts, transforms, and loads weather data into a PostgreSQL database.
- **Automation**: Seamless CI/CD pipeline implemented with GitHub Actions for deployment and monitoring.
- **Visualization**: Power BI dashboards to visualize weather trends and insights.
- **Scalability**: Deployed with Astronomer to handle production-grade workloads.

---

## Project Contents

This project contains the following files and folders:

- **`dags/`**: Contains Airflow DAGs.
  - `etl_weather.py`: Processes weather data for a single API call.
  - `etl_senegal_weather.py`: Handles multiple API calls for Senegalese cities.
- **`Dockerfile`**: Defines the Astronomer Runtime Docker image.
- **`include/`**: Placeholder for additional resources.
- **`packages.txt`**: Specifies OS-level dependencies (empty by default).
- **`requirements.txt`**: Specifies Python dependencies (editable as per project needs).
- **`plugins/`**: For custom or community plugins (empty by default).
- **`airflow_settings.yaml`**: Configures Airflow Connections, Variables, and Pools locally.
- **`.github/workflows/`**: Contains GitHub Actions workflows for CI/CD:
  - `create-deployment-preview.yml`: Creates a deployment preview.
  - `deploy-to-preview.yml`: Deploys code to the preview environment.
  - `delete-preview-deployment.yml`: Deletes the preview deployment.
  - `deploy-to-main-deployment.yml`: Deploys code to the main production environment.
- **`images/`**: Contains the pipeline visualization diagram.

---

## Technologies Used

1. **Apache Airflow**: Orchestrates the ETL pipeline.
2. **Astronomer**: Manages scalable Airflow environments for production.
3. **PostgreSQL**: Stores transformed data for querying and analysis.
4. **Power BI**: Visualizes weather insights through interactive dashboards.
5. **GitHub Actions**: Automates workflows for CI/CD processes.
6. **Docker**: Ensures consistency in the development and production environments.

---

## Getting Started

### Prerequisites

- **Docker** installed and running.
- **Astronomer CLI** installed for local development.
- **PostgreSQL** database set up with connection details.
- **Power BI Desktop** for creating visualizations.

### Setup Steps

1. Clone this repository:
```bash
   git clone https://github.com/koomited/DataBeez_Hackaton_Data_Engineer.git
   cd DataBeez_Hackaton_Data_Engineer
```
2. Install Python dependencies::
```bash
   pip install -r requirements.txt
```
3. Start the Astronomer environment:
```bash
   astro dev start
```
4. Access the Airflow UI at http://localhost:8080 and trigger your DAGs.
5. Use Power BI to connect to the PostgreSQL database for data visualization.

## Future Enhancements
- Expand Coverage:
    - Include more cities for weather data collection.
- Add Real-Time Features:

    - Real-time alerting for extreme weather conditions.
    - Integration with messaging platforms for notifications.

- Predictive Analytics:

    - Leverage historical data to predict weather trends.
    - Use machine learning models for forecasting.
  
## Contribution Guidelines

Contributions are welcome! If you'd like to contribute:

1. **Fork the repository**.
2. **Create a feature branch**:
```bash
git checkout -b feature-name
```
- **Commit your changes**:
```bash
git commit -m "Add new feature"
```
- **Push to the branch**:
```bash
git push origin feature-name
```
- Open a pull request for review.
  
- License

    This project is licensed under the MIT License. See the LICENSE file for details.