import numpy as np

print("My numpy version:", np.__version__)

randm = []
for i in range (100):
    n = np.random.randint(1,20)
    randm.append(n)

# print ("random list:", randm)

randomArray = np.random.randint(1,6, size = 1000000)
print("Random array",randomArray.shape, randomArray.size)



count = [0]*5 
for number in randomArray:
    count[number - 1] +=1

for i, count in enumerate(count):
    print (f"Number of {i+ 1} is {count}")

""" print("The amount of 1 in list:", count)

print(f"The amount of 1 in list: {count} ")

print("Finished.")  """
count = [0,0,0,0,0]
for number in randomArray:
    if number == 1:
        count[0] += 1
    elif number == 2:
        count[1] += 1
    elif number == 3:
        count[2] += 1
    elif number == 4:
        count[3] += 1
    elif number == 5:
        count[4] += 1
print("Number of 1,", count[0])
print("Number of 2,", count[1])
print("Number of 3,", count[2])
print("Number of 4,", count[3])
print("Number of 5,", count[4])

counting =[0]*5
for digit in range (1,6):
    for number in randomArray:
        if number == digit:
            counting[digit-1] += 1

for digit, counting in enumerate(count):
    print (f"Number of digit {digit+1} is {counting}")

