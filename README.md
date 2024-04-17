

---

# Store Monitoring Backend API

This project is a backend system designed to help restaurant owners monitor the online/offline status of their stores during business hours. It includes APIs for generating reports based on store activity data collected over time.

## Table of Contents

- Installation
- Usage
- Endpoints
- Data Sources
- System Requirements
- API Requirement
- Considerations/Evaluation Criteria
- Contributing


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/store-monitoring-backend.git
```

2. Install dependencies:

```bash
cd store-monitoring-backend
pip install -r requirements.txt
```

3. Set up the database and import the provided CSV data.
Here is the link for the dataset.
[https://drive.google.com/drive/folders/1qRE_QcfDWFhTL_OWEQkbWgEsdSCF1P0m?usp=drive_link]
Take this data folder and paste it in the directory where run.py is there.
The data folder has three files in it.

## Usage

1. Start the server:

```bash
python app.py
```

2. Access the API endpoints using a tool like `curl` or via HTTP requests from your application.

## Endpoints

- `/trigger_report`: Trigger report generation. No input required. Returns a report_id.
- `/get_report`: Retrieve the status of the report or the generated CSV file. Input required: report_id.

## Data Sources

The project relies on three main sources of data:
1. Store activity data in CSV format.
2. Business hours data in CSV format.
3. Timezone data for the stores in CSV format.

These CSV files are provided and should be imported into the database before using the APIs.
[https://drive.google.com/drive/folders/1qRE_QcfDWFhTL_OWEQkbWgEsdSCF1P0m?usp=drive_link]

## System Requirements

- Python 3.x
- Relevant database (PostgreSQL)
- Internet connection for periodic data updates

## API Requirement

The project provides two main APIs:
1. `/trigger_report`: Initiates report generation and returns a report_id.
2. `/get_report`: Retrieves the status of the report or the generated CSV file.

## Considerations/Evaluation Criteria

- The code is well-structured, handling corner cases and errors gracefully.
- Good use of type annotations and clear documentation.
- Correct functionality for trigger + poll architecture, database reads, and CSV output.
- Efficient computation of uptime/downtime hours.
- Optimization for performance and scalability.

## Contributing

Contributions are welcome! Please follow the standard guidelines for contributing outlined in CONTRIBUTING.md.

