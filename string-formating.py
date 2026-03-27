t = input("What is the time you go to work? ")
print("You go to work at {t:.2f}".format(t=float(t)))
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(len(thislist)):
    print("The fruit at index {} is {}".format(i, thislist[i]))

l = ["apple", "banana", "cherry"]
d = ("John", "Doe", 30)
l.extend(d)
print(l)  # Output: List: None