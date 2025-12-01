input_file = "input.txt"

def parse_input(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    lines = [line.strip() for line in text.strip().split("\n")]
    return lines

password_pt1 = 0
lock = 50

# part 1
for line in parse_input(input_file):
    instruction = line[0]
    move = int(line[1:])
    if instruction == "R":
        lock += move
    if instruction == "L":
        lock -= move
    
    lock = lock % 100
    if lock == 0:
        password_pt1 +=1

print(password_pt1)

# part 2

password_pt2 = 0
lock = 50

for line in parse_input(input_file):
    instruction = line[0]
    move = int(line[1:])

    start = lock
    if instruction == "R":
        lock += move

    if instruction == "L":
        lock -= move


    if lock > 0:
        password_pt2 += lock // 100
    
    elif lock < 0:
        password_pt2 += abs(lock) // 100
        if start > 0:
            password_pt2 += 1

    elif lock == 0:
        password_pt2 += 1
    
    lock = lock % 100
    

print(password_pt2)

