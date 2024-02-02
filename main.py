import graphics as gf
import defs as df
from time import sleep
import pygame  
pygame.mixer.init() 
pygame.mixer.music.load("audio_urna.mp3") 
pygame.mixer.music.set_volume(100) 


'''
#Para zera o arquivo dos votos
teste=df.fazer_pasta()
print(teste)
'''


#Janela com a urna
win = gf.GraphWin("Urna", 1240, 720)
img = gf.Image(gf.Point(640, 360), "urna.png")
img.draw(win)


#Botão para encerrar votação
botao = ['','']
botao[0] = gf.Rectangle(gf.Point(604,564),gf.Point(755,606))
botao[0].setWidth(2)
botao[1] = gf.Text(gf.Point(677,586)," Encerrar Votação")
botao[1].setSize(10)


# Tela com a mensagem inicial da urna
tela_inicial = ['','','','']
tela_inicial[0] = gf.Text(gf.Point(423, 341), "PARA COMEÇAR A VOTAÇÃO")
tela_inicial[1] = gf.Text(gf.Point(350, 381), "APERTE NO")
tela_inicial[2] = gf.Rectangle(gf.Point(436, 364), gf.Point(564, 397))
tela_inicial[3] = gf.Text(gf.Point(499, 380), "CONFIRMA")
tela_inicial[0].setSize(20)
tela_inicial[0].draw(win)
tela_inicial[1].setSize(15)
tela_inicial[1].draw(win)
tela_inicial[2].setFill("green")
tela_inicial[2].draw(win)
tela_inicial[3].draw(win)
botao[0].draw(win)
botao[1].draw(win)


#Tela para votação
quad = ['','','','','','','']
quad[0] = gf.Rectangle(gf.Point(231, 323), gf.Point(283, 385))
quad[1] = gf.Rectangle(gf.Point(301, 323), gf.Point(355, 385))
quad[2] = gf.Text(gf.Point(348, 282), "Deputado Federal")
quad[2].setSize(20)
quad[3] = gf.Text(gf.Point(165, 239), "SEU VOTO PARA")
quad[4] = gf.Text(gf.Point(300, 282), "Presidente")
quad[4].setSize(20)
quad[5] = "Deputado Federal"
quad[6] = "Presidente"


#Informações da tela de votação
informa = ['','','','','','','']
informa[0] = gf.Text(gf.Point(155, 358), "Número:")
informa[0].setSize(18)
informa[1] = gf.Text(gf.Point(140, 464), "Nome:")
informa[1].setSize(18)
informa[2] = gf.Text(gf.Point(145, 510), "Partido:")
informa[2].setSize(18)
informa[3] = gf.Line(gf.Point(99, 556), gf.Point(773, 556))
informa[4] = gf.Text(gf.Point(155, 571), "Aperte a tecla:")
informa[5] = gf.Text(gf.Point(400, 588), "CONFIRMA para CONFIRMAR este voto")
informa[6] = gf.Text(gf.Point(400, 605), "CORRIGE para REINICIAR este voto")


#barra de carregamento
barra = ['','','','','']
barra[0] = gf.Rectangle(gf.Point(206,365),gf.Point(635,396))
barra[1] = gf.Rectangle(gf.Point(210,369),gf.Point(236,387))
barra[1].setFill("green")
barra[1].setOutline("green")
barra[2] = gf.Text(gf.Point(413,411),"Gravando...")
barra[2].setSize(15)
barra[3] = gf.Text(gf.Point(411,384),"FIM")
barra[3].setSize(36)
barra[4] =gf.Rectangle(gf.Point(210,362),gf.Point(630,394))
barra[4].setFill("#e7e7e7")
barra[4].setOutline("#e7e7e7")

#Candidatos para quando os dois votos forem brancos
voto = 1
info=[1,2]
val =['','','']
val[0] = gf.Text(gf.Point(667, 360),"vazio" )
val[1] = gf.Text(gf.Point(285, 465), info[1])
val[1].setSize(18)
val[2] = gf.Text(gf.Point(249, 510), info[0])
val[2].setSize(18)

