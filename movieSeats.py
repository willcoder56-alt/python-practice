rows, cols = 30, 20
user_row = 0
user_col = 0
#setup array
matrix = [["O" for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
  print(matrix[i])
while str(user_row).lower() != "done" or str(user_col).lower() != "done":
#get user input and check if == "done"
  user_row = input("choose a row(0-" + str(rows-1) + ") or type done to finish")
  if str(user_row).lower() == "done": 
    break
  try:
    int(user_row)
  except ValueError:
    print("Not a number or done")
    break
  user_col = input("choose a column(0-" + str(cols-1) + ") or type done to finish")
  if str(user_col).lower() == "done":
    break
  try:
    int(user_col)
  except ValueError:
    print("Not a number or done")
    break
  #if not ending convert str to int
  user_col = int(user_col)
  user_row = int(user_row)
  #check if pos is "x" if not put in x
  if (matrix[user_row][user_col]) == "X":
    print("the seat is not available")
    continue
  else:
    matrix[user_row][user_col] = "X"
    for i in range(rows):
      print(matrix[i])

