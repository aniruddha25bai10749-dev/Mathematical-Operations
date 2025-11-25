import time
import tracemalloc
tracemalloc.start()
start = time.time()
def is_fibonacci_prime(n):
    n=int(n)
    i=1
    for i in range(1,n):
        if n % i == 0:
            b=i
        i=i+1
    if b==1:
        print("prime")
    else:
        print("not prime")
    k=0
    l=1
    v=0
    for v in range(0,n):
        u=l+k
        k=l
        l=u
        if n==u:
            print("number is fibonacci")
            break
        if n<u:
            print("number is not fibonacci")
            break
    v=v+1
is_fibonacci_prime(5)
end = time.time()
current,peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak,"bytes")
print("execution time is",end - start)
