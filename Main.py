bleu = "\33[0;34m"
cyan = "\033[1;36m"
violet = "\033[0;35m"
vert = "\033[0;32m"
orange = "\033[0;33m"
rose = "\033[1;31m"
bleu_foncé = "\033[1;34m"
blanc = "\033[1;37m"
gris = "\033[1;30m"
rouge = "\033[0;31;47m"

import time
import random
import string
import webbrowser
import requests
import random

#La vérification n'est pas réele, je trouvait juste ca cool. 
print(gris, "Vérification du node.js en cours..")
print(" ")
time.sleep(3)
print(gris, "Téléchargement des paquets en cours..")
print(" ")
time.sleep(4)
print(vert, "Téléchargement terminé !")
print(" ")
time.sleep(2)
print(vert, "Démarrage du processus de vérification en cours..")
print(" ")
time.sleep(3)
print(vert, "Vérification de l'utilisateur en cours")
print(" ")
time.sleep(5)
print(vert, "Utilisateur vérifié !")
print(" ")
print("Promis Le reste n'est pas long :) ")
print(" ")
time.sleep(2)
print(bleu_foncé, "Fermeture du node.js en cours..")
print(" ")
time.sleep(5)
print(bleu, "Ouverture du logiciel en cours..")
print(" ")
time.sleep(6)

banner = """
 _   _  _____  _____ ______  _____          _____  _____  _   _  _____ ______   ___   _____  _____ ______
| \ | ||_   _||_   _|| ___ \|  _  |        |  __ \|  ___|| \ | ||  ___|| ___ \ / _ \ |_   _||  _  || ___ \
|  \| |  | |    | |  | |_/ /| | | | ______ | |  \/| |__  |  \| || |__  | |_/ // /_\ \  | |  | | | || |_/ /
| . ` |  | |    | |  |    / | | | ||______|| | __ |  __| | . ` ||  __| |    / |  _  |  | |  | | | ||    /
| |\  | _| |_   | |  | |\ \ \ \_/ /        | |_\ \| |___ | |\  || |___ | |\ \ | | | |  | |  \ \_/ /| |\ \
\_| \_/ \___/   \_/  \_| \_| \___/          \____/\____/ \_| \_/\____/ \_| \_|\_| |_/  \_/   \___/ \_| \_|
                                                                                                          
""".format(random.choice([bleu_foncé, vert, orange]))

#print(banner)
print(" _   _  _____  _____ ______  _____          _____  _____  _   _  _____ ______   ___   _____  _____ ______  ")
print("| \ | ||_   _||_   _|| ___ \|  _  |        |  __ \|  ___|| \ | ||  ___|| ___ \ / _ \ |_   _||  _  || ___ \ ")
print("|  \| |  | |    | |  | |_/ /| | | | ______ | |  \/| |__  |  \| || |__  | |_/ // /_\ \  | |  | | | || |_/ / ")
print("| . ` |  | |    | |  |    / | | | ||______|| | __ |  __| | . ` ||  __| |    / |  _  |  | |  | | | ||    /  ")
print("| |\  | _| |_   | |  | |\ \ \ \_/ /        | |_\ \| |___ | |\  || |___ | |\ \ | | | |  | |  \ \_/ /| |\ \  ")
print("\_| \_/ \___/   \_/  \_| \_| \___/          \____/\____/ \_| \_/\____/ \_| \_|\_| |_/  \_/   \___/ \_| \_| ")

print(" ")

num = input("Combien de codes souhaitez-vous vérifier ? ")

f = open("Nitro Codes .txt", "w", encoding='utf-8')

print(gris, "Ouverture de node.js... ")
time.sleep(3)
print(gris, 'Téléchargement des paquets...')
print(" ")
print(" ####- - - - - - 40 Pourcents...")
time.sleep(2)
print(" ######## - - 80 Pourcents...")
time.sleep(4)
print(vert, "Paquets Téléchargés !")
time.sleep(2)
print(bleu_foncé, 'Fermeture du node.js')
time.sleep(5)
print(bleu, "Génération des codes en cours...")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

with open("Nitro codes .txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(vert, " VALIDE | {} ".format(line.strip("\n")))
            break
        else:
            print(bleu_foncé, " INVALIDE | {} ".format(line.strip("\n")))

input("Fin de la génération ! J'espère que vous avez trouvé un Nitro ! Appuyez sur Entrée 2 fois ou exécutez à nouveau pour fermer le programme.")
input("2")
input("1")
