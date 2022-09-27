import string
def palgram(str):
    char="abcdefghijklmnopqrstuvwxyz"
    for i in char:
        if i not in str.lower():
            return False
        return  True

string=input("Enter a string\n")
if(palgram(string)==True):
    print("is palgram")
else:
    print("not palgram")