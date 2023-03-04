import pygame

##########fonction/class##########

#rectangle(0,0,0,0,red , "block") #barre inexistante
#rectangle(0 , 0 , displayX , 50 , red , "block") #barre haut
#rectangle(0 , displayY - 50 , displayX , 50 , red , "block") #barre bas
#rectangle(displayX - 50 , 0, 50 , displayY , red , "block") #barre droite
#rectangle(0 , 0 , 50 , displayY , red , "block") #barre gauche

class rectangle:
    def __init__(self, x , y , sizex , sizey , couleur , type):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.couleur = couleur
        self.type = type

def draw():
    global ester_egg , tableau ,displayX , displayY , z_rouge
    win.fill((0 , 0 , 0))
    for i in z_rouge: pygame.draw.rect(win , i.couleur , (i.x , i.y , i.sizex , i.sizey))

    if tableau == 11 and green_key_take != True and green_gate_pos != "open": pygame.draw.rect(win , green_key.couleur , (green_key.x , green_key.y , green_key.sizex , green_key.sizey))

    if green_key_take == True and green_gate_pos != "open": pygame.draw.rect(win , green_key.couleur , (player.x - 10 , player.y - 10 , green_key.sizex , green_key.sizey))

    if ester_egg == True :
        if vu == False: pygame.draw.rect(win , egg.couleur , (player.x + 25 , player.y + 25 , egg.sizex , egg.sizey))
        if tableau == 1: win.blit(texte, (80 , 350))

    if tableau == 4: pygame.draw.rect(win , truc_vert.couleur , (truc_vert.x , truc_vert.y , truc_vert.sizex , truc_vert.sizey))
    
    pygame.draw.rect(win , player.couleur , (player.x , player.y , player.sizex , player.sizey))
    pygame.display.update()

#region tableau
def tableau_1():
    global displayY , displayX , red
    z_rouge_1 = rectangle(0 , displayY - 50 , displayX , 50 , red , "block")
    z_rouge_2 = rectangle(0 , 0 , displayX , 50 , red , "block")
    z_rouge_3 = rectangle(0 , 0 , 50 , displayY , red , "block")
    z_rouge_4 = rectangle(displayX - 50 , 0 , 50 , (displayY/2) - 50 , red , "block")
    z_rouge_5 = rectangle(displayX - 50 , (displayY/2) + 50 , 50 , (displayY/2) - 50 , red , "block")
    z_rouge_6 = rectangle(displayX/2 - 50 , displayY/2 - 50 , 100 , 100 , red , "block")
    z_rouge_7 = rectangle((displayX/2) - 35 , 0 , 70 , displayY/2 , red , "block") 
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , z_rouge_7]

def tableau_2():
    global displayY , displayX , red
    z_rouge_1 = rectangle(7*player.sizex , 0 , 50 , displayY - 5.5*player.sizex , red , "block")
    z_rouge_2 = rectangle(0 , 0 , displayX , 50 , red , "block")
    z_rouge_3 = rectangle(0 , displayY - 50 , displayX , 50 , red , "block")
    z_rouge_4 = rectangle(0 , 0 , 50 , (displayY/2) - 50 , red , "block")
    z_rouge_5 = rectangle(0 , (displayY/2) + 50 , 50 , (displayY/2) - 50 , red , "block")
    z_rouge_6 = rectangle(4*player.sizex + z_rouge_1.x , 5.5*player.sizex , 50 , displayY - 5.5*player.sizex , red , "block")
    z_rouge_7 = rectangle(z_rouge_6.x + 150 , (displayY/2) - 30 , displayX , 60 , red , "block")
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , z_rouge_7]

def tableau_3():
    global displayY , displayX , red
    z_rouge_1 = rectangle(displayX - 50 , 0, 50 , displayY , red , "block")
    z_rouge_2 = rectangle(0 , 0 , displayX , 50 , red , "block") 
    z_rouge_3 = rectangle(0 , displayY - 50 , displayX - 120 , 50 , red , "block")
    z_rouge_7 = rectangle(0 , (displayY/2) - 30 , displayX , 60 , red , "block")
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_7]

