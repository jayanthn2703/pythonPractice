### Question 6: Check if 97 is a prime number
num=96
is_prime= True
if num<2:
    is_prime=False
for i in range(2,num):
    if num%i==0:
        is_prime=False
    break
print(is_prime)
