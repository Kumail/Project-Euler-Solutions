num_1 = 1
num_2 = 2
sum = 0
even = 0

four_million = 4000000

while even<four_million:
    sum = num_1 + num_2
    num_1 = num_2
    num_2 = sum
    
    if(sum%2 == 0):
        even += sum

print(even)