import pygame, sys, os, random, math, time
import pygame.mixer
from pygame.locals import *
import pygame.sprite as sprite

pygame.init()
crash_sound = pygame.mixer.Sound('sound_car_crash.ogg')         # Som de batidas
pygame.mixer.music.load('song_game.ogg')                        # Som de fundo


#------------------------------------------------
# Guarda os arquivos que seram usados no jogo
#------------------------------------------------
carro = 'veneno.png'
pista = 'pista.jpg'
inimigo1 = 'inimigo1.png'
inimigo2 = 'inimigo2.png'
inimigo3 = 'inimigo3.png'
inimigo4 = 'inimigo4.png'
inimigo5 = 'inimigo5.png'
inimigo6 = 'inimigo6.png'
inimigo7 = 'inimigo7.png'
inimigo8 = 'inimigo8.png'
inimigo9 = 'inimigo9.png'
inimigo10 = 'inimigo10.png'
menu_ = 'Lamborghini Veneno.jpg'
Font_text = pygame.font.SysFont('ShowcardGothic', 50, italic=True)
Font_text_2 = pygame.font.SysFont('ShowcardGothic', 35, italic=True)
rank_image = 'rank.jpg'


#--------------------------------
# Cores RGB
#--------------------------------
yellow = (255,255,0)    
yellow_2 = (100,100,0)  
black = (0,0,0)         
white = (255,255,255)   
orange = (255,128,0)    
red = (240,0,0)         
red_2 = (100,0,0)       
red_3 = (220,0,0)       
green = (0,240,0)      
green_2 = (0,100,0)     
blue = (0,255,255)     
blue_2 = (0,100,100)   
blue_3 = (0,200,255)  
gray = (15,15,15)     

display_width = 480
display_height = 570

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cars Attack')                           # Nome do jogo na barra do windows
icon = pygame.image.load('veneno_icon.png')                         # Icone do carro na janela do windows
pygame.display.set_icon(icon)
background = pygame.image.load(pista)                               # Pista
veneno_wallpaper = pygame.image.load(menu_)                         # Tela de fundo menu


#-------------------------------------------------------------------------------------------
# Cria a partir dos dados dos arquivos .txt, textos com seus conteudos na tela, os ranks
#-------------------------------------------------------------------------------------------
def rank_textScore():
    font = pygame.font.SysFont("impactregular", 35)
    font2 = pygame.font.SysFont("impactregular", 40)
    myRecord = open('Record.txt', 'r')
    scoreFile1 = open('Score1.txt', 'r')
    scoreFile2 = open('Score2.txt', 'r')
    scoreFile3 = open('Score3.txt', 'r')
    myRecord_read = myRecord.read()
    scoreFile1_read = scoreFile1.read()
    scoreFile2_read = scoreFile2.read()
    scoreFile3_read = scoreFile3.read()
    text = font2.render((myRecord_read), True, green)
    text2 = font.render((scoreFile1_read), True, blue)
    text3 = font.render((scoreFile2_read), True, blue)
    text4 = font.render((scoreFile3_read), True, blue)
    screen.blit(text, (20, 80))
    screen.blit(text2, (20, 130))
    screen.blit(text3, (20, 180))
    screen.blit(text4, (20, 230))


#------------------------------------------------------------------------
# Cria o botao Score no canto superior da tela do jogo
#------------------------------------------------------------------------
def score_cars(contagem):                                      
    font = pygame.font.SysFont('Narkisim', 18, bold=True)
    text = font.render('Score: '+str(contagem), True, yellow)
    screen.blit(text, (345,10))


#------------------------------------------------------------------------
# Tela de menu
#------------------------------------------------------------------------
def start_menu():                                           
    start = True
    while start:
        for event in pygame.event.get():
            #print event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(veneno_wallpaper, (-90,120))
        Text_on_Screen, Text_Font = text_2('Cars Attack', Font_text)
        Text_Font.center = ((242), (70))
        screen.blit(Text_on_Screen, Text_Font)

        buttons()
        pygame.display.update()


