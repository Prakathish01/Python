#variable scope = where a variable is visible and accessible
#scope resolution = (LEGB) Local -> Enclosed -> global -> Built-in
import math
#local
def func1():
    x=1
    print(x)
#Enclosed
def func2():
    x=2
    def func2a():
        print(x)
    func2a()
#Global
x=3
def func3():
    print(x)
#Built-in

res = math.e
print(res)

func1()
func2()
func3()
