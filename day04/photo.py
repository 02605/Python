import os
import time
# os.system("")
time_now = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
os.system("raspistill -n -t 1000 -o "+time_now+".png &")
