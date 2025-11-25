import time
import tracemalloc
import math

def is_perfect_power(n):
    if n <= 1:
        return False
    for b in range(2, int(math.log2(n)) + 2):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False

n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()

result = is_perfect_power(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Perfect Power?", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak/1024, "KB")

