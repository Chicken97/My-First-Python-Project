# Write your code here
print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
print()
print("Income: $5405")
print("Staff expenses:")
staff = int(input())
print("Other expenses:")
other = int(input())
net_income = 5405 - (staff + other)
print(f'Net income: {net_income}')