def solution(commands):
    def find(r, c):
        if parent[r][c] != [r, c]:
            parent[r][c] = find(parent[r][c][0], parent[r][c][1])

        return parent[r][c]


    def union(r1, c1, r2, c2):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)

        if [r1, c1] == [r2, c2]:
            return

        if arr[r2][c2] != None:
            if arr[r1][c1] == None:
                arr[r1][c1] = arr[r2][c2]
            arr[r2][c2] = None

        parent[r2][c2] = [r1, c1]


    def update1(r, c, value):
        r, c = find(r, c)
        arr[r][c] = value


    def update2(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                r, c = find(i, j)
                if arr[r][c] == value1:
                    arr[r][c] = value2


    def merge(r1, c1, r2, c2):
        union(r1, c1, r2, c2)


    def unmerge(r, c):
        pr, pc = find(r, c)

        temp = []

        for i in range(1, 51):
            for j in range(1, 51):
                if find(i, j) == [pr, pc]:
                    temp.append([i, j])

        for i, j in temp:
            parent[i][j] = [i, j]

        if [r, c] != [pr, pc]:
            arr[r][c] = arr[pr][pc]
            arr[pr][pc] = None


    def my_print(r, c):
        r, c = find(r, c)
        answer.append(arr[r][c] if arr[r][c] != None else "EMPTY")


    arr = [[None] * 51 for _ in range(51)]
    parent = [[[r, c] for c in range(51)] for r in range(51)]
    answer = []

    for command in commands:
        command = command.split()

        if command[0] == "UPDATE":
            if len(command) == 4:
                update1(int(command[1]), int(command[2]), command[3])
            else:
                update2(command[1], command[2])
        elif command[0] == "MERGE":
            merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "UNMERGE":
            unmerge(int(command[1]), int(command[2]))
        else:
            my_print(int(command[1]), int(command[2]))

    return answer