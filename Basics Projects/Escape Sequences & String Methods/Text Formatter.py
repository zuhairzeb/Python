### Text Formatter (Escape Sequences & String Methods)

def text_formatter():
    text = input("Enter a sentence: ")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title Case: {text.title()}")

text_formatter()