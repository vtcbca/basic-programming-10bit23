def print_pattern_function(rows):
    for i in range(1, rows + 1):
        row = ""
        for j in range(i):
            row += "* "
        print(row.strip())

rows = int(input("Enter the number of rows: "))
print_pattern_function(rows)
