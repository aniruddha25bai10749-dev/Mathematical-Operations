import time
import tracemalloc

def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    seq = [2, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

n = int(input("Enter n for Lucas Sequence: "))

tracemalloc.start()
start = time.time()

result = lucas_sequence(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Lucas Sequence:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak/1024, "KB")
