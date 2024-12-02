import sys


def solution(school):
  if school == "NLCS":
    return "North London Collegiate School"
  elif school == "BHA":
    return "Branksome Hall Asia"
  elif school == "KIS":
    return "Korea International School"
  elif school == "SJA":
    return "St. Johnsbury Academy"


school = sys.stdin.readline().strip()
print(solution(school))
