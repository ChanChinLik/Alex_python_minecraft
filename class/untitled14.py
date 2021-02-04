A = [10,25,31,2,4,6,99,-1,34]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] > A[j]:
            t = A[i]
            A[i] = A[j]
            A[j] = t
            print(A)
"""if A<B:
    t=A
    A=B
    B=t
if B<C:
    t=C
    C=B
    B=t
if A<B:
    t=A
    A=B
    B=t"""