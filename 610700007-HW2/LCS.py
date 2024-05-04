X="ABCBDAB"
Y="BDCABA"
def LCS_LENGTH(X,Y):
    m= len(X)
    n= len(Y)
    c=[[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
            else:
                c[i][j]=c[i][j-1]
    return c
def PRINT_ALL_LCS(c,X,Y,i,j):
    if i==0 or j==0:
        return set([""])
    if X[i-1]==Y[j-1]: #UL
        return set([Z+X[i-1] for Z in PRINT_ALL_LCS(c,X,Y,i-1,j-1)])
    else:
        U=set()

        if c[i-1][j] >= c[i][j-1]:#UP
            U.update(PRINT_ALL_LCS(c,X,Y,i-1,j))
        if c[i][j-1] >= c[i-1][j]:  #Left
            U.update(PRINT_ALL_LCS(c,X,Y,i,j-1))
        return U          
c=LCS_LENGTH(X,Y)
LCS_list=PRINT_ALL_LCS(c,X,Y,len(X),len(Y))
print(f"LCS length: {c[len(X)][len(Y)]}")
print(f"number of LCS: {len(LCS_list)}")
print("Printing all LCS")
print("\n".join(LCS_list))