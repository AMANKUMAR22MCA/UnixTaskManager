import threading
import time
from .models import Task

# Global dictionary to track threads
task_threads = {}

def simulate_task_lifecycle(task_id):
    # Avoid starting a new thread if one is already running for this task
    if task_id in task_threads and task_threads[task_id].is_alive():
        return
    
    def task_runner():
        time.sleep(5)  # Simulate running for 5 seconds
        try:
            task = Task.objects.get(id=task_id)
            task.state = "completed"
            task.save()
        except Task.DoesNotExist:
            pass
        finally:
            # Remove from task_threads when done
            task_threads.pop(task_id, None)

    # Create and start a new thread for the task
    thread = threading.Thread(target=task_runner)
    task_threads[task_id] = thread
    thread.start()