#------------------------------------------------------------------------
# Essa funcao cria os botoes para a tela de menu
#------------------------------------------------------------------------    
def buttons():                                              
    button = pygame.mouse.get_pos()
    mouse_clicks = pygame.mouse.get_pressed()
    if 80+80 > button[0] > 80 and 480+30 > button[1] > 480:       
        pygame.draw.rect(screen, green_2, (80,480,80,30))
        if mouse_clicks[0] == 1:
            game_loop()            
    else:
        pygame.draw.rect(screen, gray, (80,480,80,30))
        
    if 320+80 > button[0] > 320 and 480+30 > button[1] > 480:
        pygame.draw.rect(screen, red_2, (320,480,80,30))
        if mouse_clicks[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(screen, gray, (320,480,80,30))

    if 200+80 > button[0] > 200 and 480+30 > button[1] > 480:
        pygame.draw.rect(screen, yellow_2, (200,480,80,30))
        if mouse_clicks[0] == 1:
            rank()
    else:
        pygame.draw.rect(screen, gray, (200,480,80,30))
    

    button_text = pygame.font.SysFont('impactregular', 21)
    Text_on_Screen, Text_Font = text_2('Play', button_text)
    Text_Font.center = ((80 + (80/2)), (480 + (30/2)))
    screen.blit(Text_on_Screen, Text_Font)

    button_text = pygame.font.SysFont('impactregular', 21)
    Text_on_Screen, Text_Font = text_3('Exit', button_text)
    Text_Font.center = ((320 + (80/2)), (480 + (30/2)))
    screen.blit(Text_on_Screen, Text_Font)

    button_text = pygame.font.SysFont('impactregular', 21)
    Text_on_Screen, Text_Font = text_4('Rank', button_text)
    Text_Font.center = ((200 + (80/2)), (480 + (30/2)))
    screen.blit(Text_on_Screen, Text_Font)


#--------------------------------------------------------------------
# Cria a tela de Rank
#--------------------------------------------------------------------
def rank():                                                 
    while True:
        for event in pygame.event.get():
            #print event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen_rank = pygame.image.load(rank_image)
        screen.blit(screen_rank, (-200,33))

        rank_textScore()

        button_rank()
        
        pygame.display.update()


#-------------------------------------------------------------------
# Botao Play para tela de Rank (Inicia o loop do jogo)
#-------------------------------------------------------------------
def button_rank():                                          
    button_2 = pygame.mouse.get_pos()
    mouse_clicks_2 = pygame.mouse.get_pressed()
    if 20+50 > button_2[0] > 20 and 480+30 > button_2[1] > 480:       
        pygame.draw.rect(screen, green_2, (20,480,50,30))
        if mouse_clicks_2[0] == 1:
            game_loop()
    else:
        pygame.draw.rect(screen, gray, (20,480,50,30))

    button_text_2 = pygame.font.SysFont('impactregular', 20)
    Text_on_Screen, Text_Font = text_2('Play', button_text_2)
    Text_Font.center = ((20 + (50/2)), (480 + (30/2)))
    screen.blit(Text_on_Screen, Text_Font)
    
    
#----------------------------------------------------
# Funcoes declaradas para os carros
#----------------------------------------------------
def car1(car1x, car1y, car1w, car1h):                       
    [car1x, car1y, car1w, car1h]

def car2(car2x, car2y, car2w, car2h): 
    [car2x, car2y, car2w, car2h]

def car3(car3x, car3y, car3w, car3h): 
    [car3x, car3y, car3w, car3h]

def car4(car4x, car4y, car4w, car4h):
    [car4x, car4y, car4w, car4h]

def car5(car5x, car5y, car5w, car5h): 
    [car5x, car5y, car5w, car5h]

def car6(car6x, car6y, car6w, car6h): 
    [car6x, car6y, car6w, car6h]

def car7(car7x, car7y, car7w, car7h): 
    [car7x, car7y, car7w, car7h]

def car8(car8x, car8y, car8w, car8h): 
    [car8x, car8y, car8w, car8h]


#-----------------------------------------------------------------------------------------------
# Funcoes que retornam textos em diferentes corres usando os modelos RGB declarados acima
#-----------------------------------------------------------------------------------------------
def text_(text, font):                                      
    Text_on_Screen = font.render(text, True, white)
    return Text_on_Screen, Text_on_Screen.get_rect()

def text_2(text, font):
    Text_on_Screen = font.render(text, True, green)
    return Text_on_Screen, Text_on_Screen.get_rect()

def text_3(text, font):
    Text_on_Screen = font.render(text, True, red)
    return Text_on_Screen, Text_on_Screen.get_rect()

def text_4(text, font):
    Text_on_Screen = font.render(text, True, yellow)
    return Text_on_Screen, Text_on_Screen.get_rect()

def text_5(text, font):
    Text_on_Screen = font.render(text, True, red_3)
    return Text_on_Screen, Text_on_Screen.get_rect()


#--------------------------------------------------------------------------
# Funcao criada para ser chamada apenas se o carro bater, 'You Crashed!'
#--------------------------------------------------------------------------
def message(text):                                          
    Text_on_Screen, Text_Font = text_5(text, Font_text)
    Text_Font.center = ((display_width/2), (display_height/2))
    screen.blit(Text_on_Screen, Text_Font)
    

#--------------------------------------------------------------------------
# Funcao criada para ser chamada apenas se o carro bater, 'Game Over'
#--------------------------------------------------------------------------
def message_2(text):
    Text_on_Screen, Text_Font = text_5(text, Font_text_2)
    Text_Font.center = ((240), (340))
    screen.blit(Text_on_Screen, Text_Font)

    pygame.display.update()
    
    time.sleep(4)   # Pausa de 4 segundos para o jogo se iniciar novamente
   
    game_loop()     # Apos a mensagem, o jogo se inicia novamente apos a pausa
   

#-------------------------------------------------------------------------------
# Funcao criada para batidas, a musica do jogo para e inicia o som de batida
#-------------------------------------------------------------------------------   
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message('You Crashed!')
    message_2('Game Over')


#-------------------------------------------------
# Funcao do loop do jogo
#-------------------------------------------------
def game_loop():

       
    pygame.mixer.music.play(-1)                             # Faz a musica tocar repetidas vezes durante o jogo
    
    car = pygame.image.load(carro)                          # Carrega Meu Carro

    car1_load = pygame.image.load(inimigo1)                 # Carrega Inimigo1
    car2_load = pygame.image.load(inimigo2)                 # Carrega Inimigo2
    car3_load = pygame.image.load(inimigo3)                 # Carrega Inimigo3
    car4_load = pygame.image.load(inimigo4)                 # Carrega Inimigo4
    car5_load = pygame.image.load(inimigo5)                 # Carrega Inimigo5
    car6_load = pygame.image.load(inimigo9)                 # Carrega Inimigo9
    car7_load = pygame.image.load(inimigo7)                 # Carrega Inimigo7
    car8_load = pygame.image.load(inimigo10)                # Carrega Inimigo10
    

    FPS = 60                                                # Taxa de quadros por segundo
    fpsTime = pygame.time.Clock()


    carX = 211                                              # Posicao inicial do meu carro
    carY = 460                                              # Posicao inicial do meu carro
    
    x_direction = 0                                         # Variavel criada para direcao do meu carro, sera util para dar movimento
    
    
    car1_startx = random.randrange(210, 390)                # Movendo inicial do 1º inimigo, cai de uma posicao aleatoria 
    car1_starty = -500
    car1_speed = 7
    car1_width = 30
    car1_height = 90

    car2_startx = random.randrange(50, 200)                 # Movendo inicial do 2º inimigo, cai de uma posicao aleatoria  
    car2_starty = -800
    car2_speed = 7
    car2_width = 30
    car2_height = 90

    car3_startx = random.randrange(210, 390)                # Movendo inicial do 3º inimigo, cai de uma posicao aleatoria 
    car3_starty = -1100
    car3_speed = 7
    car3_width = 30
    car3_height = 90

    car4_startx = random.randrange(50, 200)                 # Movendo inicial do 4º inimigo, cai de uma posicao aleatoria 
    car4_starty = -1400
    car4_speed = 7
    car4_width = 30
    car4_height = 90

    car5_startx = random.randrange(70, 370)                # Movendo inicial do 5º inimigo, cai de uma posicao aleatoria 
    car5_starty = -1700
    car5_speed = 10
    car5_width = 30
    car5_height = 110

    car6_startx = random.randrange(50, 200)                 # Movendo inicial do 6º inimigo, cai de uma posicao aleatoria
    car6_starty = -2000
    car6_speed = 7
    car6_width = 30
    car6_height = 90

    car7_startx = random.randrange(210, 390)                # Movendo inicial do 7º inimigo, cai de uma posicao aleatoria
    car7_starty = -2300
    car7_speed = 7
    car7_width = 30
    car7_height = 90

    car8_startx = random.randrange(50, 200)                 # Movendo inicial do 8º inimigo, cai de uma posicao aleatoria
    car8_starty = -2600
    car8_speed = 7
    car8_width = 30
    car8_height = 90


    score = 0

    gameExit = False


#----------------------------------------------------------
# Funcoes criadas para salvar em arquivo os Scores
#----------------------------------------------------------
    def arquivo_score1():
        arquivo1 = open("Score1.txt", 'w')
        arquivo1.write("1º  %d" %(score))
        arquivo1.close()
    def arquivo_score2():
        arquivo2 = open("Score2.txt", 'w')
        arquivo2.write("2º  %d" %(score))
        arquivo2.close()
    def arquivo_score3():
        arquivo3 = open("Score3.txt", 'w')
        arquivo3.write("3º  %d" %(score))
        arquivo3.close()
    def arquivo_record():
        arquivo4 = open("Record.txt", 'w')
        arquivo4.write("Record: %d" %(score))
        arquivo4.close()
    def return_score1():
        arquivo3 = open("Score3.txt", 'w')
        arquivo3.write("3º  %s" %str(30))
        arquivo3.close()            
    def return_score2():
        arquivo2 = open("Score2.txt", 'w')
        arquivo2.write("2º  %s" %str(50))
        arquivo2.close()



    while not gameExit:
        

        screen.blit(background, (0,0))                                  # Faz a pista aparecer na tela do jogo
        
        car1(car1_startx, car1_starty, car1_width, car1_height)         # Chama a funcao car1() com paremetros de movimento, tamanho que ocupa e velocidade
        car1_starty += car1_speed
        score_cars(score)

        car2(car2_startx, car2_starty, car2_width, car2_height)         # Chama a funcao car2() com paremetros de movimento, tamanho que ocupa e velocidade
        car2_starty += car2_speed
        score_cars(score)

        car3(car3_startx, car3_starty, car3_width, car3_height)         # Chama a funcao car3() com paremetros de movimento, tamanho que ocupa e velocidade
        car3_starty += car3_speed
        score_cars(score)

        car4(car4_startx, car4_starty, car4_width, car4_height)         # Chama a funcao car4() com paremetros de movimento, tamanho que ocupa e velocidade
        car4_starty += car4_speed
        score_cars(score)

        car5(car5_startx, car5_starty, car5_width, car5_height)         # Chama a funcao car5() com paremetros de movimento, tamanho que ocupa e velocidade
        car5_starty += car5_speed
        score_cars(score)

        car6(car6_startx, car6_starty, car6_width, car6_height)         # Chama a funcao car6() com paremetros de movimento, tamanho que ocupa e velocidade
        car6_starty += car6_speed
        score_cars(score)

        car7(car7_startx, car7_starty, car7_width, car7_height)         # Chama a funcao car7() com paremetros de movimento, tamanho que ocupa e velocidade
        car7_starty += car7_speed
        score_cars(score)

        car8(car8_startx, car8_starty, car8_width, car8_height)         # Chama a funcao car8() com paremetros de movimento, tamanho que ocupa e velocidade
        car8_starty += car8_speed
        score_cars(score)


        
        screen.blit(car, (carX,carY))                                   # Faz meu carro aparecer na tela nas posicoes inicias declaradas antes                        

        screen.blit(car1_load, (car1_startx , car1_starty))             # Faz os carros aparecerem na tela com os parametros declarados antes
        screen.blit(car2_load, (car2_startx , car2_starty))   
        screen.blit(car3_load, (car3_startx , car3_starty))  
        screen.blit(car4_load, (car4_startx , car4_starty))
        screen.blit(car5_load, (car5_startx , car5_starty))
        screen.blit(car6_load, (car6_startx , car6_starty))
        screen.blit(car7_load, (car7_startx , car7_starty))
        screen.blit(car8_load, (car8_startx , car8_starty))


        for event in pygame.event.get():
            #print event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


#---------------------------------------------------------------
# Da movimento ao meu carro
#---------------------------------------------------------------                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_direction = -7                        # Altera o tempo de resposta do teclado
                if event.key == pygame.K_RIGHT:
                    x_direction = 7                         # Altera o tempo de resposta do teclado
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_direction = 0
                   
        carX += x_direction


#--------------------------------------------------------------------------------------------------
# Se os parametros informados para o limite da pista forem invadidos, chama a funcao crash()
#--------------------------------------------------------------------------------------------------        
        if carX > 395 or carX < 30:
            crash()


#-------------------------------------------------------------------------------------------------
# Esses parametros fazem os carros cairem novamente da tela, porem com uma nova velocidade
#-------------------------------------------------------------------------------------------------
        if car1_starty > display_height:            
            car1_starty = 0 - 2000                          # Altera o tempo de queda do carro
            car1_startx = random.randrange(210, 390)        # Faz os carros cairem novamente em posicoes aleatorias
            score += 1                                      # A variavel Score é aumentada a cada passada
            car1_speed += 0.2                               # O velocidade é aumentada a cada passada
            
        if car2_starty > display_height:            
            car2_starty = 0 - 2200
            car2_startx = random.randrange(50, 200)
            score += 1
            car2_speed += 0.2

        if car3_starty > display_height:
            car3_starty = 0 - 2300
            car3_startx = random.randrange(210, 390)
            score += 1
            car3_speed += 0.2
            
        if car4_starty > display_height:
            car4_starty = 0 - 2500
            car4_startx = random.randrange(50, 200)
            score += 1
            car4_speed += 0.2

        if car5_starty > display_height:
            car5_starty = 0 - 4000
            car5_startx = random.randrange(70, 370)
            score += 1
            car5_speed += 0.0

        if car6_starty > display_height:
            car6_starty = 0 - 2900
            car6_startx = random.randrange(50, 200)
            score += 1
            car6_speed += 0.2

        if car7_starty > display_height:
            car7_starty = 0 - 3100
            car7_startx = random.randrange(210, 390)
            score += 1
            car7_speed += 0.2

        if car8_starty > display_height:
            car8_starty = 0 - 3300
            car8_startx = random.randrange(50, 200)
            score += 1
            car8_speed += 0.2


#--------------------------------------
# Sistema de colisoes
#--------------------------------------
        if carY < car1_starty + car1_height:
            if carX > car1_startx and carX < car1_startx + car1_width or carX + 38 > car1_startx and carX + 30 < car1_startx + car1_width:
                crash()

        if carY < car2_starty + car2_height:
            if carX > car2_startx and carX < car2_startx + car2_width or carX + 38 > car2_startx and carX + 30 < car2_startx + car2_width:
                crash()

        if carY < car3_starty + car3_height:
            if carX > car3_startx and carX < car3_startx + car3_width or carX + 38 > car3_startx and carX + 30 < car3_startx + car3_width:
                crash()

        if carY < car4_starty + car4_height:
            if carX > car4_startx and carX < car4_startx + car4_width or carX + 38 > car4_startx and carX + 30 < car4_startx + car4_width:
                crash()
                
        if carY < car5_starty + car5_height:
            if carX > car5_startx and carX < car5_startx + car5_width or carX + 38 > car5_startx and carX + 40 < car5_startx + car5_width:
                crash()

        if carY < car6_starty + car6_height:
            if carX > car6_startx and carX < car6_startx + car6_width or carX + 38 > car6_startx and carX + 40 < car6_startx + car6_width:
                crash()

        if carY < car7_starty + car7_height:
            if carX > car7_startx and carX < car7_startx + car7_width or carX + 38 > car7_startx and carX + 40 < car7_startx + car7_width:
                crash()

        if carY < car8_starty + car8_height:
            if carX > car8_startx and carX < car8_startx + car8_width or carX + 38 > car8_startx and carX + 40 < car8_startx + car8_width:
                crash()

#-----------------------------------------------------------
# Algoritmo que altera o valor do rank
#-----------------------------------------------------------
        if score > 0:
            if score >= 30 and score < 50:
                arquivo_score3()
            elif score >= 50:
                return_score1()                
            if score > 50 and score < 100:
                arquivo_score2()
            elif score >= 100:
                    return_score2()                    
            if score > 100:
                arquivo_score1()
            if score > 220:
                arquivo_record()
                arquivo_score1()

            
        
        pygame.display.update()
        fpsTime.tick(FPS)
     
start_menu()
game_loop()
pygame.quit()
quit()