#senha
senha=['','','','','']
senha[0] = gf.Text(gf.Point(260, 300), "Senha:")
senha[0].setSize(15)
for i in range(1,5):
  senha[i] = gf.Rectangle(gf.Point(161+70*i, 323), gf.Point(211+72*i, 385))
        

senha_da_urna ='1234'
senha_teste = ''


voto = ''
primeiro = gf.Text(gf.Point(259, 355),voto)
primeiro.draw(win)
num_valido = df.candidato()

teste = 0
encerrar = 0
confirma = 0 # Para os números nao funcionarem
certo = 0 # Para saber quando é deputado ou presidente
branco = 0
nulo = 0 # Para saber quando o voto é nulo
cont = 0 #Para saber quando o branco é do deputado ou presidente
val = 0 # Para seber se nulo é deputado ou presidente 
termina = False
while True:
  clique = win.getMouse()
  posy = clique.getY()
  posx = clique.getX()
  print("X ->", posx)
  print("Y ->", posy)
  print("-------------")
  if posy > 565 and posy < 606 and posx > 605 and posx < 755 and confirma == 0 :
    print("encerrar")
    print("teste",teste)
    print("encerrar",encerrar)
    termina = True

    
    if encerrar == 0 and teste == 0:
      for i in range(len(tela_inicial)):
        tela_inicial[i].undraw()
      if encerrar == 2:
        barra[3].undraw()
      for i in range(5):
        senha[i].draw(win)
    if encerrar == 2 and teste == 0:
      for i in range(len(tela_inicial)):
        tela_inicial[i].undraw()
      if encerrar == 2:
        barra[3].undraw()
      for i in range(5):
        senha[i].draw(win)
    if encerrar == 2 and teste == 2:
      for i in range(len(tela_inicial)):
        tela_inicial[i].undraw()
      if encerrar == 2:
        barra[3].undraw()
      for i in range(5):
        senha[i].draw(win)
    x = 0
    while x < 4:
      clique = win.getMouse()
      posy = clique.getY()
      posx = clique.getX()
      num = df.posicao(posy,posx)
      senha_teste += f"{num}"
      senha1 = gf.Text(gf.Point(259+70*x, 360), "*")
      senha1.setSize(35)
      senha1.draw(win)
      x+= 1
    
    if senha_teste != senha_da_urna:# Senha errada
      errada = gf.Text(gf.Point(413,435),"Senha Errada!!")
      errada.setSize(20)
      errada.draw(win)
      click = gf.Text(gf.Point(440,472),"Click em encerrar votação, para tentar novamente.")
      click.setSize(15)
      click.draw(win)
      sleep(0.5)
      for i in range(1,5):
        senha[i].undraw()
      apaga2 =gf.Rectangle(gf.Point(223,310),gf.Point(504,394))
      apaga2.setFill("#e7e7e7")
      apaga2.setOutline("#e7e7e7")
      apaga2.draw(win)
      for i in range(1,5):
        senha[i].draw(win)
      senha_teste=''
      teste = 1
      sleep(0.8)
      errada.undraw()
      click.undraw()
    
      
      
    if senha_da_urna == senha_teste: # Se a senha estiver corrita
      sleep(0.5)
      apaga = gf.Rectangle(gf.Point(221,284),gf.Point(524,392))
      apaga.setFill("#e7e7e7")
      apaga.setOutline("#e7e7e7")
      apaga.draw(win)
      barra[0].draw(win)
      barra[2].draw(win)
      botao[0].undraw()
      botao[1].undraw()
      for i in range(395):
        barra[1] = gf.Rectangle(gf.Point(210,369),gf.Point(236+i,394))
        barra[1].setFill("green")
        barra[1].setOutline("green")
        barra[1].draw(win)
      sleep(1)
      for i in range(3):
        barra[i].undraw()
      apaga2 =gf.Rectangle(gf.Point(210,362),gf.Point(630,394))
      apaga2.setFill("#e7e7e7")
      apaga2.setOutline("#e7e7e7")
      apaga2.draw(win)
      quadrado =gf.Rectangle(gf.Point(238,322),gf.Point(561,402))
      quadrado.setWidth(2)
      quadrado.draw(win)
      mensagem =gf.Text(gf.Point(398,350),"Votos Gravados...")
      mensagem.setSize(20)
      mensagem.draw(win)
      mensagem2 =gf.Text(gf.Point(403,382),"Votação Encerrada")
      mensagem2.setSize(20)
      mensagem2.draw(win)
      voto = "encerrar"
    val = df.votos(voto)
    df.encerrar() 
    #print(val)
    #print(senha_teste)    
    #print(teste)
  if termina == False:     
    if posy > 307 and posy < 355 and posx > 508 and posx < 945 and len(voto) < 2 and confirma == 1:
      print("1")
      voto += "1"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
        
    if posy > 307 and posy < 355 and posx > 969 and posx < 1029 and len(voto) < 2 and confirma == 1:
      voto += "2"
      print("2")
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 307 and posy < 355 and posx > 1052 and posx < 1117 and len(voto) < 2 and confirma == 1:
      print("3")
      voto += "3"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 379 and posy < 427 and posx > 882 and posx < 943 and len(voto) < 2 and confirma == 1:
      print("4")
      voto += "4"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)  

    if posy > 379 and posy < 427 and posx > 968 and posx < 1030 and len(voto) < 2 and confirma == 1:
      print("5")
      voto += "5"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 379 and posy < 427 and posx > 1055 and posx < 1115 and len(voto) < 2 and confirma == 1:
      print("6")
      voto += "6"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 450 and posy < 497 and posx > 883 and posx < 944 and len(voto) < 2 and confirma == 1:
      print("7")
      voto += "7"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 450 and posy < 497 and posx > 969 and posx < 1030 and len(voto) < 2 and confirma == 1:
      print("8")
      voto += "8"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 450 and posy < 497 and posx > 1053 and posx < 1115 and len(voto) < 2 and confirma == 1:
      print("9")
      voto += "9"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)
      
    if posy > 520 and posy < 566 and posx > 969 and posx < 1032 and len(voto) < 2 and confirma == 1:
      print("0")
      voto += "0"
      primeiro.undraw()
      primeiro = gf.Text(gf.Point(259, 355), f"{voto[0]}")
      primeiro.setSize(35)
      primeiro.draw(win)
      if len(voto) == 2:
        segundo = gf.Text(gf.Point(329, 355), f"{voto[1]}")
        segundo.setSize(35)
        segundo.draw(win)
      print(voto)  
    
    if len(voto) == 2 and certo == 0:
      info = df.informacoes(win,voto)
      if voto in num_valido:# voto validos
        if quad[5] == info[0]:
          val =['','','']
          val[0] = gf.Image(gf.Point(667, 360), f"{info[3]}")
          val[0].draw(win)
          val[1] = gf.Text(gf.Point(285, 465), info[1])
          val[1].setSize(18)
          val[1].draw(win)
          val[2] = gf.Text(gf.Point(249, 510), info[2])
          val[2].setSize(18)
          val[2].draw(win)
          for i in range(len(informa)):
            informa[i].draw(win)
        
        if quad[6] == info[0]:
          val =['','','']
          val[0] = gf.Image(gf.Point(667, 360), f"{info[3]}")
          val[0].draw(win)
          val[1] = gf.Text(gf.Point(285, 465), info[1])
          val[1].setSize(18)
          val[1].draw(win)
          val[2] = gf.Text(gf.Point(249, 510), info[2])
          val[2].setSize(18)
          val[2].draw(win)
          for i in range(len(informa)):
            informa[i].draw(win) 
        
        certo = 1
      if voto not in num_valido:# voto nulo
        num_errado = gf.Text(gf.Point(222, 405), "NÚMERO ERRADO")
        num_errado.setSize(20)
        num_nulo = gf.Text(gf.Point(420, 490), "VOTO NULO")
        num_nulo.setSize(30)           
        num_nulo.draw(win)
        num_errado.draw(win)
        informa[0].draw(win)
        for i in range(3,7):
            informa[i].draw(win)
        voto = ''
        nulo = 1
      
    if posy > 587 and posy < 636 and posx > 841 and posx < 930 and confirma == 1:
      
      print("Branco")
      print("branco -->",branco)
      if len(voto) == 0 and cont == 0: # branco no deputado
        for i in range(len(quad)-3):
          quad[i].undraw()
        quad[3].draw(win)
        branco1 = gf.Text(gf.Point(417, 354), "VOTO EM BRANCO")
        branco1.setSize(30)
        branco1.draw(win)
        for i in range(3,7):
          informa[i].draw(win)
        branco += 1
        teste = 1
      if branco == 0 or branco == 1 and cont == 1 : # branco no presidente
        for i in range(len(quad)-3):
          quad[i].undraw()
        quad[4].undraw()
        quad[3].draw(win)
        branco1 = gf.Text(gf.Point(417, 354), "VOTO EM BRANCO")
        branco1.setSize(30)
        branco1.draw(win)
        for i in range(3,7):
          informa[i].draw(win)
        teste += 1 
        branco = 2
    if posy > 587 and posy < 636 and posx > 953 and posx < 1042 and confirma == 1:
      print("corrige")
      primeiro.undraw()
      if len(voto) == 1:
        voto = ''
      if len(voto) == 2 and nulo == 0:
        segundo.undraw()
        voto = ''
        if quad[5] == info[0]:
          val[0].undraw()
          val[1].undraw()
          val[2].undraw()
          for i in range(len(informa)):
            informa[i].undraw()
          certo = 0
          cont = 5
      if branco != 0 and cont == 0: # branco no deputado
        branco1.undraw()
        for i in range(3,7):
          informa[i].undraw()
        quad[0].draw(win)
        quad[1].draw(win)
        quad[2].draw(win)
      if cont == 1 and nulo != 1: # branco no presidente
        branco1.undraw()
        for i in range(3,7):
          informa[i].undraw()
        quad[0].draw(win)
        quad[1].draw(win)
        quad[4].draw(win)

      if nulo == 1: # nulo 
        segundo.undraw()
        informa[0].undraw()
        for i in range(3,7):
          informa[i].undraw()
        apaga=gf.Rectangle(gf.Point(100,389),gf.Point(550,507))
        apaga.setFill("#e7e7e7")
        apaga.setOutline("#e7e7e7")
        apaga.draw(win)
        
      
    if posy > 582 and posy < 636 and posx > 1067 and posx < 1155 and encerrar == 0:
      print("Confirma")
      if confirma == 0:
        for i in range(len(tela_inicial)):#para tira a tela inicial
          tela_inicial[i].undraw()
        botao[0].undraw()
        botao[1].undraw()
        for i in range(len(quad)-3):# para começar a tela de votação
          quad[i].draw(win)
        confirma = 1
      print("branco-->",branco)
      print("certo-->",certo)
      print("confirma-->",confirma)
      print("teste-->",teste)
      print("nulo-->",nulo)
      print("val-->",val)
      if branco == 1 and certo == 0 and teste == 1 and nulo == 0: # voto branco no deputado 
        desenha = gf.Rectangle(gf.Point(223,322),gf.Point(601,377))
        desenha.setFill("#e7e7e7")
        desenha.setOutline("#e7e7e7")
        desenha.draw(win)
        for i in range(3,7):
          informa[i].undraw()
        quad[0].draw(win)
        quad[1].draw(win)
        quad[4].draw(win)
        df.votos("branco de deputado")
        certo = 0
        cont = 1

      if branco == 2 and certo == 0 and teste != 2: # voto branco no presidente
        branco1.undraw()
        for i in range(3,7):
          informa[i].undraw()
        for i in range(3):
            val[i].undraw()
        for i in range(len(informa)):
          informa[i].undraw()
        for i in range(5):
          quad[i].undraw()
        df.votos("branco de presidente")
        barra[0].draw(win)
        barra[2].draw(win)
        for i in range(395):
          barra[1] = gf.Rectangle(gf.Point(210,369),gf.Point(236+i,394))
          barra[1].setFill("green")
          barra[1].setOutline("green")
          barra[1].draw(win)
        sleep(1)
        pygame.mixer.music.play() 
        for i in range(3):
          barra[i].undraw()
        barra[4].draw(win)
        barra[3].draw(win)
        botao[0].draw(win)
        botao[1].draw(win)
        certo = 0
        confirma = 0
        encerrar = 2
        
      if teste == 2:
        
        desenha = gf.Rectangle(gf.Point(223,322),gf.Point(601,377))
        desenha.setFill("#e7e7e7")
        desenha.setOutline("#e7e7e7")
        desenha.draw(win)
        for i in range(3,7):
          informa[i].undraw()
        
        for i in range(len(informa)):
          informa[i].undraw()
        for i in range(5):
          quad[i].undraw()
        df.votos("branco de presidente")
        barra[0].draw(win)
        barra[2].draw(win)
        for i in range(395):
          barra[1] = gf.Rectangle(gf.Point(210,369),gf.Point(236+i,394))
          barra[1].setFill("green")
          barra[1].setOutline("green")
          barra[1].draw(win)
        sleep(1)
        pygame.mixer.music.play() 
        for i in range(3):
          barra[i].undraw()
        barra[4].draw(win)
        barra[3].draw(win)
        botao[0].draw(win)
        botao[1].draw(win)
        certo = 0
        confirma = 0
        encerrar = 2

      if nulo == 1  and certo == 0:
        if val == 0:# nulo no deputado
          primeiro.undraw()
          segundo.undraw()
          quad[2].undraw()
          quad[4].draw(win)
          informa[0].undraw()
          for i in range(3,7):
            informa[i].undraw()
          apaga=gf.Rectangle(gf.Point(100,389),gf.Point(550,507))
          apaga.setFill("#e7e7e7")
          apaga.setOutline("#e7e7e7")
          apaga.draw(win)
          df.votos("nulo de deputado")
        if val != 0: # nulo no presidente
          primeiro.undraw()
          segundo.undraw()
          quad[0].undraw()
          quad[1].undraw()
          quad[4].undraw()
          quad[3].undraw()
          informa[0].undraw()
          for i in range(3,7):
            informa[i].undraw()
          apaga=gf.Rectangle(gf.Point(100,389),gf.Point(550,507))
          apaga.setFill("#e7e7e7")
          apaga.setOutline("#e7e7e7")
          apaga.draw(win)
          barra[0].draw(win)
          barra[2].draw(win)
          for i in range(395):
            barra[1] = gf.Rectangle(gf.Point(210,369),gf.Point(236+i,394))
            barra[1].setFill("green")
            barra[1].setOutline("green")
            barra[1].draw(win)
          sleep(1)
          pygame.mixer.music.play() 
          for i in range(3):
            barra[i].undraw()
          barra[4].draw(win)
          barra[3].draw(win)
          botao[0].draw(win)
          botao[1].draw(win)
          df.votos("nulo de presidente")
          confirma = 0
          encerrar = 2
        val = 1
      
        
      if len(voto) == 2: #voto valido
        if quad[5] == info[0]:
          primeiro.undraw()
          segundo.undraw()
          val[0].undraw()
          val[1].undraw()
          val[2].undraw()
          for i in range(len(informa)):
            informa[i].undraw()
          quad[2].undraw()
          quad[4].draw(win)
          df.votos(voto)
          voto = ''
          certo = 0
          cont = 1
        if quad[6] == info[0]:
          primeiro.undraw()
          segundo.undraw()
          df.votos(voto)
          for i in range(3):
            val[i].undraw()
          for i in range(len(informa)):
            informa[i].undraw()
          for i in range(5):
            quad[i].undraw()
          barra[0].draw(win)
          barra[2].draw(win)
          for i in range(395):
            barra[1] = gf.Rectangle(gf.Point(210,369),gf.Point(236+i,394))
            barra[1].setFill("green")
            barra[1].setOutline("green")
            barra[1].draw(win)
          sleep(1)
          pygame.mixer.music.play()
          for i in range(3):
            barra[i].undraw()
          barra[4].draw(win)
          barra[3].draw(win)
          botao[0].draw(win)
          botao[1].draw(win)
          encerrar = 2
          confirma = 0