def tableau_4():
    global displayY , displayX , red
    z_rouge_1 = rectangle(displayX - 50 , 0, 50 , displayY - 120 , red , "block")
    z_rouge_2 = rectangle(0 , displayY - 50 , displayX , 50 , red , "block")
    z_rouge_3 = rectangle(0 , 0 , displayX - 120 , 50 , red , "block")
    z_rouge_4 = rectangle(0 , 120 , 50 , displayY , red , "block")
    z_rouge_5 = rectangle(120 , 0, 50 , displayY - 120 , red , "block")
    z_rouge_6 = rectangle((displayX/2) - 25 , 100 , 50 , displayY - 220 , red , "block") 
    z_rouge_7 = rectangle((displayX/2) - 25 , 100 , displayX , 50 , red , "block")
    z_rouge_8 = rectangle((displayX/2) - 25 , displayY - 170 , (displayX/2) -55 , 50 , red , "block")
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , z_rouge_7 , z_rouge_8]

def tableau_5():
    global displayY , displayX , red , orange_ennemie
    z_rouge_1 = rectangle(0 , displayY - 50 , (displayX/2) - 35 , 50 , red , "block") #bas gauche
    z_rouge_2 = rectangle(0 , 0 , displayX , 50 , red , "block") #haut
    z_rouge_3 = rectangle(0 , 0 , 50 , displayY , red , "block") #gauche
    z_rouge_4 = rectangle((displayX/2) + 35 , displayY - 50 , displayX , 50 , red , "block") # bas droit
    z_rouge_5 = rectangle(displayX - 50 , 120, 50 , displayY , red , "block") #droite bas
    ennemie = rectangle((displayX/2) - 15 , (displayY/2) - 15 , 30 , 30 , orange_ennemie , "ennemie")
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , ennemie]

def tableau_6():
    global displayY , displayX , red , green , green_gate_pos
    z_rouge_2 = rectangle(0 , 0 , displayX - 120 , displayY - 120 , red , "block") #haut
    z_rouge_3 = rectangle(displayX - 50 , 0, 50 , 50 , red , "block") #angle
    z_rouge_4 = rectangle(0 , displayY - 50 , displayX , 50 , red , "block") # bas
    z_rouge_5 = rectangle(displayX - 50 , 120, 50 , displayY , red , "block") #droite
    green_gate = rectangle(350 , displayY - 120 , 50 , 70 , green , "gate")
    liste = [z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5]
    if green_gate_pos == "close": liste.append(green_gate)
    return liste

def tableau_7():
    global displayY , displayX , red
    z_rouge_1 = rectangle(0 , displayY - 120 , displayX , 120 , red , "block")
    z_rouge_2 = rectangle(0 , 0 , 100 , 150 , red , "block")
    z_rouge_3 = rectangle(displayX - 100 , 0, 100 , 150 , red , "block")
    z_rouge_4 = rectangle(100 , 0 , 365 , 230 , red , "block")
    z_rouge_5 = rectangle(displayX - 465 , 0 , 365 , 230 , red , "block")
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5]

def tableau_8():
    global displayY , displayX , red
    z_rouge_1 = rectangle(0 , displayY - 100 , displayX-120 , 100 , red , "block") #bas gauche
    z_rouge_2 = rectangle(displayX - 50 , displayY - 100 , displayX , 100 , red , "block") #bas droite
    z_rouge_3 = rectangle(0 , 200 , (displayX/2) - 50 , 50 , red , "block") #bordure basse virage gauche
    z_rouge_4 = rectangle(0 , 0 , 117 , displayY , red , "block")#haut gauche gauche
    z_rouge_5 = rectangle(167 , 0 , 116 , 150 , red , "block") #centre virage gauche
    z_rouge_6 = rectangle(333 , 0 , 117 , 200 , red , "block") #haut centre gauche
    z_rouge_7 = rectangle((displayX/2) + 50 , 200 , (displayX/2) - 50 , 50 , red , "block") #bordure basse virage droit
    z_rouge_8 = rectangle(displayX - 117 , 0 , 117 , 200 , red , "block")#haut droite droite
    z_rouge_9 = rectangle(displayX - 284 , 0 , 116 , 150 , red , "block") #centre virage droite
    z_rouge_10 = rectangle(displayX - 450 , 0 , 117 , 200 , red , "block") #haut centre droite
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , z_rouge_7 , z_rouge_8 , z_rouge_9 , z_rouge_10]

