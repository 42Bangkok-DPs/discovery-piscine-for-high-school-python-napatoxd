number = int(input("Enter a number less than 25  "))
while True :
    if number >= 25 :
        print("Error")
        break
    else :
        number = number +1
        print("Inside the loop, my variable is" , number)

