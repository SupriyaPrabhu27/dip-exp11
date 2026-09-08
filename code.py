import math


p = [0.40, 0.30, 0.15, 0.10, 0.05]

code = ["1", "01", "001", "0000", "0001"]


print("Codewords")


for i in range(5):
    print("a", i + 1, "=", code[i])


H = 0

for x in p:
    H = H + x * math.log2(1 / x)


L = 0

for i in range(5):
    L = L + p[i] * len(code[i])


E = (H / L) * 100


R = 100 - E


print("\nEntropy =", round(H, 3), "bits/symbol")
print("Average Code Length =", round(L, 3), "bits/symbol")
print("Efficiency =", round(E, 2), "%")
print("Redundancy =", round(R, 2), "%")
