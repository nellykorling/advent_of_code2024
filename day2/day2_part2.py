with open('input.txt', 'r') as file:
    input = file.read()

lines = []
line = []
for l in input.split('\n'):
    lines.append(l.split(' '))

def test_increase(list):
    for i in range(len(list) - 1):
        bad_count = 0
        diff = int(list[i+1]) - int(list[i])
        if diff < 1 or diff > 3:
            bad_count += 1
    if bad_count > 1:
        return False
    return True

def test_decrease(list):
    for i in range(len(list) - 1):
        bad_count = 0
        diff = int(list[i]) - int(list[i+1])
        if diff < 1 or diff > 3:
            bad_count += 1
    if bad_count > 1:
        return False
    return True

counter = 0
for list in lines:
    if test_increase(list) or test_decrease(list):
        counter += 1
        
print(counter)