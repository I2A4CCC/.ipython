palindrome = input('enter a four digit integer: ')
palindrome.strip()
reversed_pal = list(reversed(palindrome.strip()))
print(reversed_pal)
if reversed_pal[:2] == palindrome[2:]:
    print("YES")
else:
    print("NO")



