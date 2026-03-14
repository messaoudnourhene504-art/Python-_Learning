# Simple Calculator Tool
# Created by: messaoudnourhene504-art

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error! Division by zero."
    return x / y

def main():
    print("\n" + "="*25)
    print("   PYTHON CALCULATOR   ")
    print("="*25)
    
    try:
        num1 = float(input("Enter first number: "))
        print("Select operation: +, -, *, /")
        op = input("Operation: ")
        num2 = float(input("Enter second number: "))

        if op == '+': print(f"Result: {add(num1, num2)}")
        elif op == '-': print(f"Result: {subtract(num1, num2)}")
        elif op == '*': print(f"Result: {multiply(num1, num2)}")
        elif op == '/': print(f"Result: {divide(num1, num2)}")
        else: print("Invalid Operation!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

    print("="*25)

if __name__ == "__main__":
    main()
