def power(x,n=2):
    s = 1
    while n >0:
        n=n-1
        s=s*x
    return s

def power(x,n,j=2):
    s=1
    while n > 0:
        n=n-1
        s=s*(x+j)
    return s,'second function'
