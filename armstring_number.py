n = 371
temp = n
s = 0

while n > 0:
    digits = n % 10
    s = s + digits * digits * digits
    n //= 10

if s == temp:
    print(True)
else:
    print(False)
