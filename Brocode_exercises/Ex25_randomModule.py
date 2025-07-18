#Random Module

import random

cards = ["2","3","4","5","6","7","8","9","10","K","Q","J","A"]
random.shuffle(cards)
rand_num = random.random()
number =random.randint(1,20)
option = random.choice(cards)
print(option)
print(number)
print(rand_num)
print(cards)