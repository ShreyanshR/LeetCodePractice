from typing import List, Tuple

def find_pairs_with_sum(arr: List[int], target: int) -> List[Tuple[int, int]]:
    #Write a function that takes in an array of integers, which can be both positive and negative, along with a target integer. 
    # The function should return all unique pairs of integers from the array that sum up to the target integer.
    
    arr.sort()

    print(arr)

    begin = 0
    end = len(arr) - 1

    sum_v = 0
    res = []

    while begin < end:
        sum_v = arr[begin] + arr[end]

        print(f'sum : {sum_v}')

        if sum_v == target:
            res.append([arr[begin], arr[end]])
        
            begin += 1
            end -= 1

        elif sum_v < target:
            #this thing will work because it's a sorted array.
            # so if sum <9, the 1st element is too small, so we need to move it forward
            #the  previous program was not doing pairwise, it was doing just begin & end from an array
            begin += 1
        
        else:
            end -=1

        print(res)

    return res


def find_paris_with_sum_1(arr: List[int], target: int):
    result_set = set()

    complementary_set = set()

    for num in arr:
        complement = target - num #so what it is trying to do is it's creating a comp if the comp in comp_set, the num + comp = traget

        if complement in complementary_set:
            result_set.add(tuple(sorted[num, complement]))
            #num + comp = target
        complementary_set.add(num)

    return list(result_set)



if __name__ == "__main__":
    find_pairs_with_sum([1, 2, 3, 9], 11)

