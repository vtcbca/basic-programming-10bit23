def is_palindrome_join(s):
    return s == ''.join(reversed(s))

string = input("Enter a string: ")
if is_palindrome_join(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
 
