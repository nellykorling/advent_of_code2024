def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

with open('input1.txt', 'r') as file:
    input = file.read()

left_list = []
right_list = []

for i in range(len(input.split('\n'))):
    left_list.append(input.split('\n')[i].split(' ')[0])
    right_list.append(input.split('\n')[i].split(' ')[3])

left_list = quick_sort(left_list)
right_list = quick_sort(right_list)

diff = 0

for i in range(len(left_list)):
    diff += abs(int(left_list[i]) - int(right_list[i]))

print(diff)
