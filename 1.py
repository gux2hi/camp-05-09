N = int(input())
B = list(map(int, input().split()))
C = list(map(int, input().split()))

T =""
for i in range(N):
    T= B[i]-C[i]
    print(T,end=' ')