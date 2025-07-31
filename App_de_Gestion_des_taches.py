import os
import time
t=time
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
            os.makedirs(nom_utili)
            open(os.path.join(nom_utili,'perso_infos'),'w')
            open(os.path.join(nom_utili,'taches'),'w')
            open(os.path.join(nom_utili,'corbeille'),'w')
            with open(f"{nom_utili}/perso_infos",'r+') as f:
                f.write(code)
            print('Compte enregistre👍.')  
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
            if os.path.exists(nom_utili):
                print("ce nom d'utilisateur est deja existant. Veuillez saisir un autre.")
                print('...')
                t.sleep(1.5)
                clear()
                start()
            else:
                codde() 

    elif choic_input == "2":
        print('----Connexion----')
        alre_nom_utili = input("Entrer votre nom d'utilisateur : ")
        alre_code = input("Mot de passe : ")
        if os.path.isdir(alre_nom_utili) :
            with open(f"{alre_nom_utili}/perso_infos",'r+') as f:
                line=f.readline()
                if alre_code==line:
                    print('Entree reussi👍.')
                    print('...')
                    t.sleep(1)
                    clear()
                    general()
                else:
                    print("Mot de passe incorrect.")
                    t.sleep(0.5)
                    clear()
                    start()

        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            t.sleep(1)
            clear()
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
    if os.path.getsize(f"{nom_utili}/taches")==0:
        print("Vous n'avez pas de taches.")
        print("...")
        t.sleep(1.5)
        clear()
        general()
    else:
        print("\nVotre taches :")
        with open(f"{nom_utili}/taches",'r+') as f:
            lines=f.readlines()
            for ind,i in enumerate(lines,1):
                print(f"{ind} : {i}")
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
                with open(f"{nom_utili}/taches",'r+') as f:
                    for i in taches:
                        f.write(i+'\n')
                print("les taches sont ajoutees avec succèes")

                print('...')
                t.sleep(1)
                clear()
                general()
            taches.append(tache)
def supprimer():
    voir()
    with open(f"{nom_utili}/taches",'r+') as f:
        lines=f.readlines()
    try:
        index = input("choisir l'incide du tache a supprimer, ou entrer 'N' pour anuler : ")
        if index.lower()=='n':
            print('Action anuulee.')
            t.sleep(1)
            general()
        else:
            index_int=int(index)
            index_int-=1
            supp=lines.pop(index_int)
            with open(f"{nom_utili}/taches",'w+') as f:
                for i in lines:
                    f.write(i)
            with open(f"{nom_utili}/corbeille",'r+') as f:
                f.seek(0,2)
                f.write(supp)
            print(f"la tache {index} est supprimer")
            t.sleep(1.5)
            clear()
    except IndexError:
        print("Invalide entre, veuillez entrer un indice existant")
        t.sleep(2)
        supprimer()
def courbeille():
    clear()
    if  os.path.getsize(f"{nom_utili}/corbeille")==0:
        print(" la courbeille est vide.")
        t.sleep(0.5)
        clear()
        general()
    print("Les taches recement supprimer : ")
    with open(f"{nom_utili}/corbeille",'r+') as f:
        lines=f.readlines()
    for indice,i in enumerate(lines,1):
        if i !=0:
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
        choix=input("Vous voulez supprimer la tache (1), cette tache ou la restorer (2) : ")
        if choix=='1':
            choi_def=input("cette tache sera supprimer definitivement, Etes vous sure(O/N) :")
            if choi_def.lower()=='o' or choi_def=='0':
                lines.pop(index_int)
                with open(f"{nom_utili}/corbeille",'w+') as f:
                    for i in lines:
                        f.write(i)
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
            with open(f"{nom_utili}/taches",'a+') as f:
                f.write(lines[index_int])
            lines.pop(index_int)
            with open(f"{nom_utili}/corbeille",'w+') as f:
                for i in lines:
                    f.write(i)
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

