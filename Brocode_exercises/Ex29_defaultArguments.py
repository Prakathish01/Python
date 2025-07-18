#Default Arguments
import time
def net_price(price,discount=0,tax=0.05):
    return price * (1-discount) * (1+tax)
print(net_price(450))
print(net_price(500,5,0))
print(net_price(500,tax=0.1))

def count_down(start,end):
    for num in range(start,end+1):
        print(num)
        time.sleep(1)
count_down(0,5)

