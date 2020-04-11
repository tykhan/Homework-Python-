
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_num = 0
    sum_of_num = 0
    for element in arr:
        if element > 0:
            count_num += 1
        elif element < 0:
            sum_of_num += element
    return [count_num, sum_of_num]

