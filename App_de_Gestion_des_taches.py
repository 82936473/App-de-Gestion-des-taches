import time
t=time
comptes={}
codes={}
corbeille={}
nom_utili = '' 
code = '' 
def clear():
    from os import name,system
    system('cls' if name == 'nt' else 'clear')
    print('\n', f"{" <'TACHER'> ":-^50}")
clear()
def codde():
         global code
         code = input("Creer un mot de passe : ")
         veerification = input('Verifier le mot de passe : ')
         if veerification==code:
            codes[nom_utili]=code

            print('Compte enregistre👍.')  
            comptes[nom_utili]=''
            corbeille[nom_utili]=[]
            print("...")
            t.sleep(1.5)
            clear()
            start()
         else:
            print('mot de passe incorrect ')
            codde()
def start():
    global alre_code, alre_nom_utili,nom_utili 

    choic_input = input("\nTu veux creer un nouveau compte (1) ou vous avez deja un (2)? ")

    if choic_input == "1":
        while True:
            nom_utili = input("Entrer un nom d'utilisateur : ")
            if nom_utili in comptes:
                print("ce nom d'utilisateur est deja existant. Veuillez saisir un autre.")
                print('...')
                t.sleep(1.5)
                clear()
                start()
            else:
                codde() 

    elif choic_input == "2":
        if not nom_utili and not code: # verification si la valeur est initiale 
            print("Aucun compte n'a été créé. Veuillez d'abord créer un compte.")
            print('...')
            t.sleep(2.5)
            clear()
            start() 
        print('----Connexion----')
        alre_nom_utili = input("Entrer votre nom d'utilisateur : ")
        alre_code = input("Mot de passe : ")
        if alre_nom_utili in codes:
            if alre_nom_utili in codes.keys() and alre_code==codes[alre_nom_utili] :
                print('Entree reussi👍.')
                print('...')
                t.sleep(1)
                clear()
                general()
            else:
                print("Nom d'utilisateur ou mot de passe incorrect.")
                start()
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            start()
    else:
        print("Choix invalide.")
        print('...')
        t.sleep(1)
        clear()
        start()
#! la deuxieme tache du code:👇
def menu():
    print("(1) Voir tes taches.")
    print("(2) Ajouter une tache.")
    print("(3) Supprimer une tache.")
    print("(4) La corbeille.")
    print("(5) Quitter.")
def voir():
    clear()
    if not comptes[alre_nom_utili]:
        print("Vous n'avez pas de taches.")
        print("...")
        t.sleep(1.5)
        general()
    else:
        print("\nVotre taches :")
        for index , tache in enumerate(comptes[alre_nom_utili],1):
            print(f"{index}: {tache}")        
            t.sleep(0.4)                   
def ajouter():
        print("Entrer vos taches, cliquer entrer pour passer a la tache suivante entrer 'Fin' pour finir l'ajout de taches.")
        taches=[]
        while True:
            tache = input(" >>> ")
            if tache.lower()=='fin':
                if not taches:
                    print('aucun tache ajouter')
                    t.sleep(1)
                    clear()
                    break
                print("les taches sont ajoutees avec succèes")
                if not comptes[alre_nom_utili]:
                    comptes[alre_nom_utili]=taches
                else:
                    for i in taches:
                        comptes[alre_nom_utili].append(i)
                print('...')
                t.sleep(1)
                clear()
                general()
            taches.append(tache)
def supprimer(): 
    voir()
    try:
        index = input("choisir l'incide du tache a supprimer, ou entrer 'N' pour anuler : ")
        if index.lower()=='n':
            print('Action anuulee.')
            t.sleep(1)
            general()
        else:
            cour=[]
            index_int=int(index)
            index_int-=1
            supp=comptes[alre_nom_utili].pop(index_int)

            corbeille[alre_nom_utili].append(supp)
            print(f"la tache {index} est supprimer")
            t.sleep(1.5)
            clear()
    except IndexError:
        print("Invalide entre, veuillez entrer un indice existant")
        t.sleep(2)
        supprimer()
def courbeille():
    clear()
    if  not corbeille[alre_nom_utili]:
        print("Aucun element dans la courbeille.")
        t.sleep(0.5)
        clear()
        general()
    print("Les taches recement supprimer : ")
    for indice,i in enumerate(corbeille[alre_nom_utili],1):
        print(f"{indice} : {i}")
        t.sleep(0.4)
    index=input("choisir un indice, entrer 'N' pour annuler l'action : ")
    if index.lower()=='n':
        print("Action annulee.")
        t.sleep(0.4)
        clear()
        general()
    try:
        index_int=int(index)
        index_int-=1
        choix=input("Vous voulez supprimer(1), cette tache ou la restorer(2) : ")
        if choix=='1':
            choi_def=input("cette tache sera supprimer definitivement, Etes vous sure(O/N) :")
            if choi_def.lower()=='o' or choi_def=='0':
                corbeille[alre_nom_utili].pop(index_int)
                print("👍")
                t.sleep(0.4)
                clear()
            elif choi_def.lower()=='n':
                print("Action annule.")
                t.sleep(0.4)
                clear()
                general()
            else:
                print("choix invalide.")
                courbeille()
        elif choix=='2':
            comptes[alre_nom_utili].append(corbeille[alre_nom_utili][index_int])
            corbeille[alre_nom_utili].pop(index_int)
            print('👍')
            t.sleep(0.4)
            clear()
    except:
        print("Choix invalide.")
        t.sleep(0.4)
        clear()
        courbeille()


def general():
    while True:
        print("\nchoisir une option : " )
        menu()
        choix = input(">>> ")
        if choix == '1':
            print('Prossus...')
            t.sleep(0.5)
            voir()
        elif choix == '2':
            ajouter()
        elif choix == '3':
            supprimer()
        elif choix == '4':
            courbeille()
        elif choix == '5':
            clear()
            start()
        else:
            print("\ninvalide choix, choisir un nombre existant dans la liste.")
            t.sleep(1)
            clear()
start()

