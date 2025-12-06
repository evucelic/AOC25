input_file = "input.txt"


def parse_input(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    lines = [line.strip() for line in text.strip().split("\n\n")]
    ranges, ingredients = lines[0], lines[1]
    ranges_lines = ranges.split("\n")
    ingredients_lines = ingredients.split("\n")
    return ranges_lines, ingredients_lines


r, i = parse_input(input_file)

# part 1
p1_sum = 0

for el in i:
    num = int(el)
    for line in r:
        left, right = line.split("-")
        if num >= int(left) and num <= int(right):
            p1_sum +=1
            break

print(p1_sum)


# part 2
p2_sum = 0

intervals = []
for line in r:
    left, right = map(int, line.split("-"))
    intervals.append((left, right))

intervals.sort(key=lambda x: x[0])

no_overlap = []

first, last = intervals[0]

for next_first, next_last in intervals[1:]:
    if next_first <= last + 1:
        last = max(last, next_last)
    else:
        no_overlap.append((first, last))
        first, last = next_first, next_last

no_overlap.append((first, last))

for el in no_overlap:
    p2_sum += el[1] - el[0] + 1

print(p2_sum)