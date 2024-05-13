N,L = map(int, input().split())
scores = [] # 学生、試験ごとのスコアを格納する2次元配列

for i in range(L):
    student = list(map(int, input().split()))
    scores.append(student)

tops = {}
for i in range(N):
    top_score = 0
    top_student = 0
    for j in range(L):
        if( top_score < scores[j][i]):
            top_score = scores[j][i]
            top_student = j
    if(top_student + 1 in tops):
        tops[top_student + 1] += 1
    else:
        tops[top_student + 1] = 1


max_val = max(tops.values())
min_student = L
for i in tops.keys():
    if(tops[i] == max_val and i < L ):
        min_student = i

print(f'{min_student} {max_val}')
