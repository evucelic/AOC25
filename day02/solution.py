input_file = "input.txt"

def parse_input(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    lines = [line.strip() for line in text.strip().split(",")]
    return lines


# part 1
invalid_sum = 0

for el in parse_input(input_file):
    start, end = el.split("-")
    for i in range(int(start), int(end)+1):
        s = str(i)
        if len(s) % 2 != 0:
            continue
        
        if s[:len(s)//2] == s[len(s)//2:]:
            invalid_sum += i

print(invalid_sum)


# part 2
invalid_sum_pt2 = 0

for el in parse_input(input_file):
    start, end = el.split("-")
    for i in range(int(start), int(end)+1):
        s = str(i)
        for j in range(1, len(s)//2 + 1):
            temp_set = set([s[k:k+j] for k in range(0, len(s), j)])
            if len(temp_set) == 1:
                invalid_sum_pt2 += i
                break


print(invalid_sum_pt2)
