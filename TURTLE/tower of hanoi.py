n=int(input("Enter number of disk : "));
def twh(n,source,auxx,dest):
    if(n>0):
        twh(n-1,source,dest,auxx)
        print(" move disk ",n,"from ",source,"to",dest)
        twh(n-1,auxx,source,dest)

source='A'
auxx='B'
dest='C'
twh(n,source,auxx,dest)