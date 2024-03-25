def palindrome(string,i):
    if i >=len(string)//2:
        return True
    if string[i] != string[len(string)-i-1]:
        return False
    return palindrome(string,i+1)



str ='mom'
x = palindrome(str,0)
print(x)