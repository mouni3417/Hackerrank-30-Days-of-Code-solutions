meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())

i = (meal_cost * (tip_percent / 100))
j = (meal_cost * (tax_percent / 100))
x= round(i+j+meal_cost, )
print(i)
print(j)
print("The total meal cost is " + str(int(i + j + meal_cost)) + " dollars.")
print("The total meal cost is " + str(int(x)) + " dollars.")
