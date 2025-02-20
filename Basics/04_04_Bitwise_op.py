# Bitwise ek tarika hai jisme numbers ko binary (0 aur 1) ki form me treat karke 
# un par operations perform kiye jate hain. Yeh operations directly computer ke hardware
#  ke sath kaam karte hain, is wajah se yeh fast hote hain.

 # Common Bitwise Operations:
    # 1. AND  (&) → Dono bits 1 hon to result 1 hota hai, warna 0
    # 2. OR   (|) → Agar koi ek bit bhi 1 ho to result 1 hota hai.
    # 3. XOR  (^) → Dono bits alag hon to 1, warna 0.
    # 4. NOT  (~) → Har bit ka ulta kar deta hai (1 ko 0 aur 0 ko 1). 
    # 5. Left Shift (<<) → Bits ko left move karne se number double hota hai.
    # 6. Right Shift (>>) → Bits ko right move karne se number half hota hai

a = 5  # Binary:  0101  
b = 3  # Binary:  0011  

print(a & b)  # Output: 1 (0001)
print(a | b)  # Output: 7 (0111)
print(a ^ b)  # Output: 6 (0110)
print(~a)     # Output: -6 (Inverted bits)
print(a << 1) # Output: 10 (1010)
print(a >> 1) # Output: 2  (0010)

