n=int(input())
for divisor in range(2,n//2+1):
    if n%divisor==0:
        print('not a prime num')
    else:
        print('its a prime num')
