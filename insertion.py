l = [4, 3, 2, 10, 12, 1, 5, 6, 15, 7, 99, 4]

print("{} {}".format(l, "Original"))

for i in range(len(l) - 1):
  a = l[i + 1]
  b = l[i]
  if l[i + 1] <= l[i]:
    if l[i + 1] <= l[0]:
      del l[i + 1]
      l.insert(0, a)
      print("{}".format(l))
      c = l[0:i]
    else:
      del l[i + 1]
      l.insert(len(c), a)
      c = l[0:i]
      print("{}".format(l))

  