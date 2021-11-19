# 標準入力を受け付ける。
A, B, C = map(int, input().split())

# 乗数が偶数の場合、A, Bともに正の値となる。 ⏩A, Bの絶対値を取得して、A, Bの大小比較をすると良い。
# 乗数が奇数の場合、正のA or 正のBのみ正の値となり、負のA or 負のBのみ負の値となる。 ⏩そのままA, Bの大小比較をすると良い。
if C % 2 == 0:
    A = abs(A)
    B = abs(B)

# A, Bの大小比較。
if A == B:
    print('=')
elif A > B:
    print('>')
else:
    print('<')
