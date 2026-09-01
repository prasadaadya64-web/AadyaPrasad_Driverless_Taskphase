



def multiply(A, B):
    if len(A[0]) != len(B):
        print("Matrix multiplication is not possible")
        return None

    result = []

    for i in range(len(A)):
        row = [] 
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)

    print("Resultant Matrix:")
    for row in result:
        print(row)

r1 = int(input("Enter the number of rows for Matrix A: "))
c1 = int(input("Enter the number of columns for Matrix A: "))

A = []
for i in range(r1):
     A.append(list(map(int, input().split())))

r2 = int(input("Enter the number of rows for Matrix B: "))
c2 = int(input("Enter the number of columns for Matrix B: "))

B = []
for i in range(r2):
    B.append(list(map(int, input().split())))

multiply(A, B)
   



    


    