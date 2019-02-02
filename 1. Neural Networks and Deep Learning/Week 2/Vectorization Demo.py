import numpy as np
import time

# Creating a million dimensional vector
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Explicit for loop
c = 0
start = time.time()
for i in range(1000000):
	c += a[i] * b[i]
end = time.time()
print(c)
print("Explicit for loop's time " + str(1000*(end-start)) + "ms")

# Vectorized version

c = 0
start = time.time()
c = np.dot(a,b)
end = time.time()
end = time.time()
print(c)
print("Vectorization time " + str(1000*(end-start)) + "ms")