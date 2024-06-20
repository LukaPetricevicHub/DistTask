# Distributed Task Scheduling Framework

## Overview
This initiative introduces an innovative system for allocating computational workloads across several CPU cores to boost parallel processing efficiency. Key attributes include workload distribution, dynamic
balancing, resilience against failures, and customization options for user-defined tasks. Designed for seamless integration with existing infrastructures, it offers an intuitive API for task submission, result
retrieval, and worker activity monitoring. The primary modules consist of a web interface built with Flask for managing job and output queues, alongside parallel-executing worker units. Users have the flexibility to
create and serialize their tasks, submitting them through HTTP endpoints. Ideal for scenarios demanding high-efficiency computing, such as big data analytics and complex simulations.

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
