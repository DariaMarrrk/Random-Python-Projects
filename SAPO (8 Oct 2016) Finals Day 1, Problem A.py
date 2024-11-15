N = input('Enter a number N ')
N = int(N) 
#P = 0.0
#Q = 0.0
Can_obtain = False
T = 0
while (T!= N) and Can_obtain == False:
    S = 0
    T = T + 1
    while (S!= T) and Can_obtain == False:
        Q = (T - S + 1)/2
        P = N / (S + T)
        if P == Q:
            Can_obtain = True
        if Can_obtain == False:
            S = S + 1
 
if Can_obtain == True:
    print('Can obtain ')
    print(S, T, P, Q)
else: 
    print('Cannot obtain ')
    print(S, T, P, Q)
