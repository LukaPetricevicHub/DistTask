import multiprocessing
import pickle

def worker(task_queue, result_queue, load_dict, lock):
    worker_name = multiprocessing.current_process().name
    while True:
        try:
            task_func, task_args = task_queue.get_nowait()
        except multiprocessing.queues.Empty:
            break
        with lock:
            load_dict[worker_name] += 1
        result = task_func(*task_args)
        with lock:
            load_dict[worker_name] -= 1
        result_queue.put(result)

def serialize_task(task_func, *task_args):
    return pickle.dumps((task_func, task_args)).hex()