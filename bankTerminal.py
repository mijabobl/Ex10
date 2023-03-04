
secret = str()
count = int(0)
while secret != '9999':
    secret = input("Please enter your 4 digit pin: ")
    count = count + 1
    if secret == str("9999"):
        print("Welcome to Your banking How Much Money Would you Like")
    else:
        print("no")
        if count == 1:
            print("1 attempt, think about it")
        elif count == 2:
            print("2 attempts, careful, only 1 left")
        else:
            print("That's too many attempts, Goodbye")
            break
