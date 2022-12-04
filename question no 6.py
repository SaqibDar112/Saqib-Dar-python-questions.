def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 2, 5, 2, 5, 1, 3, 7, 9]))