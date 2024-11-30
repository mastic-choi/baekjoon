import sys
input = sys.stdin.readline

# 체스판 패턴 생성
def create_chess_patterns():
    pattern1, pattern2 = [], []
    for i in range(8):
        if i % 2 == 0:
            pattern1.append("WBWBWBWB")
            pattern2.append("BWBWBWBW")
        else:
            pattern1.append("BWBWBWBW")
            pattern2.append("WBWBWBWB")
    return pattern1, pattern2

# 다시 칠해야 하는 개수를 계산
def count_mismatch(board, pattern, start_row, start_col):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern[i][j]:
                count += 1
    return count

# 메인 로직
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
pattern1, pattern2 = create_chess_patterns()

min_paint = float('inf')

# 8x8 보드 순회
for i in range(n - 7):
    for j in range(m - 7):
        # 두 패턴과 비교
        mismatch1 = count_mismatch(board, pattern1, i, j)
        mismatch2 = count_mismatch(board, pattern2, i, j)
        # 최소값 갱신
        min_paint = min(min_paint, mismatch1, mismatch2)

print(min_paint)
