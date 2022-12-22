import re,random,time,os
 
N=10
COLONNES=[str(i) for i in range(N)]
LIGNES = [' '] + list(map(chr, range(97, 107)))
DICT_LIGNES_INT = {LIGNES[i]:i-1 for i in range(len(LIGNES))}
VIDE = '.'
EAU='o'
TOUCHE= 'x'  
BATEAU= '#'
DETRUIT='@'
NOMS=['Transporteur','Cuirasse','Croiseur','Sous-marin','Destructeur']
TAILLES=[5,4,3,3,2]
#h5
BLANC=""
DECALGE=0
#♣5

def create_grid():
    return [[VIDE for i in range(N)]for x in range(N)]


def plot_grid(m):
     print(" ",end=" ")
     for z in COLONNES:
         print(BLANC + z,end=" ")
     for i in range(len(m)):
         print(" ")
         print(BLANC + LIGNES [i+1],end=" ")
         for w in (m[i]):
             print(w,end=" ")
     print(BLANC+' ')
     
     
     
def show_grid(m,flotte): # montre les bateau pour faciliter la placement 
    print(" ",end=" ")
    for z in COLONNES:
        print(BLANC + z,end=" ")
    for i in range(len(m)):
        print(" ")
        print(BLANC + LIGNES [i+1],end=" ")
        for w in range(len(m[i])):
            if presence_bateau((i,w), flotte)==True: #  soit bateau 
                print(BATEAU,end=" ")
            else :
                print(VIDE,end=" ") # soit vide
    print(BLANC+' ')


def random_position():
    r=[random.randrange(0,N) for i in range(2)]
    r=tuple(r)
    return(r)
