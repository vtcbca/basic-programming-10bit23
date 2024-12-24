def factorial_list_comprehension(n):
    return 1 if n == 0 else [i for i in range(1, n+1)].reduce(lambda x, y: x * y)

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial_list_comprehension(number)}")