def tableau_9():
    global displayY , displayX , red , orange_ennemie
    z_rouge_1 = rectangle(0 , displayY - 50 , (displayX/2) - 35 , 50 , red , "block") #bas gauche
    z_rouge_2 = rectangle(0 , 0 , (displayX/2) - 35 , 50 , red , "block") #haut gauche
    z_rouge_3 = rectangle((displayX/2) + 35 , 0 , displayX , 50 , red , "block") # haut droit
    z_rouge_4 = rectangle((displayX/2) + 35 , displayY - 50 , displayX , 50 , red , "block") # bas droit
    z_rouge_5 = rectangle(displayX - 50 , 0, 50 , displayY , red , "block") #barre droite
    z_rouge_6 = rectangle(0 , 120, 50 , displayY , red , "block") #gauche
    ennemie = rectangle(displayX - 100 , 50 , 50 , displayY - 100 , orange_ennemie , "ennemie2")
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , ennemie]

def tableau_10():
    global displayY , displayX , red , aqua , blue_gate_pos
    z_rouge_1 = rectangle(0 , 0 , displayX , 50 , red , "block") #barre haut
    z_rouge_2 = rectangle(displayX - 50 , 0, 50 , displayY , red , "block") #barre droite
    z_rouge_3 = rectangle(0 , displayY - 120 , 50 , 120 , red , "block") #gauche bas
    z_rouge_4 = rectangle(0 , 0 , 50 , 150 , red , "block") #gauche haut
    z_rouge_5 = rectangle((displayX/2) + 35 , displayY - 50 , displayX , 50 , red , "block") # bas droit
    z_rouge_6 = rectangle(0 , displayY - 50 , (displayX/2) - 35 , 50 , red , "block") #bas gauche
    blue_gate = rectangle((displayX/2) - 35 , displayY - 50 , 70 , 50 , aqua , "gate") #barre inexistante
    liste = [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6]
    if blue_gate_pos == "close": liste.append(blue_gate)
    return liste

def tableau_11():
    global displayY , displayX , red
    z_rouge_1 = rectangle(displayX - 50 , 0 , 50 , 150 , red , "block") #gauche haut
    z_rouge_2 = rectangle(displayX - 50 , displayY - 120 , 50 , 120 , red , "block") #gauche bas
    z_rouge_3 = rectangle(0 , 0 , 50 , displayY , red , "block") #barre gauche
    z_rouge_4 = rectangle(0 , displayY - 50 , displayX , 50 , red , "block") #barre bas
    z_rouge_5 = rectangle(0 , 0 , displayX , 50 , red , "block") #barre haut
    z_rouge_6 = rectangle(0,0,0,0,red , "block") #barre inexistante
    z_rouge_7 = rectangle(0,0,0,0,red , "block") #barre inexistante
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , z_rouge_7]

def tableau_12():
    global displayY , displayX , red
    z_rouge_1 = rectangle(0 , 100 , 117 , displayY , red , "block")#bas angle gauche
    z_rouge_2 = rectangle(167 , 0 , 116 , displayY , red , "block")#barre central virage gauche
    z_rouge_3 = rectangle((displayX/2) - 167 , 120 , 117 , displayY , red , "block") # centre gauche
    z_rouge_4 = rectangle(0 , 0 , (displayX/2) - 35 , 50 , red , "block") #haut gauche
    z_rouge_5 = rectangle((displayX/2) + 35 , 0 , displayX , 50 , red , "block") # haut droit
    z_rouge_6 = rectangle(displayX - 117 , 100 , 117 , displayY , red , "block")#bas angle droit
    z_rouge_7 = rectangle(displayX -284 , 0 , 116 , displayY , red , "block")#barre central virage droit
    z_rouge_8 = rectangle((displayX/2) + 50 , 120 , 117 , displayY , red , "block") # centre gauche
    return [z_rouge_1 , z_rouge_2 , z_rouge_3 , z_rouge_4 , z_rouge_5 , z_rouge_6 , z_rouge_7 , z_rouge_8]# , z_rouge_9 , z_rouge_10]
#endregion

##########programme##########

#region def_variable
loop = True
pos_p = False
green_key_take = True
vu = False
ester_egg = False
renvoie = False
cheat = False #    <------ cheat

tableau = 1
mort = 0
vel = 1
vit_ennemie = 0.8 
displayY = 576
displayX = 1000

green_gate_pos = "close"
blue_gate_pos = "close"

red = (120 , 0 , 0)
green = (0 , 255 , 0)
blue = (0 , 0 , 255)
aqua = (0 , 255 , 255)
grey = (100 , 100 , 100)
orange_ennemie = (242 , 100 , 17)

coo_depart = [100 , 100]
coo = [100 , 100]
z_rouge = tableau_1()

