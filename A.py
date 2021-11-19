# 標準入力を受け付ける。
A, B = map(int, input().split())

# 比例式を考えて、演算する。
# 100 : B = A : X ⏩ B * A = 100 * X ⏩ X = (B * A) / 100。
print((B * A) / 100)
