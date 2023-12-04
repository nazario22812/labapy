def check(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2 == 0 or n% 3 ==0:
        return False
    
    i = 5
    while i*i<=n:
        if n% i == 0 or n% (i+2) == 0:
            return False
        i+=6
    return True


n = int(input())
if check(n):
    print(f"{n} jest liczbą pierwszą")
else:
    print(f"{n} nie jest liczbą pierwszą")