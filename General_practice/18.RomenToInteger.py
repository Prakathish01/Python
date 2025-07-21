#Romen to Interger

dic= {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
s= input("Enter The Roman to Convert:")
sum = 0
prev_value = 0
for char in reversed(s):
    current_value = dic[char]
    if current_value < prev_value:
        sum -= current_value
    else:
        sum += current_value
    prev_value = current_value
print(sum)