def InsertionSort(A):
      for i in range(1,len(A)):
            temp = A[i]
            j = i-1
            while (j >= 0 and A[j]>temp):
                  A[j+1] = A[j]
                  j =j-1
            A[j+1] = temp
A = input("Enter the list of numbers:").split()
A = [int(x) for x in A]
InsertionSort(A)
print(A)
