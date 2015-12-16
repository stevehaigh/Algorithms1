
## The idea is to implement merge sort.
## However, to pass the Coursera homework we need to  count how many times we spot an inversion
## during the merge process. An inversion is simply the situation where the right hand value is larger
## than the left when merging 2 arrays.


## Merge 2 arrays and count inversions found when doing so
##
def mergeandcountinversions(left, right, count):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            ## inversions may have been found
            if (i  < len(left)):
                count += len(left) - i

    result += left[i:]
    result += right[j:]
    return result, count

## Basic recursive mergesort implementation
##
def mergesort(list, count):
    if len(list) < 2:
        return list, 0
    middle = len(list) / 2
    left, li = mergesort(list[:middle], count)
    right, ri = mergesort(list[middle:], count)
    count += li
    count += ri
    return mergeandcountinversions(left, right, count)

if __name__ == "__main__":
    inversions = 0

    f = file("./IntegerArray.txt", "r")
    data = [int(line) for line in f]
    f.close()

    newarray, i = mergesort(data, inversions)
    print i