def is_available(candidate,current_col): # 수직체크 대각선 체크
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    
    return True



def DFS(N,current_row,current_candidate,final_result):
    if current_row ==N: # N개 배치가 다 끝났다.
        final_result.append(current_candidate[:]) # 얇은 복사
        return
    
    for candidate_col in range(N):
        if is_available(current_candidate,candidate_col):
            current_candidate.append(candidate_col)
            DFS(N,current_row+1,current_candidate,final_result)
            current_candidate.pop() # 백트래킹


def solve_n_queens(N):
    final_result= []
    DFS(N,0,[],final_result)
    return final_result


print(solve_n_queens(4))