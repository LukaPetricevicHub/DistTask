import unittest
import multiprocessing
import pickle
from multiprocessing import Queue
from tasks import worker, serialize_task

def example_task(x, y):
    return x + y

class TestDistributedTaskScheduler(unittest.TestCase):
    def test_example_task(self):
        result = example_task(4, 5)
        self.assertEqual(result, 9)

    def test_task_serialization(self):
        serialized_task = serialize_task(example_task, 4, 5)
        task_func, task_args = pickle.loads(bytes.fromhex(serialized_task))
        result = task_func(*task_args)
        self.assertEqual(result, 9)

    def test_task_distribution(self):
        task_queue = Queue()
        result_queue = Queue()
        load_dict = multiprocessing.Manager().dict()
        lock = multiprocessing.Lock()

        for i in range(2):
            load_dict[f'Worker-{i}'] = 0

        tasks = [serialize_task(example_task, i, i) for i in range(5)]
        for task in tasks:
            task_queue.put(pickle.loads(bytes.fromhex(task)))

        workers = []
        for i in range(2):
            p = multiprocessing.Process(target=worker, args=(task_queue, result_queue, load_dict, lock))
            workers.append(p)
            p.start()

        for p in workers:
            p.join()

        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        self.assertEqual(len(results), 5)
        expected_results = [0, 2, 4, 6, 8]
        for result in results:
            self.assertIn(result, expected_results)

if __name__ == "__main__":
    unittest.main()