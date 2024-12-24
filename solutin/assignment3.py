def fibonacci_list_comprehension(max_value):
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for _ in range(2, max_value) if fib_sequence[-1] + fib_sequence[-2] <= max_value]
    return fib_sequence

max_value = int(input("Enter the maximum value: "))
fib_seq = fibonacci_list_comprehension(max_value)
print(f"Fibonacci sequence up to {max_value}: {fib_seq}")
