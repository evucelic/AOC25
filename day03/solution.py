input_file = "input.txt"


def parse_input(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    lines = [line.strip() for line in text.strip().split("\n")]
    return lines



# part 1
p1_sum = 0

for line in parse_input(input_file):
    num_arr = [int(i) for i in line]
    left = max(num_arr[:-1])
    right = max(num_arr[num_arr.index(left)+1:])
    p1_sum += 10 * left + right

print(p1_sum)


# part 2
p2_sum = 0

def argmax(a):
    return max(range(len(a)), key=lambda x: a[x])

for line in parse_input(input_file):
    num_arr = [int(i) for i in line]
    final = []
    idxs = []
    for j in range(11, -1, -1):
        if not final:
            idx = argmax(num_arr[:-j])
            final.append(num_arr[idx])
            idxs.append(idx)
        else:
            last_index = idxs[-1]
            if j == 0:
                window = num_arr[last_index + 1:]
            else:
                window = num_arr[last_index + 1:-j]

            idx = argmax(window)
            global_idx = last_index + 1 + idx
            final.append(num_arr[global_idx])
            idxs.append(global_idx)

    p2_sum += int(''.join(map(str, final)))

print(p2_sum)