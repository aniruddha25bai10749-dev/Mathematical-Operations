import time
import tracemalloc

def collatz_length(n):
    steps = 0
    while n != 1:
        n = n//2 if n%2==0 else 3*n+1
        steps += 1
    return steps

n = int(input("Enter number: "))

tracemalloc.start()
start = time.time()

result = collatz_length(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Steps:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak/1024, "KB")
