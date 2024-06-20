# Distributed Task Scheduling Framework

## Overview
This project provides a lightweight framework for distributing computational tasks across multiple cores of a single computer, enabling parallel processing to improve performance.

## Features
- Task Distribution
- Load Balancing
- Fault Tolerance
- Easy Integration
- User-Defined Tasks

## Getting Started
1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the Flask API: `python app.py`

## API Usage
- **Submit Task**: `POST /submit_task` with JSON body `{"task": "serialized_task"}`
- **Get Results**: `GET /get_results`
- **Check Status**: `GET /status`

## Examples
### Submitting a User-Defined Task
First, define and serialize your task in your script:
```python
import requests
from tasks import serialize_task

def example_task(x, y):
    return x + y

task = serialize_task(example_task, 3, 4)
response = requests.post('http://127.0.0.1:5000/submit_task', json={"task": task})
print(response.json())
```

### Retrieving Results
```bash
curl http://127.0.0.1:5000/get_results
```

### Checking Worker Status
```bash
curl http://127.0.0.1:5000/status
```