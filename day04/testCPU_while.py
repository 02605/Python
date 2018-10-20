import time
starttime = time.time()
lastnum = 0
num = 0
while num < 100000000:
    num += 1
    lastnum += num
print(lastnum)

endtime = time.time()
print("cost: ",endtime-starttime)
