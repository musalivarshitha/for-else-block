n=int(input())
if n>1:
    for divisor in range(2,n//2+1):
        if n%divisor==0:
            print('not a prime num')
            break
    else:
        print('its a prime num')
else:
    print('n is not a prime num')
