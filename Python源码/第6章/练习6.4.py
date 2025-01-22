def find_max_value(lst):
    """
    找到列表中的最大值。

    参数:
    lst: 列表。

    返回值:
    列表中的最大值。
    """
    if not lst:
        return None  # 空列表返回 None
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

# 示例用法
numbers = [1, 5, 3, 9]
max_value = find_max_value(numbers)
print("最大值:", max_value)  # 输出: 最大值: 9
