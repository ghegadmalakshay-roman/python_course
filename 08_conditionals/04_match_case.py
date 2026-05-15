a = int(input("Enter your lucky number"))

match a:
    case 122:
        print("The value is 122")
    case 3:
        print("The value is 3")
    case 6:
        print("The value is 6")
    case _:
        print("better luck next time")             