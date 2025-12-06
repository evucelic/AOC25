input_file = "input.txt"


def parse_input(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    lines = [line.strip() for line in text.strip().split("\n")]
    grid = [[c for c in line] for line in lines]
    return grid


grid = parse_input(input_file)
rows = len(grid)
cols = len(grid[0])

# part 1 
p1_sum = 0

directions = [(-1,0), # up
              (1,0), # down
              (0, 1), # right
              (0, -1), # left
              (-1,-1), # up left
              (-1, 1), # up right
              (1,1), # down right
              (1, -1) # down left
              ]


for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            continue
        around = []
        for dr, dc in directions:
            ni, nj = i + dr, j + dc
            if 0 <= ni < rows and 0 <= nj < cols:
                around.append(grid[ni][nj])
        
        if around.count("@") < 4:
            p1_sum += 1

print(p1_sum)
        


# part 2
p2_sum = 0

while True :
    to_remove = []
    changed = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                continue
            around = []
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols:
                    around.append(grid[ni][nj])
            
            if around.count("@") < 4:
                changed += 1
                to_remove.append((i,j))
    
    p2_sum += changed
    if changed == 0:
        break

    for ri, rj in to_remove:
        grid[ri][rj] = "."

print(p2_sum)