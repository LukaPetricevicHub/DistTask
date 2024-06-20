from flask import Flask, request, jsonify
import multiprocessing
import pickle
from tasks import worker

app = Flask(__name__)
task_queue = multiprocessing.Queue()
result_queue = multiprocessing.Queue()
lock = multiprocessing.Lock()
load_dict = multiprocessing.Manager().dict()

for i in range(multiprocessing.cpu_count()):
    load_dict[f'Worker-{i}'] = 0

@app.route('/submit_task', methods=['POST'])
def submit_task():
    task = request.json.get('task')
    task = pickle.loads(bytes.fromhex(task))  # Deserialize the task
    task_queue.put(task)
    return jsonify({"status": "Task submitted"})

@app.route('/get_results', methods=['GET'])
def get_results():
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    return jsonify(results)

@app.route('/status', methods=['GET'])
def status():
    return jsonify(load_dict.copy())

if __name__ == "__main__":
    workers = []
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=worker, args=(task_queue, result_queue, load_dict, lock))
        workers.append(p)
        p.start()

    app.run(debug=True)

    for p in workers:
        p.join()