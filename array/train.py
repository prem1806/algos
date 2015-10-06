import math

def max_packed_schedule(trains_schedule):
	hash_arr = [0 for i in range(0, 24)]
	for i in range(0, len(trains_schedule)):
		each_train = trains_schedule[i]
		start, end = each_train[0], each_train[1]
		for k in range(start, end+1):
			hash_arr[k] += 1
	print hash_arr
	max_packs = []
	maxi = max(hash_arr)
	for i in range(0, len(hash_arr)):
		if hash_arr[i] == maxi:
			max_packs.append(i)
	return max_packs


if __name__ == "__main__":
	num_of_trains = raw_input()
	num_of_trains = int(num_of_trains)
	trains_schedule = []
	for i in range(0, num_of_trains):
		start, end = raw_input().split()
		start, end = int(start), int(end)
		trains_schedule.append((start, end))
	print max_packed_schedule(trains_schedule)