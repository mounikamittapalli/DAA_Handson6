#In non_randomized pivot is chosen as last element
#In randomized pivot is chosen randomly
import random
def partition(A, p, r):
   x=A[r]# pivot for non_randomized
   #print(f"pivot used in non_randomized,{x}")
   i=p-1
   for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
   A[i + 1], A[r] = A[r], A[i + 1]
   return i + 1
def quicksort(A,p,r):
 if p < r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
def randomized_partition(A, p, r):
    i = random.randint(p, r)  # Random pivot index
    A[r], A[i] = A[i], A[r]  # Swap pivot to the end
    pivot_value=A[r]
    #print("pivot used in non_randomized,{pivot_value}")
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)  # Randomized pivot selection
        randomized_quicksort(A, p, q - 1)  # Sort left subarray
        randomized_quicksort(A, q + 1, r)  # Sort right subarray

def generate_random_array(size):
    # Generate a random array of integers for a given size
    return [random.randint(0, 99) for i in range(size)]

# Example usage
if __name__ == "__main__":
    size = random.randint(5, 5)  # Random size between 100 and 15000, we can change the numbers as needed
    arr = generate_random_array(size)
    # print("Generated array: of size: ", arr, size)
    print("Original array:", arr)
    arr_non_random = arr.copy()
    quicksort(arr_non_random ,0,len(arr_non_random ) - 1)
    print("Array after Non_randomized quicksort", arr_non_random )
    arr_randomized= arr.copy()
    randomized_quicksort(arr_randomized, 0, len(arr_randomized ) - 1)
    print("Array after randomized quicksort,pivot:", arr)

