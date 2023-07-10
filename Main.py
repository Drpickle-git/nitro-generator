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

print(gris, "Vérification du node.js en cours...")
time.sleep(3)
print(gris, "Téléchargement des paquets en cours...")
time.sleep(4)
print(vert, "Téléchargement terminé !")
time.sleep(2)
print(vert, "Démarrage du processus de vérification en cours...")
time.sleep(3)
print(vert, "Vérification de l'utilisateur en cours...")
time.sleep(5)
print(vert, "Utilisateur vérifié !")
time.sleep(2)
print(bleu_foncé, "Fermeture du node.js en cours...")
time.sleep(5)
print(bleu, "Génération des codes en cours...")
time.sleep(6)

num = input("Combien de codes souhaitez-vous vérifier ? ")

f = open("Nitro Codes.txt", "w", encoding='utf-8')

print(gris, "Pinging node.js... ")
time.sleep(3)
print(gris, 'Téléchargement des paquets...')
time.sleep(4)
print(vert, "Téléchargés !")
time.sleep(2)
print(vert, 'Démarrage du processus de vérification.')
time.sleep(3)
print(vert, 'Vérification de l\'utilisateur...')
time.sleep(5)
print(vert, "Utilisateur humain !")
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

# Vérification des codes
with open("codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(vert, " VALIDE | {} ".format(line.strip("\n")))
            break
        else:
            print(bleu_foncé, " INVALIDE | {} ".format(line.strip("\n")))

input("Fin de la génération ! J'espère que vous avez trouvé un Nitro ! Appuyez sur Entrée 5 fois ou exécutez à nouveau pour fermer le programme.")
input("4")
input("3")
input("2")
input("1")
