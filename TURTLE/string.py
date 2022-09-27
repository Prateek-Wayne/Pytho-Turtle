s=input("enter a string\n")
def Palindrome(s):
   return s==s[::-1]
rev=Palindrome(s)
if rev:
    print("Yes Palindroem")
else:
    print("No..")
