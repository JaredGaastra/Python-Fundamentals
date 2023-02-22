def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    smallestNum = nums[0]

    for lowestNum in nums:
        if lowestNum >= lowest and lowestNum < smallestNum:
            print(lowestNum)

    for highestNum in nums:
        if highestNum <= highest and highestNum > smallestNum:
            print(highestNum)

in_range([10, 20, 30, 40, 50], 15, 30)            
