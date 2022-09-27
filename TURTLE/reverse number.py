rev_num=0

def palindrome(n):
    global check
    while(n>0):
        global rev_num
        remainder=n%10
        rev_num=rev_num*10 +remainder
        n=n//10
    print("reverse number is" ,format(rev_num))
    if check==rev_num:
        print("Number is Palindrome✌")
    else:
        print("Number is not palindrome ")
n=int(input("enter a number"))
check=n
palindrome(n)
