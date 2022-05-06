print("Hello World")
with open('results.txt', 'w') as f:
  for i in range(100):
    for j in range(i):
      f.write(" ")
    for j in range(i, 100):
      f.write("*")
    f.write('\n')
