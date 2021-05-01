'''
functions
'''
def parser(a):
  b=['']
  c=0
  for x in a:
    if x.isdigit() or x=='.':
      b[c]+=x
    else:
      b.append('')
      c+=1
      b[c]+=x
      b.append('')
      c+=1
  return b

def sf(x): #significant figures
  if x=='':
    return 0
  c=0
  key=0
  for i in x:
    if (1-key) and i!='0' and i!='.':
      c+=1
      key=1
    elif key and i.isdigit():
      c+=1   
  return c

def dn(x): #decimal numbers
  c=''
  key=0
  for i in x:
    if i=='.':
      key=1
    elif key and i.isdigit():
      c+=i   
  return c

def wn(x): #whole numbers
  c=''
  key=0
  for i in x:
    if i=='.':
      break
    elif key==0 and i!='0':
      c+=i
      key=1
    elif key:
      c+=i
  return c

def dfa(x,n): #decimal figures aprox.
  k=''
  w=wn(x)
  d=dn(x)
  if n==0:
    if len(d)>0:
      if int(d[0])>5 or (int(d[0])==5 and int(w[-1])%2!=0):
        w=str(int(w)+1)
    return w
  for i in range(1,n+1):
    k+='0'
  a=w+'.'
  decimal=d+k
  for i in range(0,n):
    a+=decimal[i]
  if int(decimal[n])>5 or (int(decimal[n])==5 and int(decimal[n-1])%2!=0):
    a=str(float(a)+10**(-n))
  return a

def sfa(x,n): #significant figures aprox.
  k=''
  w=wn(x)
  d=dn(x)
  for i in range(1,n+1):
    k+='0'
  a=w+'.'+d+k
  r=''
  c=0
  if n<len(w) or n==len(w):
    w=dfa(a,0)
    return w
  r=w+'.'
  for i in (d+k):
    r+=i
    c+=1
    if c==n-len(w):
      break
  return r

def operation(a,op,b):
  mindn=min(len(dn(a)),len(dn(b)))
  minsf=min(sf(a),sf(b))
  if op=='+':
    r=float(a)+float(b)
    r=dfa(str(r),mindn)
  elif op=='-':
    r=float(a)-float(b)
    r=dfa(str(r),mindn)
  elif op=='/':
    r=float(a)/float(b)
    r=sfa(str(r),minsf)
  elif op=='*':
    r=float(a)*float(b)
    r=sfa(str(r),minsf)
  else:
    print("Error")
  return r
  
def op(x): #operations' priority
  c=0
  d=[]
  for i in x:
    if c%2==1:
      if i=='*' or i=='/':
        d.append(c)
    c+=1
  c=0 
  for i in x:
    if c%2==1:
      if i=='+' or i=='-':
        d.append(c)
    c+=1
  return d

def calc(u):
  u=parser(u)
  while len(u)>=3:
    o=op(u)
    i=o[0]
    r=operation(u[i-1],u[i],u[i+1])
    u[i]=r
    u.pop(i-1)
    u.pop(i)
  return u[0]

def calculator():
  u=input()
  print(calc(u))