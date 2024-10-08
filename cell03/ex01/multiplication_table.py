def multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(0, 10):
        print(f"{number} x {i} = {number * i}")

def main():
        input1 = input("Enter a number to display its multiplication table: ")
        number = int(input1)

        multiplication_table(number)

main()