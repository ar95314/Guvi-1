n=int(input())
if(n==1):
  print('no')
elif(n==2):
  print('yes')
else:
  for x in range(2,n):
    if(n%x)==0:
      print('no')
      break
  else:
    print('yes')
