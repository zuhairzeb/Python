'''
Function ek formula ki tarah hota hai jo ek baar likh diya jaye aur jab zaroorat ho, usay use kar liya jaye.
Jaise agar aap chai banana seekh lein, toh har baar naye tareeke se banane ki zaroorat nahi hoti. Bas wahi tareeqa (recipe) dobara
 istemal kar lete hain.

Python mein function bhi aise hi kaam karta hai. Aik baar likho, phir jab chaho use karo.

'''

# Example 1'

def salam_dena():  
    print("Assalam-o-Alaikum!")  

salam_dena()  # Function ko bulaya (call kiya)

# Example 2

def greet():
    print("Hello, World!")
greet()  

# Example 3

def salam_naam_se(name):
    print("Assalam-o-Alaikum, " + name + "!")

salam_naam_se("Zuhee")  # Function ko call kiya aur naam diya


# Example 4
def add_numbers(a, b):
    return a + b  # Do numbers ko add karega aur result dega

result = add_numbers(5, 7)  # Function ko call kiya aur values di
print(result)
