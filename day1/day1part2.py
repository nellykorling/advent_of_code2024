with open('input1.txt', 'r') as file:
    input = file.read()

left_list = []
right_list = []

for i in range(len(input.split('\n'))):
    left_list.append(input.split('\n')[i].split(' ')[0])
    right_list.append(input.split('\n')[i].split(' ')[3])

right_dict = {}

for i in range(len(right_list)):
    if right_list[i] in right_dict:
        right_dict[right_list[i]] += 1
    else:
        right_dict[right_list[i]] = 1

output = 0

for i in range(len(left_list)):
    if left_list[i] in right_dict:
        output += int(left_list[i]) * right_dict[left_list[i]]

print(output)
