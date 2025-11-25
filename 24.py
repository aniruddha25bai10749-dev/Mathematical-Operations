import time
import tracemalloc
tracemalloc.start()
start = time.time()
def order_mod(a, n):
    a=int(a)
    n=int(n)
    for k in range(1,n):
        if (a**k)%n==1:
            print(k)
            break
    else:
        print("no order")
order_mod(5,2)
end = time.time()
current,peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak,"bytes")
print("execution time is",end - start)
