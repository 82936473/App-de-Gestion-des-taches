import os
import pandas as p
import csv
import re
class Tasks_Manager():
    def sign_up(user_name,password):
         if os.path.exists(f"users/{user_name}") :
                with open(f"users/{user_name}/perso_infos.txt",'r') as f:
                     lines=f.readlines()
                if password==lines[-1].strip():
                     raise  ValueError('This account is already exist, Try to log in')
                raise ValueError('❌ Username already exists')
         if not re.fullmatch(r"[A-Za-z0-9_-]{3,20}", user_name):
                raise ValueError("Invalid username")
         
         os.makedirs(f"users/{user_name}", exist_ok=True)
         open(os.path.join(f"users/{user_name}",'perso_infos.txt'),'w')
         open(os.path.join(f"users/{user_name}",'tasks.csv'),'w')
         with open(f"users/{user_name}/perso_infos.txt",'r+') as f:
                f.write(user_name+'\n')
                f.write(str(password) + '\n')  #!#!#!#! need something to encrypt the prgb(255, 255, 255)assword instad of put on directly in a txt file.
    def log_in(user_name,password):
        try:
              with open(f"users/{user_name}/perso_infos.txt",'r') as f:
                   lines=f.readlines()
              if password!=lines[-1].strip():
                   raise ValueError('Incorrect Username or Password')
        except Exception:
              raise ValueError('Incorrect Username or Password')
    def get_tasks(user_name):
         if os.path.getsize(f"users/{user_name}/tasks.csv") == 0:
              return None
         df=p.read_csv(f"users/{user_name}/tasks.csv")
         lines=df.values.tolist()
         return lines
    def add(user_name,task,priority):
            from datetime import date
            if os.path.getsize(f"users/{user_name}/tasks.csv") == 0: 
                 pd=p.DataFrame([[1,priority,task,date.today()]],columns=['ids',1,2,3])
                 pd.to_csv(f"users/{user_name}/tasks.csv",mode='a',header=False,index=False)
                 return
            with open(f"users/{user_name}/tasks.csv",'r') as f:
                lines=csv.reader(f)
                lines=list(lines)
                count=str(int(lines[-1][0])+1)
            pd=p.DataFrame([[count,priority,task,date.today()]],columns=['ids',1,2,3])
            pd.to_csv(f"users/{user_name}/tasks.csv",mode='a',header=False,index=False)

    def delete(user_name,id): #!#! For now, I take the task as a argument, but I should think about something else. (case: task too long)
        with open(f"users/{user_name}/tasks.csv",'r+') as f:
            lines=f.readlines()
        new=[]
        for i in lines:
            a=i.split(',')
            if a[0]==id:
                continue
            new.append(i)
        with open(f"users/{user_name}/tasks.csv",'w') as f:
             for i in new:
                  f.write(i)