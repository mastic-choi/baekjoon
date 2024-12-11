while 1:
  x, y = input().split()
  h1, m1 = map(int, x.split(':'))
  h2, m2 = map(int, y.split(':'))
  if h1 == m1 == h2 == m2 == 0: # 00:00 00:00의 입력을 받으면 break
    break
  t = h1*60+m1 + h2*60+m2
  n = t//60//24
  h = t//60 % 24
  m = t%60
  if n > 0:
    print("%02d:%02d +%d" % (h,m,n))
  else:
    print("%02d:%02d" % (h,m))