# Program to demonstrate format specifiers in f-strings

price = 45.6789
name = "Ash"
value = 123.4567
num = 1234567
rate = 0.856
text = "Hi"

print(f"1. .2f (2 decimals): Price = {price:.2f}")
print(f"2. < (Left align): Name = {name:<10}Done")
print(f"3. > (Right align): Name = {name:>10}Done")
print(f"4. ^ (Center align): Name = {name:^10}Done")
print(f"5. Width + decimals: Value = {value:10.2f}")
print(f"6. Padding with char: {text:-^10}")
print(f"7. Thousands separator: Number = {num:,}")
print(f"8. Percentage: Success Rate = {rate:.2%}")
print(f"9. Zero padding: Number = {num:020}")

