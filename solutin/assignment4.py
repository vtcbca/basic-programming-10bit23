def reverse_string_join(s):
    return ''.join(reversed(s))

string = input("Enter a string: ")
reversed_string = reverse_string_join(string)
print(f"Reversed string: {reversed_string}")
