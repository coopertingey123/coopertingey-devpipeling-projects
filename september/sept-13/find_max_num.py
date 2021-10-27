nums = [1, 4, 3, 45, 6, 23]

def find_max(list_of_nums):
  max_num = list_of_nums[0]
  for num in list_of_nums:
    if num > max_num:
      max_num = num
  return print(max_num)

find_max(nums)