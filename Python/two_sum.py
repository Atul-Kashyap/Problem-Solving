import pdb 
def two_sum(arr: list[int], target: int) -> list[int]:
    # if array is none or length of array is zero
    if arr is None or len(arr) == 0:
        return [-1, -1]
    pdb.set_trace()
    
    # two pointer one start from index 0 and other start from index (length of arr - 1)
    iter_1, iter_2 = 0, len(arr) - 1
    sorted(arr)
    pdb.set_trace()

    while iter_1 < iter_2:
        sum = arr[iter_1] + arr[iter_2]
        pdb.set_trace()
        if sum == target:
            return [iter_1, iter_2]
        elif sum > target:
            iter_2 = iter_2 - 1
        else:
            iter_1 = iter_1 + 1
    return [-1, -1]


if __name__ == "__main__":
    arr, target = [2, 7, 11, 15], 9
    result = two_sum(arr=arr, target=target)
    print(result)




    
