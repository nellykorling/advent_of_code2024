with open('input.txt', 'r') as file:
    input = file.read()

lines = []
line = []
for l in input.split('\n'):
    lines.append(l.split(' '))

def test_sequence(list):
    if test_increase(list) or test_decrease(list):
        return True
        
    for i in range(len(list)):
        modified_list = list[:i] + list[i+1:]
        if test_increase(modified_list) or test_decrease(modified_list):
            return True
            
    return False

def test_increase(list):
    for i in range(len(list) - 1):
        diff = int(list[i+1]) - int(list[i])
        if diff < 1 or diff > 3:
            return False
    return True

def test_decrease(list):
    for i in range(len(list) - 1):
        diff = int(list[i]) - int(list[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

counter = 0
for list in lines:
    if test_sequence(list):
        counter += 1
        
print(counter)