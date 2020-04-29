MAZE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

MAZEO = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
         [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maze_width = 10
maze_height = 8

i = 1
j = 1
forward = 1
road = [[i, j, forward]]


def push():
    global forward, i, j
    road.append([i, j, forward])


def pop():
    global forward, i, j
    i, j, forward = road.pop()
    return i, j, forward


def main():
    global forward, i, j, road

    while [i, j] != [maze_height, maze_width]:
        if forward == 1:
            if MAZE[i][j + 1] == 0:
                push()
                i = i
                j = j + 1
                forward = 4

            elif MAZE[i + 1][j] == 0:
                push()
                i = i + 1
                j = j
                forward = 1

            elif MAZE[i][j - 1] == 0:
                push()
                i = i
                j = j - 1
                forward = 2

            else:
                MAZE[i][j] = 1
                i, j, forward = pop()

        elif forward == 2:
            if MAZE[i + 1][j] == 0:
                push()
                i = i + 1
                j = j
                forward = 1

            elif MAZE[i][j - 1] == 0:
                push()
                i = i
                j = j - 1
                forward = 2

            elif MAZE[i - 1][j] == 0:
                push()
                i = i - 1
                j = j
                forward = 3

            else:
                MAZE[i][j] = 1
                i, j, forward = pop()

        elif forward == 3:
            if MAZE[i][j - 1] == 0:
                push()
                i = i
                j = j - 1
                forward = 2

            elif MAZE[i - 1][j] == 0:
                push()
                i = i - 1
                j = j
                forward = 3

            elif MAZE[i][j + 1] == 0:
                push()
                i = i
                j = j + 1
                forward = 4

            else:
                MAZE[i][j] = 1
                i, j, forward = pop()
        else:
            if MAZE[i - 1][j] == 0:
                push()
                i = i - 1
                j = j
                forward = 3

            elif MAZE[i][j + 1] == 0:
                push()
                i = i
                j = j + 1
                forward = 4

            elif MAZE[i + 1][j] == 0:
                push()
                i = i + 1
                j = j
                forward = 1

            else:
                MAZE[i][j] = 1

                # i, j, forward = pop()
                i, j, forward = pop()

                if [i, j] == [1, 1]:
                    print("dead maze!")
                    break

    push()

    for [x, y, d] in road:
        MAZEO[x][y] = '*'

    # print(road)
    for m in range(10):
        for n in range(12):
            print(MAZEO[m][n], end='')
        print()


if __name__ == '__main__':
    main()
# branch is branch, merge is merge . they are different.

