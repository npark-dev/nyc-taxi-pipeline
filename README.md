# NYC Taxi Data Pipeline

An ETL pipeline project for collecting, transforming, and loading NYC taxi data.

## Overview

This project implements a data pipeline that collects NYC taxi data from the NYC Open Data API, processes it, and makes it available for analysis. The project is structured in phases:

### Phase 1
- Store raw data in MinIO object storage
- Load and analyze data in ClickHouse

### Phase 2
- Store data in Google Cloud Storage (GCS)
- Build a data warehouse using BigQuery

### Final Phase
- Create dashboards to visualize analysis results

## Key Features

- NYC taxi data collection (Yellow, Green, FHV)
- Data cleaning and transformation
- Data storage in MinIO and ClickHouse
- Advanced analytics with ClickHouse
- Workflow automation with Airflow
- Dockerized execution environment
- Dashboard for data visualization

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- NYC Open Data API access token

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/npark-dev/nyc-taxi-pipeline.git
   cd nyc-taxi-pipeline
   ```

2. Set up virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```
   cp .env.example .env
   # Edit the .env file with your values
   ```

### Running the Pipeline

```
docker-compose up -d
```

This will start:
- MinIO on port 9000 (console on 9001)
- ClickHouse on port 8123 (TCP on 9000)
- Airflow webserver on port 8080
- Dashboard on port 8050

## Project Structure

```
nyc-taxi-pipeline/
├── airflow/                    # Airflow DAGs and configurations
├── data/                       # Sample data and schemas
├── docker/                     # Docker-related files
├── k8s/                        # Kubernetes manifests
├── scripts/                    # Utility scripts
├── src/                        # Source code
│   ├── collectors/             # Data collection modules
│   ├── transformers/           # Data transformation modules
│   ├── loaders/                # Data loading modules
│   └── common/                 # Common utilities
└── tests/                      # Test code
```

## License

This project is distributed under the MIT License.