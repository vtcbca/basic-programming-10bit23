def build_row(i, n):
    row = " " * (n - i)
    for j in range(1, 2 * i):
        row += str(j) + " "
    return row.strip()

def print_triangle_function(n):
    for i in range(1, n + 1):
        print(build_row(i, n))

n = int(input("Enter the number of rows: "))
print_triangle_function(n)
