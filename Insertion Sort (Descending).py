# Using Insertion Sort
def insertionsort(arr):
  '''This func can sort array in descending order'''
  for i in range(1, len(arr)):
    key = arr[i] # this var temporarily stores the number to bring to the front
    j = i - 1
    while j >= 0 and arr[j] < key:
      arr[j + 1] = arr[j]
      j = j - 1
    arr[j + 1] = key

lst = [9, 5, 1, 4, 3]
insertionsort(lst)
print("Descending Sorted Array: ", lst)