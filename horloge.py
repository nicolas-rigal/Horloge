import time

# https://www.pierre-giraud.com/python-apprendre-programmer-cours/module-datetime-time-calendar/#:~:text=La%20fonction%20time()%20renvoie,00%3A00%20(UTC). 
#----------------------------------------------------------#
#       initialisation de mes variable de parametre        #
#                recuperation nom du user                  #
#        et fonction de verification format 12/24          #
#----------------------------------------------------------#
#-%H	Heure (horloge sur 24 heures) sous forme de nombre décimal [00,23].
#-%M	Minutes sous forme décimale [00,59].
#-%S	Deuxième sous forme de nombre décimal [00,61].

minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))
# permet de vérifier si l'alarme a été initialisée ou non
alarm_heure = -1 
alarm_minute = -1
alarm_second = -1.0
alarm_on = False
format_time = "24"

# input de initialisation de l'heure, minute, seconde
def afficher_heure():
    global heure, minute, second
    heure = int(input("Voyez pararametre une heure pour initialiser votre horloge  :")) 
    minute = int(input("Voyez pararametre une minutes pour initialiser votre horloge : "))
    second = int(input("Voyez pararametre une second pour initialiser votre horloge : "))
    
# input de initialisation de l'heure, minute, seconde pour l'alarme 
def set_alarm():
    global alarm_heure, alarm_minute, alarm_second, alarm_on
    alarm_heure = int(input("Voyez pararametre une heure pour votre alarme :"))
    alarm_minute = int(input("Voyez pararametre une minutes pour votre alarme :"))
    alarm_second = int(input("Voyez pararametre une second pour votre alarme :"))
    alarm_on = True

# fonctiond deselection du format de l'heure
def set_format_time():
    global format_time
    format_time = input("Quel format souhaitez vous ? (12 or 24) : ")
    if format_time != "12" and format_time != "24":
        format_time = input("Quel format souhaitez vous ? (12 or 24) : ")
    


# appele de mes fonction input avec user 
afficher_heure()
set_alarm()
set_format_time()


#----------------------------------------------------------#
#               initialisation de ma boucle                #
#         verification du format si 12 selectionner        #
#      fonctionement analogique d'un horloge clasique      #
#      fonctionement analogique d'un horloge clasique      #
#----------------------------------------------------------#

while True:
    if format_time == "12" and heure < 12:
        if heure == 0:
            heure = 12
#\r permet d'actualiser l'horloge
            print("\r%02d:%02d:%02d AM" % (heure, minute, second), end="")
        elif format_time == "12" and heure > 12:
            heure -= 12
            print("\r%02d:%02d:%02d PM" % (heure, minute, second), end="")
    if format_time == "24":
        print("\r%02d:%02d:%02d" % (heure, minute, second), end="")
    print("\r%02d:%02d:%02d" % (heure, minute, second), end="")

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
        heure = 0
    if alarm_on:
        # permet de vérifier les conditions qui vont permettre à l'alarme de s'activer
        if heure == alarm_heure or heure == alarm_heure - 12 and minute == alarm_minute and second == alarm_second:
            print("\nJesse wake up ! I don't like this! Jesse Wake up! Hello 👨‍🦱🤘🎸🎲")
            alarm_on = False
            if alarm_heure > 12:
                print("\r%02d:%02d:%02d PM" % (heure, minute, second), end="")
            else:
                print("\r%02d:%02d:%02d AM" % (heure, minute, second), end="")

