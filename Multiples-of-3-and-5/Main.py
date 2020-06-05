sum = 0
limit = 1000

for x in range(limit):
    if(x%3==0 or x%5==0):
        sum += x

print("The sum of multiples is:" ,sum)