"""
Exception - An event that interrupts the flow of a program
            (ZeroDivisionError , TypeError , ValueError)
            1.try , 2.except , 3.finally
"""
try :
    num = int(input("Enter the number to divide :\n"))
    print(10/num)
except ZeroDivisionError :
    print("You can't type zero dah Gopal!!!")
except ValueError :
    print("Enter only numbers please")
except Exception:
    print("Something Went Wrong")
finally:
    print("----------------------------")
    print("'It executes no matter what'")