# Partis 5 
def better_random_Choice(): # caluce en bas de page
    poid =[0.003304421790625443, 0.005804647326434086, 0.007312515304215586, 0.00815021973631642, 0.008655419947675692, 0.008418285154588687, 0.008224968747180803, 0.007449125565450492, 0.005678347273594267, 0.003407523874576315, 0.006113953578286701, 0.008482723957057983, 0.010011212351629658, 0.010892735169409612, 0.011186576108669596, 0.011410823141262743, 0.01103450053484206, 0.010168443029654736, 0.008856469011379892, 0.005701545242483214,0.007472323534339438, 0.010248347144716662, 0.011477839495830809, 0.012508860335339529, 0.012369672522005852, 0.012671246117562152, 0.012320699032129187, 0.01146495173533695, 0.010467439073112265, 0.00698774373977034,0.008596136249403941, 0.01097779438866908, 0.012034590749165517, 0.012745995128426533, 0.013323366798551416, 0.012880027837562667, 0.012245950021264804, 0.01189540293583184, 0.011070586264224866, 0.007753276713105563,0.008490456613354297, 0.011318031265706957, 0.012691866534352326, 0.013063034036575464, 0.013797636384725425, 0.013609475081515086, 0.012508860335339529, 0.01276919309731548, 0.011658268142744834, 0.008650264843478148,0.008567783176317451, 0.011129869962496618, 0.012663513461265836, 0.012990862577809854, 0.013050146276081606, 0.01330016882966247, 0.012336164344721817, 0.0128130114829946, 0.011756215122498163, 0.008505921925946928,0.008026497235575374, 0.010658177928421378, 0.012480507262253039, 0.011910868248424472, 0.012934156431636874, 0.013447089299292461, 0.012622272627685487, 0.012248527573363577, 0.011261325119533979, 0.008067738069155722,0.007299627543721728, 0.009616846880517572, 0.011560321162991508, 0.01165053548644852, 0.012132537728918846, 0.012508860335339529, 0.012243372469166033, 0.01183869678965886, 0.010758702460273478, 0.007621821556068202,0.006036627015323547, 0.008572938280514995, 0.010482904385704896, 0.010946863763483819, 0.010957173971878906, 0.011158223035583106, 0.011124714858299073, 0.010031832768419832, 0.008820383281997088, 0.006031471911126004,0.003670434188651038, 0.005920637170878817, 0.007709458327426443, 0.008137331975822561, 0.008199193226193084, 0.008222391195082031, 0.008029074787674145, 0.0069387702498936756, 0.005693812586186898, 0.0033611279367984225]
    Population=[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
    return random.choices(Population,poid)[0]

def pos_string(s,m):
    if len(s)!=3  : # taille normal
        print("Retirer s'il vous plait form: 'a 1'")
        return False
    else:
         exp=(re.findall("[abcdefghij][ ][0-9]", s ))# Permet de trouver l'odre en permetant dans la souplesse. 
         
         if exp==[]:
             print("Retirer s'il vous plait form: 'a 1'") # pas la bone forme
             return False
         elif m[int(LIGNES.index(exp[0][0]))-1][int(exp[0][2])]!=VIDE: # verifier l'originalité de l'attack
             print(" Vous avez deja attaquer cette position") 
             return False
         else:
             return(int(LIGNES.index(exp[0][0]))-1,int(exp[0][2]))  
         
def nouveau_bateau(flotte,nom,taille,pos,orientation):
    emplacement=[] # soit l'enseble des position
    orientation=orientation[2]
    for i in range(taille):
        if orientation=="h":
            emplacement.append((pos[0],pos[1]+i))
            if pos[1]+i > 9 or presence_bateau((pos[0],pos[1]+i),flotte)==True: # verifie que es position soit possible
                return( False) # Stop le probleme
            
        elif orientation=="v": # cf au dessus
            emplacement.append((pos[0]+i,pos[1]))
            if pos[0]+i > 9 or presence_bateau((pos[0]+i,pos[1]),flotte)==True:
                return False
        else:
            print("erreur")    
    bateau={} # creez un dictionnaire pour les info du bateau
    bateau['nom']=nom
    bateau['taille']=taille
    bateau['case touché']=0 #intact
    bateau['position']=emplacement[::]
    flotte.append(bateau)
    return True

def presence_bateau(pos,flotte): 
    for bateau in flotte: # pour chaque bateau
        for quai in bateau['position']: # chaque partie de bateau
            if pos==quai: # verifie une correspondance
                return True
    else : return False
    

def ajout_bateau(flotte,nom,taille):
    ftour=False
    while ftour == False:
        reponse=(input(("Oû mettre votre bateau : " + str(nom)+" de taille "+ str(taille)+" ?    ")))
        if len(reponse)!=3  :
            print("De la forme : 'a 1'")
        else:
            exp=(re.findall("[abcdefghij][ ][0-9]", reponse )) # verifie la posibilité dela réponse
            if exp==[]:
                print("De la forme : 'a 1'")
            else:
                position_bateau=(int(LIGNES.index(exp[0][0])-1),int(exp[0][2]))
                reponse=input("dans quel sens [ h ou v ] ? ")
                exp=(re.findall(r"[hv]", str(reponse)))
                if len(exp)!=1 : print(" h ou v") # une seul boucle pour éviter le blocage du jeux en cas impossible ( comme marqué J 9)
                
                else :
                    print(position_bateau, exp) # sinon cree la flotte
                    a= nouveau_bateau(flotte, nom, taille, position_bateau , str(exp))
                    print(flotte)
                    if a==False : 
                        print("Position NON-valide")
                    if a==True :
                        ftour= True # fin du while
                        


def id_bateau_at_pos(pos,flotte): # commme presence
    for bateau in flotte:
        for quai in bateau['position']:
            if pos==quai:
                return flotte.index(bateau) # cependant le tetour est l'index du bateau
    else : return None

def tir(m,paire,flotte):
    a=paire[0]
    b=paire[1] 
    if m[a][b] != VIDE: # si la case n'as pas été attaquer
             return False
    if presence_bateau(paire, flotte): # si il y a un bateau
        bateau_malheureux=flotte[id_bateau_at_pos(paire,flotte)] 
        bateau_malheureux['case touché']+=1 # augmente sont nbr de casetouché
        m[a][b]=TOUCHE # met la case en touché
        if bateau_malheureux['taille']==bateau_malheureux['case touché']: # si tt case détruite
            for coule in bateau_malheureux['position']:
                m [coule[0]] [coule[1]] = DETRUIT  # marque lescase en coulé
            print("")
            print(bateau_malheureux['nom'] , "a été détruit ! Bravo" )
            flotte.pop(id_bateau_at_pos(paire,flotte)) # enlève le bateau
    else :
        m[a][b]=EAU # si ce n'est pas un bateau ==> c'est de l'eau
    return True



def tir_ai_random(m,flotte): 
    while True:
        attack=random_position()
        a=attack[0]
        b=attack[1] 
        if m[a][b] == VIDE:
            tir(m, attack, flotte)
            break
        
def tour_joueur(nom,m,flotte):
    attack=False # tant qu l'attaque n'est pas valide
    while attack==False:
         ordre = input(" Quel coup voulez vous jouer ? ")
         attack=pos_string(ordre,m) 
         if attack != False: # si le format est bon lance l'attaque
             attack=tir(m, attack, flotte)

coup=[better_random_Choice()] #utilisation d'une variable avant pour se souvenir  du coup précédent
    
def tour_ia_better_random(m,flotte):
    attack=coup[0] #analyse coup précédent
    if m[attack[0]][attack[1]]==TOUCHE : # si y a été fructieux
        for i in range(200):
            a= random.randint(1, 2) # chosiie vertical ou horizontale
            if a==1:
                mattack1 = attack[0]+ random.randint(-1, 1) #cherche autout
                mattack2 = attack[1]
            else:
                mattack2 = attack[1]+ random.randint(-1, 1)
                mattack1 = attack[0]
            ordre=(mattack1 ,mattack2) # attribue la attaque a une valeur
            if  -1< mattack1 < 10 and  -1< mattack2 < 10:
                if m[mattack1][mattack2] == VIDE: #verifie que la zone a pas ete attaque
                    tir(m, ordre, flotte)
                    if m[mattack1][mattack2] == TOUCHE :
                        coup[0]=ordre
                    return " "
            if i >198: # dans certain cas le programme peut se bloquer
                coup[0]=random_position()
# h5
    # sile coup précedent n'as pas été  bon mais qu'il  reste des point découvert
    #☺uyilité si le bateau a été remonter mais pas du début évite de refaire toute les case 
    for l in range(len(m)):
        for i in range(len(m[l])):
            if m[l][i]== TOUCHE :
                #regarde s'il y a une case découvrte 
                for v in range(200): #attaque autour     
                    a= random.randint(1, 2) #choice aléatoire d'une ligne ou cologne
                    if a==1: 
                        mattack1 = l + int(random.choice([-1,1])) #varie selon le paramètre 
                        mattack2 = i 
                    else:
                        mattack2 = i + int(random.choice([-1,1]))
                        mattack1 = l
                    ordre=(mattack1 ,mattack2)
                    if ( -1< mattack1 < 10 and  -1< mattack2 < 10) and tir(m, ordre, flotte) :                  
                        if m[mattack1][mattack2] == TOUCHE :
                            coup[0]=ordre # s'il la ase st toucher retour a case 1
                        return True
                    if v>198:
                        break
                 # dans certain cas le programme peut se bloquer
                #1,3*10^-25  de chance de ne pas toucher la bonne case   
                  #Dans le cas d'un blocage attack a hazard
                  
    # /fin h5              
            
    if True: 
        while True: #dans le cas normal ne vas attack au hazard 
            attack=better_random_Choice() #version probabliste
            a=attack[0]
            b=attack[1] 
            if m[a][b] == VIDE:
                tir(m, attack, flotte)        
                return ""


def test_fin_partie(nom,flotte,nbtour,m):
    if flotte==[]:
        plot_grid(m) # affiche la grill gagner [ rajouter]
        print(nom ," a gagner la L'escarmouche ! Bravo")
        print( nbtour ," ont été necessaire affin d'arriver a cette victoire")
        for i in range(6): # timer de 60s avant de clore le programme
            print(" Fin du programme dans ",60-i*10 ," seconde")
            time.sleep(10)
        os._exit(0)

def init_joueur():
    flotte=[]
    m=create_grid()
    for i in range(len(NOMS)): # pur chaque bateau
        show_grid(m, flotte) # montre le bateau poser
        ajout_bateau(flotte, NOMS[i],TAILLES[i]) # permet de l'ajouter
        
    return[m,flotte] #utilise un liste pour stoquer les information

def int_ai():
    flotte=[] # soit une flotte vide 
    m=create_grid()
    for i in range(len(TAILLES)): #Pour chaque bateau
        bateau_poser=False
        while bateau_poser==False: #tante de les mettres su rdes position aléatoire sinon
            bateau_poser=nouveau_bateau(flotte, NOMS[i],TAILLES[i],random_position(), random.choice(['hhh','vvv']))
    return [m,flotte]
    
def Joueurs_vs_ia():
    dr_no=int_ai()
    zone_mechante=dr_no[0]
    flotte_mechante=dr_no[1]
    mr_bond=init_joueur()
    zone_Mi6=mr_bond[0]
    flotte_angletterre=mr_bond[1]
    nbtour=0
    nom=input("Quel votre nom : ")
    while True:
        
        plot_grid(zone_Mi6)
        plot_grid(zone_mechante)
        tour_joueur(nom, zone_mechante , flotte_mechante)
        
        test_fin_partie(nom,flotte_mechante, nbtour, zone_mechante)
        tour_ia_better_random(zone_Mi6, flotte_angletterre)
        test_fin_partie("Dr No ", flotte_angletterre, nbtour, zone_Mi6)
        nbtour+=1

def deux_joueurs():
    nom_joueur1=input("entrez le nom du joueur 1 ")
    nom_joueur2=input("entrez le nom du joueur 2 ")
    #initialisation joueur 1
    print("initialisation "+""+ nom_joueur1)
    var_j1=init_joueur()
    m1=var_j1[0]
    flotte1=var_j1[1]
    hide()
    #initialisation joueur 2
    print(" initialisation " + nom_joueur2)
    var_j2=init_joueur()
    m2=var_j2[0]
    flotte2=var_j2[1]
    hide()
    nbtour=0
    while(True):

        #tour joueur 1
        print("Tour de "+ nom_joueur1)
        plot_grid(m2)
        tour_joueur(nom_joueur1,m2,flotte2)
        print(flotte2)
        test_fin_partie(nom_joueur1, flotte2, nbtour, m2)
        #tour joueur 2

        print("Tour de "+ nom_joueur2)
        plot_grid(m1)
        tour_joueur(nom_joueur2,m1,flotte1)
        test_fin_partie(nom_joueur2, flotte1, nbtour, m1)
        nbtour+=1

def hide():
    for i in range(180):
        print("")        
        





#PArtie 5
grill=[[0 for i in range(N)]for x in range(N)]



def ia():
    dr_no=int_ai()
    zone_mechante=dr_no[0]
    flotte_mechante=dr_no[1]
    nbtour=0
    while True:
        tour_ia_better_random(zone_mechante , flotte_mechante)
        time.sleep(0.25)
        plot_grid(zone_mechante)
        if flotte_mechante==[]:
            break
        nbtour+=1
    return nbtour

    
#Valeur=[[1282, 2252, 2837, 3162, 3358, 3266, 3191, 2890, 2203, 1322], [2372, 3291, 3884, 4226, 4340, 4427, 4281, 3945, 3436, 2212], [2899, 3976, 4453, 4853, 4799, 4916, 4780, 4448, 4061, 2711], [3335, 4259, 4669, 4945, 5169, 4997, 4751, 4615, 4295, 3008], [3294, 4391, 4924, 5068, 5353, 5280, 4853, 4954, 4523, 3356], [3324, 4318, 4913, 5040, 5063, 5160, 4786, 4971, 4561, 3300], [3114, 4135, 4842, 4621, 5018, 5217, 4897, 4752, 4369, 3130], [2832, 3731, 4485, 4520, 4707, 4853, 4750, 4593, 4174, 2957], [2342, 3326, 4067, 4247, 4251, 4329, 4316, 3892, 3422, 2340], [1424, 2297, 2991, 3157, 3181, 3190, 3115, 2692, 2209, 1304]]
# Nombre de fois qu'n bateau a ete prsence sur la case pour un echantillons de 10 k parties
# 30 mn de traitement
# d'un le stockage sous forme de valeur ==> évite retraitement 



# for l in Valeur:
#     for i in range(len(l)):
#         l[i]/=387965
##calcule pour connaitre la fréquence d'apparition de chaque bateau    
# plot_grid(Valeur)  
#poid =[[0.00330442790625443, 0.005804647326434086, 0.007312515304215586, 0.00815021973631642, 0.008655419947675692, 0.008418285154588687, 0.008224968747180803, 0.007449125565450492, 0.005678347273594267, 0.003407523874576315], [0.006113953578286701, 0.008482723957057983, 0.010011212351629658, 0.010892735169409612, 0.011186576108669596, 0.011410823141262743, 0.01103450053484206, 0.010168443029654736, 0.008856469011379892, 0.005701545242483214], [0.007472323534339438, 0.010248347144716662, 0.011477839495830809, 0.012508860335339529, 0.012369672522005852, 0.012671246117562152, 0.012320699032129187, 0.01146495173533695, 0.010467439073112265, 0.00698774373977034], [0.008596136249403941, 0.01097779438866908, 0.012034590749165517, 0.012745995128426533, 0.013323366798551416, 0.012880027837562667, 0.012245950021264804, 0.01189540293583184, 0.011070586264224866, 0.007753276713105563], [0.008490456613354297, 0.011318031265706957, 0.012691866534352326, 0.013063034036575464, 0.013797636384725425, 0.013609475081515086, 0.012508860335339529, 0.01276919309731548, 0.011658268142744834, 0.008650264843478148], [0.008567783176317451, 0.011129869962496618, 0.012663513461265836, 0.012990862577809854, 0.013050146276081606, 0.01330016882966247, 0.012336164344721817, 0.0128130114829946, 0.011756215122498163, 0.008505921925946928], [0.008026497235575374, 0.010658177928421378, 0.012480507262253039, 0.011910868248424472, 0.012934156431636874, 0.013447089299292461, 0.012622272627685487, 0.012248527573363577, 0.011261325119533979, 0.008067738069155722], [0.007299627543721728, 0.009616846880517572, 0.011560321162991508, 0.01165053548644852, 0.012132537728918846, 0.012508860335339529, 0.012243372469166033, 0.01183869678965886, 0.010758702460273478, 0.007621821556068202], [0.006036627015323547, 0.008572938280514995, 0.010482904385704896, 0.010946863763483819, 0.010957173971878906, 0.011158223035583106, 0.011124714858299073, 0.010031832768419832, 0.008820383281997088, 0.006031471911126004], [0.003670434188651038, 0.005920637170878817, 0.007709458327426443, 0.008137331975822561, 0.008199193226193084, 0.008222391195082031, 0.008029074787674145, 0.0069387702498936756, 0.005693812586186898, 0.0033611279367984225]]
#Population=([[(x,i) for i in range(N)]for x in range(N)])   
       
#teste du nombre de coup moyen de 
def auto():
    summ=0
    for i in range(1000):
        summ+=ia()
        print(summ)
    
# 84 coup moyenne random ancien 
# 64 coup moyen better random
# 63 coup avec la version améliorer  
# 60 avec version ameliorer + approche proba de l'aléatoire 


couleur= input(" Voulez vous le jeux en couleur taper c sinon taper sur entrer : ")
if (couleur == "c"):
        BLANC = '\033[0m'
        VIDE = '\033[0m'+'.'
        EAU='\033[34m'+'o'
        TOUCHE= '\33[35m' +'x'  
        BATEAU= '\033[32m'+'#'
        DETRUIT='\033[33m'+'@'
        DECALGE=1



while True:
    print("Taper 1 pour Joueur contre un ai ou Taper 2 pour 2 joueur ou 3 pour le mode automatique " )
    rep=input(" Que voulez vous faire ")
    if rep=="1":
        print("Intilisation joueur : rentrez vos position")
        Joueurs_vs_ia()
    elif rep=="2":
        deux_joueurs()
    elif rep=="3":
        auto()
    else :
        hide()
        print("Erreur verifier le Format : 1 , 2 ou 3")
        print("")