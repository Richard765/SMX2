import os
import time
x = 1

while x <= 10:
    time.sleep(0.5)
    print(os.getpid())
    x = x + 1
