names = ["Darcy", "Elizabeth", "Bingley", "Jane", "Lydia"]

names.append("Liya")

names = names + ["Aibike"]

for item in names:
    print(item + " hello?")
    print (item[0])
    for g in item:
        print(g)

print("Finished")


for k in range (len(names)):
    print(k,names[k])

hundrednames = [f"name_{i}" for i in range (100)]
print (hundrednames)



