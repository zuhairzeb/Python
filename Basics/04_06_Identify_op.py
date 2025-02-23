# Python mein identity operators yeh check karte hain ke do variables ek hi cheez ko point kar rahe hain ya nahi.

# Do tarah ke identity operators hote hain:

# is → Check karta hai ke do variables ek hi object hain.
# is not → Check karta hai ke do variables alag objects hain.

# 🚗 Socho ke tumhare paas ek car hai.

# Agar do log ek hi car ko dekh rahe hain, to dono ek hi object ko refer kar rahe hain. (Ye is wala case hoga)
# Agar do log alag alag cars ko dekh rahe hain, lekin dono ka color aur model same hai, to cars alag hain. (Ye is not wala case hoga)

# Example 1:
car1 = ["Toyota", "Red"]
car2 = car1  # `car2` ko `car1` ka reference mila, yani dono ek hi car hain

print(car1 is car2)    # True (kyunki dono ek hi cheez hain)
print(car1 is not car2) # False (kyunki dono alag nahi hain)

# ✅ Yahan dono variables ek hi jagah (memory) mein hain.
# ✅ Agar car1 mein kuch change karo, to car2 bhi change ho jayega!

# Example 2:

carA = ["Honda", "Blue"]
carB = ["Honda", "Blue"]  # `carB` ek naya object hai

print(carA is carB)    # False (kyunki dono alag hain)
print(carA is not carB) # True (kyunki dono same nahi hain)

# ✅ Dono ki values same hain, lekin ye alag alag jagah par hain!
# ✅ Agar carA mein kuch change karoge, to carB farq nahi padega.