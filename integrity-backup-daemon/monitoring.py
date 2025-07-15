import os
import random
import sys
import utils
import shutil
import logging
from datetime import datetime, time

# Creaza folderul de logs in cazul in care acesta nu exista
os.makedirs("logs", exist_ok=True)

log_path = os.path.join("logs", "monitoring.log")

# Configurare logging pentru consola si log file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path, mode='a'),
        logging.StreamHandler()
    ]
)

watch_folder = sys.argv[1]

# Creaza o lista cu numele fisierelor din folder-ul pasat ca argument
my_files = os.listdir(watch_folder) 

# Lista pentru a compara valorile hash actuale cu cele precedente 
old_hash_list = [] 

# Fisierul unde vor fi salvate toate hash-urile
hash_file = "hashes.txt" 

# Creaza folderul de backup, secured, in cazul in care acesta nu exista
os.makedirs("secured", exist_ok=True) 

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Salvam hash-urile initiale in fisierul hashes.txt pentru a putea compara ulterior daca fisierele au fost modificate
with open(hash_file, "w") as f:
    for file in my_files:
        
        nume, extensie = os.path.splitext(file) # Salvam numele fisierului si extensia sa
        source_path = os.path.join(watch_folder, file) # Calea spre fisierul caruia ii calculam hash-ul

        if os.path.isfile(source_path):
            f.write(utils.hashing_function(source_path) + "\n")
        
# Citim hash-urile initiale si creem lista pentru comparare cu posibilele hash-urile noi
with open(hash_file, "r") as f:
    old_hash_list = [line.strip() for line in f.readlines()]

# Reiteram lista de fisiere din folderul de interes pentru a vedea daca hash-ul vreunui fisier s-a schimbat
for file in my_files:
    nume, extensie = os.path.splitext(file) # Salvam numele fisierului si extensia sa
    source_path = os.path.join(watch_folder, file) # Calea spre fisierul caruia ii calculam hash-ul

    # Genereaza un nou hash pentru comparare
    actual_hash = utils.hashing_function(source_path)

    locked_path = source_path + ".lock"
    backup_path = os.path.join("secured", nume + "-" + timestamp)
    
    if actual_hash not in old_hash_list:
        
        try:
            os.rename(source_path, locked_path)
            shutil.copy2(locked_path, backup_path)
            
            time.sleep(random.randint(1, 5))

            logging.info("General info - Backup completed for file: %s", file)
            os.rename(locked_path,source_path)

        except Exception as e:
            logging.error("An error happend! %s: %s", file, str(e))

        
        

    
        
            

