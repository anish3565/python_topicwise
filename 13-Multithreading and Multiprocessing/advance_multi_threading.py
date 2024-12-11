## Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers=[1,2,3,4,5,6,1,3,5,0,1,2,3,4,]
t=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number, numbers)

finished_time=time.time()-t
for result in results:
    print(result)