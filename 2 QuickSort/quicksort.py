## QuickSort.
## Works with 3 different pivot types, as per the quesion.
##

comparisons = 0


## Quicksort - sorts in place.
##
def quicksort(A, l , r, pivotType):
    global comparisons

    ##print(str(A), str(l), str(r))
       
    if r - l <= 0:
        return A

    # update comparison count
    comparisons += r - l 
       
    p = choosePivotPosition(A, l , r, pivotType)

    ### ensure pivot at first position
    A[l], A[p] = A[p], A[l]
         
    # partition around p
    i = l+1
    j = l+1
    while j <= r:
        if A[j] < A[l]:
           A[i], A[j] = A[j], A[i]
           i+=1
        j+=1

    # swap the pivot with it's rightful place
    A[l], A[i-1] = A[i-1], A[l]

    # recursively do the sides
    quicksort(A, l, i - 2, pivotType)
    quicksort(A, i, r, pivotType)

## Gets the pivot, eithe rthe first, last or the "median of 3" value.
##
def choosePivotPosition(A, l, r, pivotType):
    # this is the bit to tweak!
    if (pivotType == 1):
        return l

    elif (pivotType == 2):
        return r

    ## calculate median of 3
    m = l + (r - l)//2
    vals = [A[l], A[r], A[m] ]
    chosenOne = sorted(vals)[1]

    ## which one was it?
    if (A[l] == chosenOne):
        return l
    if (A[r] == chosenOne):
        return r
    return m

## Verify an array is in sorted order
##
def verify(A):
    j = 0
    while j < len(A) - 1:
        if A[j] > A[j+1]:
            print("FAILED")
            return
        j+=1

    print("OK")
    
## MAIN ##

if __name__ == "__main__":
    
    f = open("./QuickSort.txt", "r")
    data = [int(line) for line in f]
       
    data1 = data[:]
    data2 = data[:]
    f.close()

    print("Loaded file, now sorting")

    comparisons = 0
    quicksort(data, 0, len(data) - 1, 1)
    print ("Question 1: " + str(comparisons))
    verify(data)
    comparisons = 0

    quicksort(data1, 0, len(data1) - 1, 2)
    print ("Question 2: " + str(comparisons))
    verify(data1)

    comparisons = 0 
    result = quicksort(data2, 0, len(data2) - 1, 3)
    print ("Question 3: " + str(comparisons))
    verify(data2)

    print ("Done!")