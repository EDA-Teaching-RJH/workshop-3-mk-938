op = input("enter operator (+,-,*,/,^,%) or quit to end app ")
no_1 = int(input("enter first number: "))
no_2 = int(input("enter second number: "))


match op:
    case "+":
        print (no_1 + no_2)
    case "-":
        print (no_1 - no_2)
    case "*":
        print (no_1 * no_2)
    case "/":
        print (no_1 / no_2)
    case "^":
        print (no_1 ^ no_2)
    case "%":
        print (no_1 % no_2)
    case "quit":
        print ("quitting application")
