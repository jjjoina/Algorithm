def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    
    ans = 0
    
    while True:
        remove_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove_set.add((i, j))
                    remove_set.add((i, j+1))
                    remove_set.add((i+1, j))
                    remove_set.add((i+1, j+1))
                    
        if len(remove_set) == 0:
            break
        ans += len(remove_set)
        for i, j in remove_set:
            board[i][j] = 0
        
        for j in range(n):
            stack = []
            for i in range(m):
                if board[i][j] != 0:
                    stack.append(board[i][j])
            for i in range(m-1, -1, -1):
                if stack:
                    board[i][j] = stack.pop()
                else:
                    board[i][j] = 0
    
    return ans