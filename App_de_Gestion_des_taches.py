from datetime import date
import ast
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
#! Creating a Password and create a account file 
def codde():
         global code
         code = input("create a password : ")
         if len(code)==0:
             print('invalid password. Please try again')
             codde()
         veerification = input('verify it : ')
         if veerification==code:
            os.makedirs(nom_utili)
            open(os.path.join(nom_utili,'perso_infos.txt'),'w')
            open(os.path.join(nom_utili,'taches.csv'),'w')
            open(os.path.join(nom_utili,'corbeille.csv'),'w')
            archi(code)
            with open(f"{nom_utili}/perso_infos.txt",'r+') as f:
                for i in liste:
                    f.write(str(i) + '\n')
            print('sign up success.')  
            print("...")
            t.sleep(1.5)
            clear()
            start()
         else:
            print('wrong password.')
            codde()

#! Encrypt the password (Not recommed We should change it)
def archi(code):
    global liste
    liste=[]
    for i in code:
        liste.append(i)

    for ind,i in enumerate(liste):
        i=ord(i)
        liste1=[]
        while True:
            if i==1:
                liste1.reverse()
                liste[ind]=liste1
                break
            if i%2==0:
                i/=2
                liste1.append('P')
            else:
                i=i*3+1
                liste1.append('I')

    for current in liste:
        for i in current:
            a=0
            while a<len(current)-1:
                if 'P' in current[a] and current[a+1] =='P':
                    current[a]=current[a]+current.pop(a+1)
                else:
                    a+=1

    for current in liste:
        for ind,i in enumerate(current):
            if len(i)>1:
                current[ind]=str(len(i))+'P'
            else:
                pass
#! decipher the password (also we should change it)
def desarchi(liste1):
    global chiffree
    chiffree=[]
    for val in liste1:
        chiffre=1
        for i in val:
            if i=='P':
                chiffre=chiffre*2
            elif len(i)>1 :
                chiffre=chiffre*2**int(i[:-1])
            else:
                chiffre=(chiffre-1)//3
        chiffree.append(chiffre)
    for ind,i in enumerate(chiffree):
            chiffree[ind]=chr(i)
    chiffree=''.join(chiffree)

#! Creating new account or log in
def start():
    global alre_code, alre_nom_utili,nom_utili 

    choic_input = input(">>> ")

    if choic_input == "sign up":
        while True:
            nom_utili = input("user name: ")
            if os.path.exists(nom_utili) or len(nom_utili)==0:
                print("This user name is already exist or invalid. please try again.")
            else:
                codde() 

    elif choic_input == "sign in":
        print('---- Signing ----')
        alre_nom_utili = input("user name : ")
        alre_code = input("Password : ")
        if os.path.isdir(alre_nom_utili) :
            liste1=[]
            with open(f"{alre_nom_utili}/perso_infos.txt",'r+') as f:
                for line in f:
                    liste1.append(line.strip())
                for j,i in enumerate(liste1):
                    liste1[j]=ast.literal_eval(i)
                desarchi(liste1)
            if alre_code==chiffree:
                nom_utili=alre_nom_utili
                print('Success.')
                print('...')
                t.sleep(1)
                clear()
                general()
            else:
                print("user name or password is not correct.")
                t.sleep(0.5)
                clear()
                start()

        else:
            print("user name or password is not correct.")
            t.sleep(1)
            clear()
            start()
    elif choic_input=='help':
        help_()
        start()
    elif choic_input=='cls':
        clear()
    else:
        print("invalid input, you should sign in or sign up first. try 'help' to get help")
        print('...')
        start()


#! la deuxieme tache du code:👇

def help_():
    print(''' These are all the commands used in various situations: 
        Before starting:
            sign up         create an account
            sign in         sign in to an existing account
            (The user name and the password can't change currently)   #!#!#!
        In the dashboard (after signing):
            add tasks       to create more tasks
                accepted priority types        high,medium,low
                stop                           stop adding tasks 
            delete task
            recycle bin     enter the recycle bin to delete permanently tasks (use 'delete') or to restore them (use 'restore')
            cls             to clear the terminal
            clear           to clear all tasks
            exit            log out from thee account or to cancel any action
            ''')


#! view the current tasks
def voir():
    clear()
    if os.path.getsize(f"{nom_utili}/taches.csv")==0:
        print("No active tasks.")
        print("...")
        t.sleep(1.5)
        clear()
        general()
    else:
        print("Your tasks :")
        priority=['High:','Medium:','Low:']
        with open(f"{nom_utili}/taches.csv",'r+') as f:
            lines=f.readlines()
            classing=[[],[],[]]
            for i in lines:
                i=i.split(',')
                if i[0]=='High':
                    classing[0].append(f"   [{i[2].replace('\n','')}] - {i[1].replace('$#%^',',')}")
                elif i[0]=='Medium':
                    classing[1].append(f"   [{i[2].replace('\n','')}] - {i[1].replace('$#%^',',')}")
                elif i[0]=='Low':
                    classing[2].append(f"   [{i[2].replace('\n','')}] - {i[1].replace('$#%^',',')}")
            for i in range(3):
                if not len(classing[i])==0:
                    print(priority[i])
                    for i in classing[i]:
                        print(i)
