from operator import le


text = "Syed Salahuddin"

fre = {
    
}

for char in text:
    if char in fre:
        fre[char] += 1
    else:
        fre[char] = 1
        
    
print(f"=== Character Frequency Counter: ")
print(f"Text: {text}")
print(fre)

print(f"\nTotal Characters: {len(text)}")
print(f"Unique Characters: {len(fre)}")
