text = input("Enter Your Input String : ").lower()
vowels = "aeiou"
count = 0
for char in text:
  if char in vowels:
    count = count + 1
print(f"Number of vowels in the given string {text} is {count}")
    
