def LinearSearch(array, x):
      for i in range (0, len(array)):
            if (array[i] == x):
                  return i
      return -1

array = input("Enter the list of numbers:").split()
array = [int(y) for y in array]
x = int(input())

A = LinearSearch(array, x)
if(A == -1):
    print("Element not found")
else:
    print("Element found at index: ", A)


