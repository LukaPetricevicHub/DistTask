# Distributed Task Scheduling Framework: Efficient Computational Workload Management

This project presents a simple framework designed to allocate computational tasks across multiple CPU cores, significantly enhancing parallel processing capabilities. The primary components include dynamic workload distribution, load balancing, fault tolerance,
and extensive customization for user-defined tasks. The system integrates seamlessly with existing infrastructures, providing an intuitive API for task submission, result retrieval, and worker activity monitoring. A web interface built with Flask manages job and
output queues, while parallel-executing worker units handle the tasks. This framework is ideal for initial exploration into high-efficiency computing, such as data processing and analytical tasks.

## Features
- **Task Distribution:** Efficient allocation of tasks across multiple CPU cores.
- **Load Balancing:** Dynamic balancing to optimize resource utilization.
- **Fault Tolerance:** Resilience against failures to ensure continuous operation.
- **Easy Integration:** Designed to work seamlessly with existing infrastructures.
- **User-Defined Tasks:** Flexibility for users to create and serialize custom tasks.

## Customizability
The framework is highly adaptable, allowing users to:
- Define and serialize their tasks.
- Integrate with various infrastructures effortlessly.
- Monitor task progress and worker status through an intuitive web interface.
- Handle failures gracefully to maintain operational integrity.

## Getting Started
To get started with the Distributed Task Scheduling Framework, follow these steps:

### Installation
Clone the repository:
```bash
git clone https://github.com/LukaPetricevicHub/DistTask.git
cd DistTask
```
Install the required packages:
```bash
pip install -r requirements.txt
```
Run the Flask API:
```bash
python app.py
```

## Usage
### API Endpoints
**Submit Task:**
- **Endpoint:** `POST /submit_task`
- **JSON Body:** `{"task": "serialized_task"}`

**Get Results:**
- **Endpoint:** `GET /get_results`

**Check Status:**
- **Endpoint:** `GET /status`

### Examples
#### Submitting a User-Defined Task
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

#### Retrieving Results
```bash
curl http://127.0.0.1:5000/get_results
```

#### Checking Worker Status
```bash
curl http://127.0.0.1:5000/status
```

## Ideas for Extensions
Here are some potential extensions and areas for further experimentation:
- **Enhanced Load Balancing Algorithms:** Explore different algorithms to optimize resource utilization further.
- **Advanced Fault Tolerance Mechanisms:** Develop more sophisticated mechanisms to enhance system resilience.
- **Expanded API Functionality:** Add more endpoints for better control and monitoring.
- **Support for Diverse Workloads:** Extend support for a wider range of tasks and computational workloads.
- **User-Friendly Interface Enhancements:** Improve the web interface for better user experience.
- **Performance Metrics and Monitoring:** Implement detailed performance metrics to monitor and analyze system efficiency.

## License
Distributed Task Scheduling Framework is released under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.
