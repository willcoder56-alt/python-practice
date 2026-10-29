def bubble_sort(lst):
  n = len(lst)
  for i in range(n-1):
    for j in range(n-i-1):
      if lst[j] > lst[j+1]:
        temp = lst[j]
        lst[j] = lst[j+1]
        lst[j+1] = temp
  return lst
a = [2,3,4,5,6,7,8,9,1]
b = [45,75,34,654,23,543,65,876,98,23,656,3,54,9,999]
print(bubble_sort(a))
print(bubble_sort(b))