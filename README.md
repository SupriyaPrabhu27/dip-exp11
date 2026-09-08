# Exp-11- Record-IMPLEMENTATION OF HUFFMAN CODING
# name : SUPRIYA PRABHU
# REG : 212224240165

# Huffman-Coding
# Aim
# To implement Huffman coding to compress the data using Python.

# Software Required
Anaconda - Python 3.7
Algorithm:
# Step1:
Get the input string

# Step2:
Create tree nodes

# Step3:
Main function to implement huffman coding

# Step4:
calculate frequency of occurence

# Step5:
print the characters and its huffmancode

# Program:

```
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

```
# OUTPUT 

<img width="431" height="250" alt="image" src="https://github.com/user-attachments/assets/0a396015-4a83-49c8-9e5c-9131b7097021" />


# Result
Thus the huffman coding was implemented to compress the data using python programming
