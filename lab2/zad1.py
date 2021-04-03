def gauss_jordan_partial_pivoting(A,B):
    n = len(A)
    M = A

    for col in range(n):
        for row in range(col,n):
            if(abs(M[row][col]) > abs(M[col][col])):
                M[col], M[row] = M[row], M[col]
        for row in range(n):
            if row == col: continue
            q = M[row][col] / M[col][col]
            for m in range(n):
                M[j][m] -= q * M[col][m]
            B[row] -= q * B[col]

    for i in range(n):
        B[i] = B[i] / A[i][i]
        
    return B
