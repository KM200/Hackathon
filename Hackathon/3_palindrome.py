def is_palindrome(s):
    if(s==s[::-1]):
        return 1
    else:
        return 0


S=input("Enter the String: ")
result= is_palindrome(S)
print(result)
