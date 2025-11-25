import time
import tracemalloc

def polygonal_number(s, n):
    return ((s - 2) * n * (n - 1)) // 2 + n

s = int(input("Enter s: "))
n = int(input("Enter n: "))

tracemalloc.start()
start = time.time()

result = polygonal_number(s, n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Polygonal Number:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak/1024, "KB")
