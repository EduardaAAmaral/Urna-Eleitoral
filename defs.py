
def posicao(posy,posx):
  if posy > 307 and posy < 355 and posx > 508 and posx < 945:
    return(1)
  if posy > 307 and posy < 355 and posx > 969 and posx < 1029:
    return(2)
  if posy > 307 and posy < 355 and posx > 1052 and posx < 1117:
    return(3)
  if posy > 379 and posy < 427 and posx > 882 and posx < 943:
    return(4)
  if posy > 379 and posy < 427 and posx > 968 and posx < 1030:
    return(5)
  if posy > 379 and posy < 427 and posx > 1055 and posx < 1115:
    return(6)
  if posy > 450 and posy < 497 and posx > 883 and posx < 944:
    return(7)
  if posy > 450 and posy < 497 and posx > 969 and posx < 1030:
    return(8)
  if posy > 450 and posy < 497 and posx > 1053 and posx < 1115:
    return(9)
  if posy > 520 and posy < 566 and posx > 969 and posx < 1032:
    return(0)
  

#Para tirar nome e partido 
def informacoes(win, voto):
  arq = open("candidatos.txt", "r")
  linhas = arq.read()
  arq.close()
  tira = linhas.split("\n")

  candidatos = []
  for vet in tira:
    candidatos.append(vet.split(";"))

  for val in candidatos:
    if voto == val[2]:
      return (val[0], val[1], val[3], val[4])


#numero do candidato
def candidato():
  arq = open("candidatos.txt", "r")
  linhas = arq.read()
  arq.close()
  tira = linhas.split("\n")

  candidatos = []
  for vet in tira:
    candidatos.append(vet.split(";"))
  
  num_candidatos = []
  for val in candidatos:
    num_candidatos.append(val[2])

  return num_candidatos


# Apagar os votos
def fazer_pasta():
  arq = open("votos.txt", "w")
  for vet in candidato():
    arq.write(vet + ";" + "0"+"\n")
  arq.write("branco de deputado;"+"0"+"\n")
  arq.write("nulo de deputado;"+"0"+"\n")
  arq.write("branco de presidente;"+"0"+"\n")
  arq.write("nulo de presidente;"+"0"+"\n")
  arq.close()
  return 

  
# Salvar os votos
def votos(voto):
  arq = open("votos.txt", "r+")
  linhas = arq.read()
  tira = linhas.split("\n")
  arq.close()
  val = []
  for vet in tira:
    val.append(vet.split(";"))

  if voto == "encerrar":
    return linhas
 
  for i in range(len(val)):
    if voto == val[i][0]:
      teste = int(val[i][1])
      teste += 1
      troca = str(teste)
      val[i][1] = troca
      print(teste)

  arq =open("votos.txt","w")
  for i in range(len(val)-1):
    arq.write(val[i][0]+";"+val[i][1]+"\n")    

  
  
    
#soma de votos 
def conta():
  arq = open("votos.txt","r")
  linhas = arq.read()
  tira = linhas.split("\n")
  arq.close()
  val = []
  for vet in tira:
    val.append(vet.split(";"))
  votos = []
  for i in range(len(val)-1):
    votos.append(val[i][1])

  total_de_votos = 0
  for i in range(len(votos)):
    vet = int(votos[i])
    total_de_votos += vet

  teste=[]
  for i in range(len(votos)):
    val = int(votos[i])
    if val != 0:
      soma=float(val*100)/float(total_de_votos)
      dois = round(soma, 2)
      teste.append(str(dois))
    if val == 0:
      teste.append(str(val))
      
  return(total_de_votos, teste)
  
conta()
    
# porcentagem de votos
def encerrar():
  arq = open("votos.txt","r")
  linhas = arq.read()
  tira = linhas.split("\n")
  arq.close()
  val = []
  for vet in tira:
    val.append(vet.split(";"))

  hg = conta()
  
  arq = open("encerrar.txt","w")
  arq.write("Total de Votos -->"+ str(hg[0])+"\n")
  x = 0
  while x < len(val)-1:
    arq.write(val[x][0]+"-->"+hg[1][x]+"%"+"\n")
    x+= 1

  return

