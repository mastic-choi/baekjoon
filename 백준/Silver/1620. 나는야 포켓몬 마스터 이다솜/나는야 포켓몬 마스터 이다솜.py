#백준 1620 / 나는야 포켓몬 마스터 이다솜
import sys


#N : 포켓몬의 총 수 / M : 문제의 개수
N, M = map(int, sys.stdin.readline().split())
#문제가 숫자일 경우 : 해당 번호의 포켓몬 이름 출력 / 문제가 영어 이름일 경우 : 해당 이름의 포켓몬 번호를 출력
pkmn = {}
#포켓몬 도감 만들기
for i in range(1, N + 1):
  name = sys.stdin.readline().strip()
  pkmn[name] = i
reverse_dict = {value: key for key, value in pkmn.items()}
for _ in range(M):
  problem = sys.stdin.readline().strip()
  if problem.isnumeric():
    print(reverse_dict[int(problem)])
  else :
    print(pkmn[problem])