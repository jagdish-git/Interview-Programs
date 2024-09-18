import timeit   
import time
from datetime import timedelta

start_time = time.time()
start_timeit = timeit.timeit()

def prime(n):
    if n > 1:
        for i in range(n):
            target = i
            for j in range(2,target):
                if target % j == 0:
                    break
            else:
                yield i

print(list(prime(100)))

end_time = time.time()
end_timeit = timeit.timeit()

print(end_time - start_time)
print(end_timeit - start_timeit)
print('TIME_DELTA', timedelta(seconds=end_time-start_time))