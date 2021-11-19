import bisect

# 標準入力を受け付ける。
N, Q = map(int, input().split())

# 問題文より、A[0] < A[1] < A[2] ... < A[N - 1]なので、ソートする必要はない。
A = list(map(int, input().split()))

for _ in range(Q):
    # <方針> ###################################
    # 1. A[x - 1] <= q(x) < A[x + 1]のx値を算出する。
    # 2. qの値より前のAの配列の要素数をlとする。
    # 3. qの値より前のAの配列の要素数(l)分、数字を進めないといけないため、qの値をq + lにする。
    # 4. 1~3を繰り返す。
    ###########################################
    q = int(input())

    l = 0

    # 二分探索を用いて、A[x - 1] <= q(x) < A[x + 1]のx値を算出する。
    while True:
        # 1つ前のlの値。
        l_prev = l

        # bisect_right ###################
        # 参考 : https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3
        # 配列内にq + lに等しい値があれば、その値の右のidxを返す。
        # A[0]より小さいq + lが入力された場合、0を返す。
        # A[N - 1]より大きいq + l値が入力された場合、Nの値を返す。
        ##################################
        l = bisect.bisect_right(A, q + l)

        if l_prev == l:
            break
    print(q + l)
