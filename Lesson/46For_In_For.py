print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8")
print("---------------------------------")
x = 1
y = 2 * x
print("2 x", x, "=", y)
print("---------------------------------")
x = x + 1
y = 2 * x
print("2 x", x, "=", y)
x = x + 1
y = 2 * x
print("2 x", x, "=", y)
x = x + 1
y = 2 * x
print("2 x", x, "=", y)
print("---------------------------------")
for x in range(12):
    x = x + 1
    y = 2 * x
    print("2 x", x, "=", y)
print("---------------------------------")
for x in range(12):    
    print("2 x", x+1, "=", 2*(x+1))
print("---------------------------------")
for x in range(12):
    for y in range(12):
        print(x+1,"x", y+1, "=", (x+1)*(y+1))