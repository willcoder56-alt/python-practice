# where the fuck the function
cards = [5,7,9,10,3,4]
empty = []
def isEmpty(lst):
  if len(lst) == 0:
    return True
  for i in range(len(lst)):
    if lst[i] != "":
      return False
  return True

def push(lst, item):
  if len(lst) == 0:
    lst.append(item)
    return True
  for i in range(len(lst)):
    if lst[i] != "":
      return 
  lst.append(item)
  return True

def peek(lst):
  if len(lst) != 0:
    temp_index = (len(lst))-1
    return lst[temp_index]
  else:
    return

print(peek(cards))
print(isEmpty(cards))
print(push(cards,6))
print(peek(cards))
print(peek(empty))
print(isEmpty(empty))
print(push(empty,6))
print(peek(empty))