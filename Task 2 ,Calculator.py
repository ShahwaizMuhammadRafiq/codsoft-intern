def add(no1,no2):
    ans=no1 + no2
    return ans
def sub(no1,no2):
    ans=no1 - no2
    return ans
def mul(no1,no2):
    ans=no1 * no2
    return ans
def div(no1,no2):
    ans=no1 / no2
    return ans

def main():
    no1=eval(input("Enter No 1:"))
    no2=eval(input("Enter No 2:"))
    
    print("\nSimple Calculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    ch = input("Enter your choice 1-4: ")
    if ch == '1':
        result = add(no1, no2)
        operation = "Addition"
    elif ch == '2':
        result = sub(no1, no2)
        operation = "Subtraction"
    elif ch == '3':
        result = mul(no1, no2)
        operation = "Multiplication"
    elif ch == '4':
        result = div(no1, no2)
        operation = "Division"

    if result is not None:
        print(f"{operation} result: {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

main()