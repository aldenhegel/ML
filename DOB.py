from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 
import math

dataDg = load_digits()

DOB = input('Please input DOB: ')

for i,j in zip(DOB, range(len(DOB))):
    plt.subplot(math.ceil(len(DOB) / 6), 6, j + 1)
    plt.imshow(dataDg['images'][int(i)], cmap='gray')
    plt.title(f"This is {dataDg['target'][int(i)]}")

plt.show()