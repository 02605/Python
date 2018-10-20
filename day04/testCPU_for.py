import time
starttime = time.time()
lastnum = 0
num = 0
for num in range(0,100000001):
    lastnum += num
print(lastnum)

endtime = time.time()
print("cost: ",endtime-starttime)
