l=6
i=[]
arq = open()
for b in range(l):
    s=input('Insira sua senha: ')
    if s.lower()==s:
      i=i+['Senha invalida']
    elif s.upper()==s:
      i=i+['Senha invalida']
    elif (6<=len(s)<=32) is False:
      i=i+['Senha invalida']
    else:
      c=[]
      for x in s:
        o=ord(x)
        if 48<=o<=57:
          c=c+[x]
        elif 65<=o<=90:
          c=c+[x]
        elif 97<=o<=122:
          c=c+[x]
if ''.join(c)==s:
	i=i+['Senha valida']
else:
	i=i+['Senha invalida']
for j in i:
	print(j)