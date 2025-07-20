# Armstrong In Range

start = int(input("Enter the starting number:\n"))
end = int(input("Enter the ending number:\n"))
"""
for num in range(start,end+1):
    length = len(str(num))
    arms = 0
    temp = num
    while temp !=0:
        rem = temp%10
        arms = pow(rem,length) + arms
        temp = temp // 10
    if arms == num:
        Arms_list.append(arms)
print(Arms_list)
"""
def is_armstrong(num,length,arms=0):
    if num ==0:
        return arms
    rem = num % 10
    arms += pow(rem,length)
    return is_armstrong(num//10,length,arms)
def range_armstrong(start,end,Arms_list = None):
    if Arms_list ==None:
        Arms_list =[]
    if start > end :
        return Arms_list
    num = start
    length = len(str(num))
    if is_armstrong(num,length) == start:
        Arms_list.append(start)
    return range_armstrong(start+1,end,Arms_list)
result = range_armstrong(start,end)
print("Armstrong range between numbers are",result)






