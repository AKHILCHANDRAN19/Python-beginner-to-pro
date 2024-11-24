end_range = int(input("Enter the range: \n"))
sum_even = 0
for i in range(0, end_range + 1, 2):
    sum_even += i
print(f"The sum of even numbers up to {end_range} is {sum_even}")
