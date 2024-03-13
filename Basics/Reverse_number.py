def reverse_number(num):
    n = num 
    reverse_number = 0
    while n>0:
        last_digit = n%10
        reverse_number = reverse_number*10+last_digit
        n =n //10
    return reverse_number

print(reverse_number(12345))


"""
TC = O(log10n)
SC = O(1)
"""