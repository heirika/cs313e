"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Erika Chang, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

HMC2674
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    #base case
    if start >= len(nums):
        return target == 0
    if group_sum(start +1, nums, target - nums[start]):
        return True
    return group_sum(start +1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    #base case
    if start >= len(nums):
        return target == 0
    #if there is a 6, it is subtracted from the total
    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - 6)


    if group_sum_6(start + 1, nums, target - nums[start]):
        return True

    return group_sum_6(start + 1, nums, target)



def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """

    if start >= len(nums):
        return target == 0
    #chooses current start, skips next
    choose_start = group_no_adj(start + 2, nums, target - nums[start])
    #skips start index, chooses next value
    choose_next = group_no_adj(start + 1, nums, target)

    return choose_next or choose_start

def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 is 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """

    if start >= len(nums):
        return target == 0

    if nums[start] % 5 == 0:
        if nums[start + 1] and start + 1 < len(nums):
            #current val is mutiple of 5 and 1 follows
            return group_sum_5(start + 2, nums, target - nums[start])
        else:
            #start is a mutiple of 5
            return group_sum_5(start +1, nums, target - start[nums])

    else:
        return (group_sum_5(start + 1, nums, target - nums[start]) or
                group_sum_5(start + 1, nums, target))

def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    same_sum = nums[start]
    count = 1
    #if nums are same and in sucession, counted and added to same_sum
    while start + count < len(nums) and nums[start + count] == nums[start]:
        same_sum += nums[start + count]
        count += 1

    #include clump
    if group_sum_clump(start + count, nums, target - same_sum):
        return True
    elif group_sum_clump(start + count, nums, target):
        return True

    return False



def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def can_split(index, group1, group2):
    #base case: checks if sum of 2 groups are equal
        if index == len(nums):
            return sum(group1) == sum(group2)

        return (can_split(index + 1, group1 + [nums[index]], group2) or
                can_split(index + 1, group1, group2 + [nums[index]]))
    return can_split(0, [], [])

def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def can_split(index, sum1, sum2):
        #base case
        if index == len(nums):
            #checks if sum1 is mutiple of 10, other is odd
            return (sum1 % 10 == 0 and sum2 % 2 == 1) or (sum2 % 10 == 0 and sum1 % 2 == 1)
        #recursive cases, current index in sum1 or sum2
        return (can_split(index + 1, sum1 + nums[index], sum2) or
                can_split(index + 1, sum1, sum2 + nums[index]))
    return can_split(0, 0, 0)

def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """

    def can_split(index, group1, group2):
        #base case: checks if 2 sum are equal
        if index == len(nums):
            return sum(group1) == sum(group2)
        num = nums[index]
        #if index is mutiple of 5, add to group1
        if num % 5 == 0:
            return can_split(index + 1, group1 + [num], group2)
        #if index mutiple of 3, add to group2
        elif num % 3 == 0:
            return can_split(index + 1, group1, group2 + [num])
        else:
            return (can_split(index + 1, group1 + [num], group2) or
                    can_split(index + 1, group1, group2 + [num]))
    if not nums:
        return False
    return can_split(0, [], [])
