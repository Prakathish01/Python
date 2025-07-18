# List comprehension
#---> A concise way to create lists in python,Compact and easier than a traditional loop
#[expression for value in iterables if condition]

doubles = [x*2 for x in range(1,10)]
num = [i for i in reversed(range(1,11))]
print(num)
print(doubles)

#Strings

fruits = ["apple", "orange" , "papaya" ,"banana"]
fruit_upper =[x.upper() for x in fruits]
fruit_fl =[x.capitalize() for x in fruits]
print(fruit_fl,fruit_upper,sep="\n")

#if

numbers = [1,-2,3,4,-5,6,7,-8,9]
positive =[num for num in numbers if num%2==0 and num > 0]
print(positive)
