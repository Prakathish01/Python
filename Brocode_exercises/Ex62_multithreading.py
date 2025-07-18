"""
Multithreading -Used to perform multiple tasks concurrently (multitasking)
                Good for i/o bound like reading files or fetching data from APIs
                threading. Thread(target = my_function)
"""

import threading,time

def walk_dog(args):
    time.sleep(4)
    print(f"Walking with {args} ended!!")
def take_out_trash(waste1,waste2):
    time.sleep(2)
    print(f"You take out the {waste1} ,{waste2} trash")

process1 = threading.Thread(target=walk_dog , args=("kumar",))
process1.start()
process2 = threading.Thread(target=take_out_trash ,args=("dry waste","water waste"))
process2.start()

process1.join()
process2.join()
print("------------------------")
print("All tasks are completed!")
print("------------------------")


