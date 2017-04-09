#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# Modules
import os
import sys
import time
import subprocess

# Etats logiciel
etatCamera = 0
etatSysteme = 1

# Variables globales de configuration
cadencement = 0
dureePriseVue = 0
rotation = 0

while (etatCamera != 2):
    print("")
    print("")
    print("")
    print("")
    print("Menu de configuration de la caméra Time-Lapse :")
    print("")
    print("[1]...Cadencement de la caméra [RC]")
    print("[2]...Durée de prise de vues (option) [RC]")
    print("[3]...Rotation de la caméra (option) [RC]")
    print("[4]...Démarrer/Arrêter la caméra [RC]")
    print("[5]...Arrêter le système [RC]")
    print("")

    menu = input("Accéder au menu N° : ")
    try: # On essaye de convertir la chaine de caractères en entier
        menu = int(menu)
        assert menu >= 1 and menu <= 5
    except NameError:
        print("La valeur du menu n'a pas été définie, veuillez réessayer.")
    except TypeError:
        print("La valeur du menu possède un type incompatible, veuillez réessayer.")
    except ValueError:
        print("La valeur du menu n'est pas un nombre valide, veuillez réessayer.")
    except AssertionError:
        print("Le menu saisi est inexistant, veuillez réessayer.")
    else:
        print("")
        print("")


        if menu == 1: # Menu : Cadencement de la caméra
            print("[Cadencement de la caméra]")
            print("")
            print("Cadencement actuel = ", cadencement, "ms")
            etatBoucle = False
            while etatBoucle == False:
                print("")
                cadencementVerif = input("Temps en millisecondes entre chaque cliché (plage comprise entre 10min et 1h) :\n")
                print("")
                try: # On essaye de convertir la chaine de caractères en entier
                    cadencementVerif = int(cadencementVerif)
                    assert cadencementVerif >= 0 and cadencementVerif <= 3600000 # Cadencement compris entre 10min et 1h
                except NameError:
                    print("La valeur du cadencement n'a pas été définie, veuillez réessayer.")
                    etatBoucle = False
                except TypeError:
                    print("La valeur du cadencement possède un type incompatible, veuillez réessayer.")
                    etatBoucle = False
                except ValueError:
                    print("La valeur du cadencement n'est pas un nombre valide, veuillez réessayer.")
                    etatBoucle = False
                except AssertionError:
                    print("Le cadencement saisi n'est pas compris entre 10min et 1h, veuillez réessayer.")
                    etatBoucle = False
                else:
                    cadencement = cadencementVerif
                    etatBoucle = True

        
        elif menu == 2: # Menu : Durée de prise de vues (option)
            print("[Durée de prise de vues]")
            print("")
            print("Durée actuelle = ", dureePriseVue, "ms")
            etatBoucle = False
            while etatBoucle == False:
                print("")
                dureePriseVueVerif = input("Durée de fonctionnement (en ms) de la caméra (0 : en continu) : ")
                print("")
                try: # On essaye de convertir la chaine de caractères en entier
                    dureePriseVueVerif = int(dureePriseVueVerif)
                    assert dureePriseVueVerif >= 0
                except NameError:
                    print("La valeur de la durée n'a pas été définie, veuillez réessayer.")
                    etatBoucle = False
                except TypeError:
                    print("La valeur du durée possède un type incompatible, veuillez réessayer.")
                    etatBoucle = False
                except ValueError:
                    print("La valeur de la durée n'est pas un nombre valide, veuillez réessayer.")
                    etatBoucle = False
                except AssertionError:
                    print("La durée saisie ne doit pas être négative, veuillez réessayer.")
                    etatBoucle = False
                else:
                    dureePriseVue = dureePriseVueVerif
                    etatBoucle = True

                    
        elif menu == 3: # Menu : Rotation de la caméra (option)
            print("[Rotation de la caméra]")
            print("")
            print("Rotation actuelle = ", rotation, "°")
            etatBoucle = False
            while etatBoucle == False:
                print("")
                rotationVerif = input("Effectuer une rotation de 0/90/180/270 degrés :\n")
                print("")
                try: # On essaye de convertir la chaine de caractères en entier
                    rotationVerif = int(rotationVerif)
                    assert rotationVerif == 0 or rotationVerif == 90 or rotationVerif == 180 or rotationVerif == 270
                except NameError:
                    print("La valeur de la rotation n'a pas été définie, veuillez réessayer.")
                    etatBoucle = False
                except TypeError:
                    print("La valeur de la rotation possède un type incompatible, veuillez réessayer.")
                    etatBoucle = False
                except ValueError:
                    print("La valeur de la rotation n'est pas un nombre valide, veuillez réessayer.")
                    etatBoucle = False
                except AssertionError:
                    print("La rotation saisie n'est pas prise en charge, veuillez réessayer.")
                    etatBoucle = False
                else:
                    rotation = rotationVerif
                    print("Prévisualisation de la rotation...")
                    time.sleep(1)
                    subprocess.Popen("raspistill -t 5000 -rot " + str(rotation), stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                    time.sleep(6)
                    print("Prévisualisation de la rotation terminée")
                    time.sleep(1)
                    print("")
                    validerRot = input("Cette configuration vous convient-elle (O : Oui / N : Non) : ")
                    print("")

                    if validerRot:
                        try:
                            assert validerRot == "O" or validerRot == "N"
                        except NameError:
                            print("La valeur de la confirmation n'a pas été définie, veuillez réessayer.")
                            etatBoucle = False
                        except TypeError:
                            print("La valeur de la confirmation possède un type incompatible, veuillez réessayer.")
                            etatBoucle = False
                        except ValueError:
                            print("La valeur de la confirmation n'est pas un nombre valide, veuillez réessayer.")
                            etatBoucle = False
                        except AssertionError:
                            print("La réponse saisie est incorrecte, veuillez réessayer.")
                            etatBoucle = False
                        else:
                            if validerRot == "O":
                                etatBoucle = True

                                
        elif menu == 4:
            # Menu : Démarrage/Arrêt du timelapse
            # Démarrage
            etatCameraVerif = None
            etatBoucle = False
            while etatBoucle == False:
                if etatCamera == 0:
                    print("")
                    etatCameraVerif = input("Voulez-vous démarrer le Time-Lapse (O : Oui / N : Non) : ")
                    print("")
                    try:
                        assert etatCameraVerif == "O" or etatCameraVerif == "N"
                    except NameError:
                        print("La valeur de l'état n'a pas été définie, veuillez réessayer.")
                        etatBoucle = False
                    except TypeError:
                        print("La valeur de l'état possède un type incompatible, veuillez réessayer.")
                        etatBoucle = False
                    except ValueError:
                        print("La valeur de l'état n'est pas un nombre valide, veuillez réessayer.")
                        etatBoucle = False
                    except AssertionError:
                        print("L'état saisi est incorrect, veuillez réessayer.")
                        etatBoucle = False
                    else:
                        if etatCameraVerif == "O":
                            
                            etatCamera = 1
                            print("")
                            print("Lancement du Time-Lapse...")
                            print("")
                            time.sleep(3)
                            subprocess.Popen("sudo mkdir /mnt/clefusb", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                            subprocess.Popen("sudo mount /dev/sda1 /mnt/clefusb", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                            subprocess.Popen("sudo mount /dev/sdb1 /mnt/clefusb", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                            subprocess.Popen("sudo mount /dev/sdc1 /mnt/clefusb", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                            subprocess.Popen("sudo mount /dev/sdd1 /mnt/clefusb", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                            subprocess.Popen("sudo mkdir /mnt/clefusb/timelapse", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                            time.sleep(3)
                            subprocess.Popen("raspistill -t " + str(dureePriseVue) + " -tl " + str(cadencement) + " -o /mnt/clefusb/timelapse/%05d.jpg -q 100 -n -rot " + str(rotation), stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                        etatBoucle = True
                
                # Arrêt   
                if etatCamera == 1:
                    print("")
                    etatCameraVerif = input("Voulez-vous arrêter le Time-Lapse (O : Oui / N : Non) : ")
                    print("")
                    try:
                        assert etatCameraVerif == "O" or etatCameraVerif == "N"
                    except NameError:
                        print("La valeur de l'état n'a pas été définie, veuillez réessayer.")
                        etatBoucle = False
                    except TypeError:
                        print("La valeur de l'état possède un type incompatible, veuillez réessayer.")
                        etatBoucle = False
                    except ValueError:
                        print("La valeur de l'état n'est pas un nombre valide, veuillez réessayer.")
                        etatBoucle = False
                    except AssertionError:
                        print("L'état saisi est incorrect, veuillez réessayer.")
                        etatBoucle = False
                    else:
                        if etatCameraVerif == "O":
                            etatCamera = 0
                        
                        if etatCamera == 0:
                            print("")            
                            print("Arrêt du Time-Lapse...")
                            print("")
                            time.sleep(3)
                        etatBoucle = True
                        
                    
        elif menu == 5: # Arrêter le système
            etatBoucle = False
            while etatBoucle == False:
                print("")
                etatSystemeVerif = input("Voulez-vous arrêter le système (O : Oui / N : Non) : ")
                print("")
                try:
                    assert etatSystemeVerif == "O" or etatSystemeVerif == "N"
                except NameError:
                    print("La valeur de l'état n'a pas été définie, veuillez réessayer.")
                    etatBoucle = False
                except TypeError:
                    print("La valeur de l'état possède un type incompatible, veuillez réessayer.")
                    etatBoucle = False
                except ValueError:
                    print("La valeur de l'état n'est pas un nombre valide, veuillez réessayer.")
                    etatBoucle = False
                except AssertionError:
                    print("L'état saisi est incorrect, veuillez réessayer.")
                    etatBoucle = False
                else:
                    if etatSystemeVerif == "O":
                        etatSysteme = 0
                    
                    if etatSysteme == 0:
                        print("")            
                        print("Arrêt du système...")
                        print("")
                        subprocess.Popen("pkill raspistill", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                        subprocess.Popen("sudo umount /dev/sda1", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                        subprocess.Popen("sudo umount /dev/sdb1", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                        subprocess.Popen("sudo umount /dev/sdc1", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                        subprocess.Popen("sudo umount /dev/sdd1", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
                        sys.exit(0)
                        
                    etatBoucle = True
    
