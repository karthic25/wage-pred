print("Hello World")
for i in range(100):
  for j in range(i):
    print(" ", end="")
  for j in range(i, 100):
    print("*", end="")
  print()
