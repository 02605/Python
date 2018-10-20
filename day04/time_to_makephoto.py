import time
import os
for i in range(1,50):
    print(str(i), 's')
    time.sleep(1)
    if i%3 == 0:
        os.system("raspistill -t 1 -o "+str(time.time())+".png")
    if i==10:
        break
print("finish")

