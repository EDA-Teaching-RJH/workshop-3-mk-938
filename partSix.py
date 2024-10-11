cost = 0
def price(x,y):
    if 12 <= x <= 64:
        if y == "Y":
            return 8
        else:
            return 10
    else:
        return 5

def info(cost):
    age = int(input("What is your age?"))
    student = input("Are you a student? (Y/N)")
    cost = price(age, student)
    return cost

customers = int(input("how many customers?"))
for x in range(0, customers):
    cost += info(cost)

print ("£", cost)
