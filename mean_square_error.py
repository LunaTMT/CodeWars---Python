def solution(a, b):
    return sum([pow(abs(i - j), 2) for i, j in zip(a, b)]) / len(a)