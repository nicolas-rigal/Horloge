import time

def afficher_heure():
    global heure, minute, second
    heure = int(input("Veuillez entrer l'heure pour initialiser votre horloge :"))
    minute = int(input("Veuillez entrer les minutes pour initialiser votre horloge : "))
    second = int(input("Veuillez entrer les secondes pour initialiser votre horloge : "))

def activation_alarm():
    global alarm_on
    alarm_on = input("Voulez-vous activer une alarme ? (oui/non) : ")
    if alarm_on.lower() == "oui":
        alarm_on = True
    else :
        alarm_on = False
        
def alarme_setting():
    if alarm_on == True:
        global alarm_heure, alarm_minute, alarm_second
        alarm_heure = int(input("Veuillez entrer l'heure pour votre alarme :"))
        alarm_minute = int(input("Veuillez entrer les minutes pour votre alarme :"))
        alarm_second = int(input("Veuillez entrer les secondes pour votre alarme :"))

def choisir_mode():
    global mode_24h
    mode_24h = input("Veuillez choisir le mode d'affichage de l'heure  (12/24) : ")
    if mode_24h == "12":
        mode_24h = False
    else:
        mode_24h = True

# initialisation de l'heure 
afficher_heure()
# activation de l'alarme 
activation_alarm()
# initialisation de l'alarme 
alarme_setting()
# choix du mode d'affichage de l'heure
choisir_mode()

while True:
    if alarm_on == True:
        if heure == alarm_heure and minute == alarm_minute and second == alarm_second:
            print("\nJesse wake up! I don't like this! Jesse Wake up! Hello 👨‍🦱🤘🎸🎲")
    if mode_24h:
        print("\r%02d:%02d:%02d" % (heure, minute, second), end="")
    else:
        if heure < 12:
            print("\r%02d:%02d:%02d AM" % (heure, minute, second), end="")
        elif heure == 12:
            print("\r%02d:%02d:%02d PM" % (heure, minute, second), end="")
        else:
            print("\r%02d:%02d:%02d PM" % (heure-12, minute, second), end="")
    time.sleep(1)
    second += 1
    # fonctionnement d'une horloge classique 
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        heure += 1
    if heure == 24:
        heure = 00
