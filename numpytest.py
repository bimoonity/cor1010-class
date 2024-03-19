import numpy as np

print("My numpy version:", np.__version__)

randm = []
for i in range (1000000):
    n = np.random.randint(1,20)
    randm.append(n)

print ("random list:", randm)

finding = randm.find(20)
print(finding)