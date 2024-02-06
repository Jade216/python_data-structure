def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    freq_nums = {}
    for num in nums:
        freq_nums[num] = freq_nums.get(num, 0) + 1

    max_freq = max(list(freq_nums.values))

    for (num, freq) in freq_nums.items:
        if freq == max_freq:
            return num

