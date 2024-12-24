def build_row(i, n):
    row = " " * (n - i)
    
    # Add increasing characters
    for j in range(1, i + 1):
        row += chr(64 + j) + " "
    
    # Add decreasing characters
    for j in range(i - 1, 0, -1):
        row += chr(64 + j) + " "
    
    return row.strip()

def print_pattern_function(n):
    for i in range(1, n + 1):
        print(build_row(i, n))

n = int(input("Enter the number of rows: "))
print_pattern_function(n)
