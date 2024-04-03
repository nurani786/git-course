#This is a whack way of doing it.

#Here is the more efficient 
palindrome = lambda x:'Palindrome' if str(x)==str(x)[::-1] else 'Not Palindrome'

num = int(input('Enter a number: '))

print(palindrome(num))

# Anothe example 
palindrome = lambda x:'Palindrome' if str(x)==str(x)[::-1] else 'Not Palindrome'

num = int(input('Enter a number: '))

print(palindrome(num))