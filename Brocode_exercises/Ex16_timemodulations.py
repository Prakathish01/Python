# Time modulations

import time

my_time = int(input("Enter the time in seconds :\n"))
for i in range(my_time,0,-1):
    seconds = i % 60
    minute = int(i/60) % 60
    print(f"Time is {minute:02}:{seconds:02}")
    time.sleep(1)