from sum import sum
from subtract import subtract

def main():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))

    operation = input("Choose operation - 'sum' or 'subtract': ").strip().lower()

    if operation == 'sum':
        result = sum(a, b)
        print(f'Sum of {a} and {b} is {result}')
    elif operation == 'subtract':
        result = subtract(a, b)
        print(f'Difference of {a} and {b} is {result}')
    else:
        print("Invalid operation chosen, please select 'sum' or 'subtract'.")

if __name__ == "__main__":
    main()
