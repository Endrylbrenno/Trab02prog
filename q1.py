def espaco(lista, total):
   m = 0
   tamanho = len(lista)
   m = (total)/(tamanho+1)  
   return m
def convertor(Bytes):
   Bytes = float(Bytes)
   return (float(Bytes/(1024*1024)))
def percent(lista, tt):
   percentual = (lista[3]/tt)*100
   lista.insert((len(usuario)),percentual)
user = []
p = 1
total = m = 0
with open ("usuarios.txt","r") as arquivo:
   valor = 0
   for linha in arquivo:
      user.append(linha.split()) 
   for usuario in user:
      usuario.insert(0,p)
      valor = convertor(float(usuario[2]))
      total += valor
      usuario.insert((len(user)),valor)
      p+=1
   for usuario in user:
      percent(usuario, total)
m = espaco(usuario,total)
with open ("relatorio.txt","w") as arquivo:
   arquivo.write("ACME Inc.               uso do espaço em disco pelos usuarios\n--------------------------------------------------------------\nNr\tusuário\tespaco utilizado\t% do uso\n\n")
   for usuario in user:
      percentagem="{0:.2f}".format(round(usuario[3],2))
      arquivo.write(str(usuario[0])+'\t{:<15}'.format(usuario[1])+'\t{:<16}'.format(percentagem)+'MB\t{0:.2f}'.format(usuario[4])+'%\n')

   arquivo.write('\n\nEspaço Total Ocupado: {0:.2f}'.format(total) + ' MB')
   arquivo.write('\n\nEspaço médio Ocupado: {0:.2f}'.format(m) + ' MB')
   arquivo.close()

