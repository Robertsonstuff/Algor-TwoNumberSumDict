#hash table {} - O(n) Time, O(n) Space -> best for time

def twoNumberSum(array, targetSum):
    # nums at this point is an empty dict or hash table.
    # the for loop will search through the array and check if 10 - num (the iteraterable in the array) is equal to the potentialMatch.
    # then the if statement simply checks that the potentialMatch is in the dictionary we created(nums). If so, print the match. The return also calls the num, which prints the iterable that made produces the answer.
    # if the potential match did not occur, the else simply adds the iterable or "key" (num) and assigns a value of 'true'. No matter the order of the array, the for loop will continue until all the iterables in the array have been searched.
    # after the loop has finished. It will either print your potential match if statement (line13) or ... "No dice grandma" (line16).
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return potentialMatch, num
        else:
            nums[num] = True
    return("No dice grandma!!\nThe numbers in the array don't match the target number.")

result = twoNumberSum([3,5,-4,-2,8,11,6], 10)
print(result)