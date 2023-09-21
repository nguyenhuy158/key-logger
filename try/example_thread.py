import threading
import random


def worker_function(thread_id, random_number):
    for i in range(random_number):
        print(f"Thread {thread_id} is working with {i}/{random_number}")


# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=worker_function,
                              args=(i, random.randint(5, 10)))
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# # Wait for all threads to finish
for thread in threads:
    thread.join()

print("===================================================================All threads have completed their work")
