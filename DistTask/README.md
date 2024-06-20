# Distributed Task Scheduling Framework

## Overview
This project is a lightweight framework for distributing computational tasks across multiple CPU cores to enhance parallel processing performance. It features task distribution, load balancing, fault tolerance, and supports user-defined tasks. The framework is easy to integrate into existing systems and provides a simple API for submitting tasks, retrieving results, and monitoring worker status. The core components include a Flask web application for managing task and result queues, and worker processes that execute tasks in parallel. Users can define custom tasks, serialize them, and submit them via HTTP requests. The framework is suitable for applications requiring high-performance computing, such as data processing and scientific simulations.

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
