while(True):
    A,B = input().split()
    A = int(A)
    B = int(B)
    if A == 0 and B == 0:
        break
    
    if A > B:
        if A % B == 0:
            print("multiple")
        else:
            print("neither")
    if A < B:
        if B % A == 0:
            print("factor")
        else:
            print("neither")