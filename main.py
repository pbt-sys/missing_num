print("This program finds the missing number in a list of integers\n")

nums = [0,1,3,4,5,2,6,7,8]

print("given a list of " + "".join(str(nums)))

len_nums = len(nums)
sorted_nums = sorted(nums)

total_len_nums = len_nums + 1
control_list = [x for x in range(total_len_nums)]

for i in range(len(control_list)):
	try:
		check = sorted_nums[i] ^ control_list[i]
	except IndexError:
		print("missing number is " + str(i))
		break
	if check != 0:
		print("missing number is " + str(i))
		break

