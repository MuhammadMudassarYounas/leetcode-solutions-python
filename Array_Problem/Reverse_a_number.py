n = 1234
result = 0

while n > 0:
    last_digit = n % 10
    result = result * 10 + last_digit
    n //= 10