def insertion_sort( mylist ):
  for i in range(1, len(mylist)):
    key = mylist[i]
    k = i
    while k > 0 and key < mylist[k - 1]:
        mylist[k] = mylist[k - 1]
        k -= 1
    mylist[k] = key
  print(mylist)


insertion_sort([4, 3, 2, 10, 12, 1, 5, 6, 15, 7, 99, 4, 35, 120, 10, 1])