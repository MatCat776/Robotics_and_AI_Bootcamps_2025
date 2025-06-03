variable = 0
for i in range(0, 10):
    print(variable)
    variable += 1
if variable > 5:
    print("Variable is larger than 5")
else:
    print("Variable smaller than or equal to 5")
variable = variable - 2
print(variable)