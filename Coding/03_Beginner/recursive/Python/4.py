def func_X(i):
    if i == 0:
        return X[0]
    return func_X(i-1) + X[i] + func_X(i-1)

N = int(input())
X = input()
print(func_X(N - 1))
