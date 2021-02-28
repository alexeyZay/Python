import time
start_time=time.time()
print(sum(number for number in range(200000000)))
result_time=time.time()-start_time
print(result_time)
start_time1=time.time()
print(sum([number for number in range(200000000)]))
result_time2=time.time()-start_time1
print(result_time2)