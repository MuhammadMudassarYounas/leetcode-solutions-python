def Remove_Right_Most(N):
    if(N & (N-1))==0:
        print("The number is power of 2")
    else:
        print("The number is not power of 2")

Remove_Right_Most(12)