def voir2():
    with open(f"{nom_utili}/taches.csv",'r') as f:
        lines=f.readlines()
        for indice,i in enumerate(lines,1):
                i=i.split(',')
                print(f"{indice} : {i[0]} - {i[1].replace('$#%^',',')} - {i[2]}")
#! Add new tasks and their priority. (We should transform the priority to english later.)
def ajouter():
        print("Enter your tasks, hit enter to pass.")
        taches=[]
        while True:
            tache={'task':None,'priority':None}
            task = input("Task: ")
            if task.lower()=='stop':
                if not taches:
                    print('No tasks added')
                    t.sleep(1)
                    break
                with open(f"{nom_utili}/taches.csv",'a+') as f:
                    for i in taches:
                        f.write(f"{i['priority']},{i['task'].replace(',','$#%^')},{date.today()}\n")
                print("Tasks added correctly")
                print('...')
                t.sleep(1)
                clear()
                general()
            while True:
                priority=input("Priority: ")
                if priority=='high':
                    tache['priority']='High'
                    break
                elif priority=='medium':
                    tache['priority']='Medium'
                    break
                elif priority=='low':
                    tache['priority']='Low'
                    break
                else:
                    print('invalid priority input, try again')
                    t.sleep(1)
            tache['task']=task
            taches.append(tache)
#! remove tasks
def supprimer():
    voir2()
    with open(f"{nom_utili}/taches.csv",'r+') as f:
        lines=f.readlines()
    try:
        index = input("write the index of the task that you want to remove: ")
        if index.lower()=='exit':
            print('action canceled')
            t.sleep(1)
            general()
        else:
            index_int=int(index)
            index_int-=1
            supp=lines.pop(index_int)
            with open(f"{nom_utili}/taches.csv",'w+') as f:
                for i in lines:
                    f.write(i)
            with open(f"{nom_utili}/corbeille.csv",'a+') as f:
                f.seek(0,2)
                f.write(supp)
            print(f"Task {index} deleted")
            t.sleep(1.5)
            clear()
    except IndexError:
        print("invalid input, try again")
        t.sleep(2)
        supprimer()
#! View The trash
def corbeille():
    if  os.path.getsize(f"{nom_utili}/corbeille.csv")==0:
        print("recycle bin empty.")
        t.sleep(0.5)
        clear()
        general()
    with open(f"{nom_utili}/corbeille.csv",'r') as f:
        lines=f.readlines()
    for indice,i in enumerate(lines,1):
            i=i.split(',')
            print(f"{indice} : {i[0]} - {i[1].replace('$#%^',',')} - {i[2]}")
            t.sleep(0.4)
    index=input("Choose an index: ")
    if index.lower()=='exit':
        print("Action canceled")
        t.sleep(0.4)
        clear()
        general()
    try:
        index_int=int(index)-1
        choice=input('>>> ')
        if choice=='delete':
            choi_def=input("This task will be permanently removed, Are you sure (y/n) :")
            if choi_def.lower()=='y':
                lines.pop(index_int)
                with open(f"{nom_utili}/corbeille.txt",'w+') as f:
                    for i in lines:
                        f.write(i)
                print("Done.")
                t.sleep(0.4)
                clear()
            elif choi_def.lower()=='n':
                print("Action canceled")
                t.sleep(0.4)
                clear()
                general()
            elif choi_def=='exit':
                clear()
                general()
            else:
                print("invalid input, try again.")
                corbeille()
        elif choice=='restore':
            with open(f"{nom_utili}/taches.txt",'a+') as f:
                f.write(lines[index_int])
            lines.pop(index_int)
            with open(f"{nom_utili}/corbeille.txt",'w+') as f:
                for i in lines:
                    f.write(i)
            print('Done')
            t.sleep(0.4)
            clear()
    except:
        print("Invalid input, try again.")
        t.sleep(0.4)
        clear()
        corbeille()

#! the main function
def general():
    print(f" ----------- {alre_nom_utili} ----------")
    while True:
        choix = input(">>> ")
        if choix == 'view tasks':
            print('Prossus...')
            t.sleep(0.5)
            voir()
        elif choix == 'add tasks':
            ajouter()
        elif choix == 'delete task':
            supprimer()
        elif choix == 'recycle bin':
            corbeille()
        elif choix == 'exit':
            clear()
            start()
        elif choix=='cls':
            clear()
            print(f"---------- {alre_nom_utili} ----------")
        elif choix=='clear':
            o=input('That will delete all current tasks, are you sure (y,n): ')
            if o=='y':
              open(f"{nom_utili}/taches.txt",'w') 
            elif o=='n':
                print('Action canceled')
                general()
            else:
                print('invalid input, back to dashboard.')
                general()
        elif choix=='help':
            help_()
        else:
            print("invalid input, try again, use help to learn the right  commands.")
            t.sleep(1)
            clear()
start()