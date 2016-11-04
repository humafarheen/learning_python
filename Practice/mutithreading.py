import thread
import time
def printtime(threadname,delay):
 count=0
 while count<5:
   time.sleep(delay)
   count=count+1
   #print ("%s"%(threadname))
try:
 thread.start_new_thread(printtime,("huma",2,))
 thread.start_new_thread(printtime,("farheen",4,))
except:
 print("unable to start thread")
while 1:
 pass
 