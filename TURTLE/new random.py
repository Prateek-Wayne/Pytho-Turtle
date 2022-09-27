def facto(int(n)):
    if int(n)==0:
        return 1
    else:
        facto(n-1)*n


facto(5)