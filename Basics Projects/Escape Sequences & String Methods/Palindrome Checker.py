## A palindrome means something that looks the same forward and backward.

## For example, the word "madam" is a palindrome because if you reverse it, it’s still "madam".

### Palindrome Checker (String Methods)

import re

def palindrome_checker():
    text = input("Enter text: ").lower()  # Convert to lowercase
    text = re.sub(r'[^a-z0-9]', '', text)  # Remove non-alphanumeric characters (letters & numbers only)
    
    if text == text[::-1]:  # Check if reversed text is same
        print("It's a palindrome!")
    else:
        print("Not a palindrome!")

palindrome_checker()


# Example
# Enter text: A man, a plan, a canal, Panama!
###    It's a palindrome!