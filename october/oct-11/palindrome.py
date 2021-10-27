def palindrome(str1):
    forward = str1.lower()
    backward = ''
    for char in str1[::-1].lower():
        backward = backward + char
    if forward == backward:
        return print(f'{str1} is a palindrome!')
    else:
        return print(f'{str1} is NOT a palindrome!')

palindrome('Racecar')