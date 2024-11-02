def quick_sort(arr):
    # 递归终止条件：如果数组长度小于或等于1，则不需要排序
    if len(arr) <= 1:
        return arr

    # 选择基准值，这里选择列表中的最后一个元素
    pivot = arr[-1]

    # 定义三个空列表用于存放小于、等于、大于基准值的元素
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    # 遍历数组中的每个元素，并根据其与基准值的关系放入对应的列表
    for element in arr:
        if element < pivot:
            less_than_pivot.append(element)
        elif element == pivot:
            equal_to_pivot.append(element)
        else:
            greater_than_pivot.append(element)

    # 递归地对小于和大于基准值的子数组进行快速排序，然后合并结果
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


# 示例
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)