player = rectangle(coo_depart[0] , coo_depart[1] , 20 , 20 , blue , "player")
truc_vert = rectangle(displayX*0.718 , displayY/2 - 25 , 50 , 50 , green , "interupteur")
egg = rectangle(player.x + 25 , player.y + 25 , 5 , 5 , grey , "egg")
green_key = rectangle(99 , 200 , 5 , 5 , green , "green key")




pygame.init()
police = pygame.font.SysFont('comicsansms' , 40)
texte = police.render("Dorian Titouan Eden Jinx Dorier. 06/02/2023" , 1 , grey)
win = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("UUC-G")
#endregion

while loop == True:
    coo = [player.x , player.y]

    if pos_p == True: print(f"({player.x} , {player.y})")
    
    pygame.time.delay(2)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: loop = False

    keys = pygame.key.get_pressed()

    #region mouvement
    if keys[pygame.K_UP] and player.y > 0: player.y -= vel

    elif keys[pygame.K_DOWN] and player.y < (displayY - player.sizey): player.y += vel

    elif keys[pygame.K_LEFT] and player.x > 0: player.x -= vel

    elif keys[pygame.K_RIGHT] and player.x < (displayX - player.sizex): player.x += vel

    #endregion

    #region mouv ennemie
    if z_rouge[-1].type == "ennemie" :
        if abs(z_rouge[-1].x - player.x) > 20 and z_rouge[-1].x < player.x: z_rouge[-1].x += vit_ennemie

        elif abs(z_rouge[-1].x - player.x) > 20 and z_rouge[-1].x > player.x: z_rouge[-1].x -= vit_ennemie

        elif  z_rouge[-1].y < player.y: z_rouge[-1].y += vit_ennemie

        elif  z_rouge[-1].y > player.y: z_rouge[-1].y -= vit_ennemie
    #endregion

    #region mouv ennemie2
    if z_rouge[-1].type == "ennemie2" :
        en = z_rouge[-1]
        if en.x > 200 and renvoie == False: en.x -= vit_ennemie*2
        elif renvoie == True and (en.x < (displayX - 100)) : en.x += vit_ennemie*2
        elif en.x <= 200: renvoie = True
        else: renvoie = False
    #endregion

    #region touche ennemie
    for i in z_rouge:
        if cheat != True and ((i.type == "ennemie") or (i.type == "ennemie2")):
            if (player.x > i.x and player.x < (i.x + i.sizex)) or ((player.x + player.sizex) > i.x and (player.x + player.sizex) < (i.x + i.sizex)) :
                if (player.y > i.y and player.y < (i.y + i.sizey)) or ((player.y + player.sizey) > i.y and (player.y + player.sizey) < (i.y + i.sizey)) :  
                    player.x , player.y = 100 , 100
                    tableau = 1
                    z_rouge = tableau_1()
                    mort += 1
                    print(f"Vous êtez mort {mort} fois.")   
    #endregion

    #region touche zone rouge
    for i in z_rouge:
        if cheat != True and (i.type == "block" or i.type == "gate"):
            if (player.x > i.x and player.x < (i.x + i.sizex)) or ((player.x + player.sizex) > i.x and (player.x + player.sizex) < (i.x + i.sizex)) :
                if (player.y > i.y and player.y < (i.y + i.sizey)) or ((player.y + player.sizey) > i.y and (player.y + player.sizey) < (i.y + i.sizey)) :  
                    player.x , player.y = coo[0] , coo[1]
         
    #endregion

    #region touche clef vert
    if tableau == 11 and ((player.x > green_key.x and player.x < (green_key.x + green_key.sizex)) or ((player.x + player.sizex) > green_key.x and (player.x + player.sizex) < (green_key.x + green_key.sizex))) :
        if ((player.y > green_key.y) and (player.y < (green_key.y + green_key.sizey))) or (((player.y + player.sizey) > green_key.y) and ((player.y + player.sizey) < (green_key.y + green_key.sizey))) :
            green_key_take = True
         
    #endregion
    
    #region changement tableau
    if tableau == 1 and player.x >= displayX - player.sizex:
        if ester_egg == True: 
            vu = True
            ester_egg = None 
        coo_depart = [10 , player.y]
        z_rouge = tableau_2()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 2
        print(tableau)

    elif tableau == 2 and player.x < 10: 
        coo_depart = [displayX - 22 , player.y]
        z_rouge = tableau_1()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 1
            
        print(tableau)

    elif tableau == 2 and player.x >= displayX - player.sizex:
        coo_depart = [10 , player.y]
        z_rouge = tableau_3()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 3
        print(tableau)

    elif tableau == 3 and player.x < 10: 
        coo_depart = [displayX - 22 , player.y]
        z_rouge = tableau_2()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 2
        print(tableau)
    
    elif tableau == 3 and player.y >= displayY - player.sizex:
        coo_depart = [player.x , 10]
        z_rouge = tableau_4()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 4
        print(tableau)

    elif tableau == 4 and player.y < 10: 
        coo_depart = [player.x , displayY - 22 ]
        z_rouge = tableau_3()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 3
        print(tableau)
    
    elif tableau == 4 and player.x < 10:
        coo_depart = [displayX - 22 , player.y]
        z_rouge = tableau_5()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 5
        print(tableau)

    elif tableau == 4 and player.x >= displayX - player.sizex:
        coo_depart = [22 , player.y]
        z_rouge = tableau_6()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 6
        print(tableau)
    
    elif tableau == 5 and player.x >= displayX - player.sizex:
        coo_depart = [10 , player.y]
        z_rouge = tableau_4()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 4
        print(tableau)

    elif tableau == 5 and player.y >= displayY - player.sizex:
        coo_depart = [player.x , 22]
        z_rouge = tableau_7()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 7
        print(tableau)

    elif tableau == 6 and player.x <= player.sizex:
        coo_depart = [displayX - 22 , player.y]
        z_rouge = tableau_4()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 4
        print(tableau)
    
    elif tableau == 6 and player.y < 10: 
        coo_depart = [player.x , displayY - 22 ]
        z_rouge = tableau_8()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 8
        print(tableau)  

    elif tableau == 6 and player.x >= displayX - player.sizex:
        coo_depart = [22 , player.y]
        z_rouge = tableau_9()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 9
        print(tableau)

    elif tableau == 7 and player.y < 10: 
        coo_depart = [player.x , displayY - 22 ]
        z_rouge = tableau_5()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 5
        print(tableau)
    
    elif tableau == 7 and player.x >= displayX - player.sizex:
        coo_depart = [10 , player.y]
        z_rouge = tableau_10()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 10
        print(tableau)
    
    elif tableau == 7 and player.x < 10:
            coo_depart = [displayX - 22 , player.y]
            z_rouge = tableau_11()
            player.x , player.y = coo_depart[0] , coo_depart[1]
            tableau = 11
            print(tableau)

    elif tableau == 8 and player.y >= displayY - player.sizex:
        coo_depart = [player.x , 22]
        z_rouge = tableau_6()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 6
        print(tableau)
    
    elif tableau == 8 and player.y < 10: 
        coo_depart = [player.x , displayY - 22 ]
        z_rouge = tableau_12()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 12
        print(tableau)

    elif tableau == 9 and player.x <= player.sizex:
        coo_depart = [displayX - 22 , player.y]
        z_rouge = tableau_6()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 6
        print(tableau)
    
    elif tableau == 10 and player.x < 10:
        coo_depart = [displayX - 22 , player.y]
        z_rouge = tableau_7()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 7
        print(tableau)

    elif tableau == 11 and player.x >= displayX - player.sizex:
        coo_depart = [10 , player.y]
        z_rouge = tableau_7()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 7
        print(tableau)
    
    elif tableau == 12 and player.y >= displayY - player.sizex:
        coo_depart = [player.x , 22]
        z_rouge = tableau_8()
        player.x , player.y = coo_depart[0] , coo_depart[1]
        tableau = 8
        print(tableau)

    #endregion
    
    #region event
    if tableau == 4 and ((player.x > truc_vert.x and player.x < (truc_vert.x + truc_vert.sizex)) or ((player.x + player.sizex) > truc_vert.x and (player.x + player.sizex) < (truc_vert.x + truc_vert.sizex))) :
        if ((player.y > truc_vert.y) and (player.y < (truc_vert.y + truc_vert.sizey))) or (((player.y + player.sizey) > truc_vert.y) and ((player.y + player.sizey) < (truc_vert.y + truc_vert.sizey))) :
            if green_key_take == False: print("Il manque quelque chose ... Peut-être une clef ?")
            elif green_key_take == True:
                green_gate_pos = "open"
                print("Quelque chose semble s'être ouvert ...")

    if tableau == 3 and player.x >= 800 and player.y < 264 and ester_egg != None: ester_egg = True
    #endregion
    
    draw()
          
pygame.quit()