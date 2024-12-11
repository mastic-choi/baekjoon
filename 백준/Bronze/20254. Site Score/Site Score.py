def function(Ur, Tr, UO, TO):
  return (56*Ur + 24*Tr+14*UO+6*TO)

def main():
  Ur, Tr, UO, TO = map(int, input().split())
  print(function(Ur, Tr, UO, TO))
main()