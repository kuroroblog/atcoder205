# 標準入力を受け付ける。
N = int(input())

A = list(map(int, input().split()))

# 数字の出現回数を配列でメモしておく。
# num_cnt_list[0]の要素は利用しない。
num_cnt_list = []
for _ in range(N + 1):
    # 数字の出現回数の初期値を0としておく。
    num_cnt_list.append(0)

for i in range(N):
    num_cnt_list[A[i]] += 1
    # 一度でも2回以上同じ数字が出現したら`No`, そうでなければ`Yes`を出力する。
    if num_cnt_list[A[i]] > 1:
        print('No')
        exit()

print('Yes')
