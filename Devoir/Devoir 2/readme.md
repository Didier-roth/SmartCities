# Devoir 1 : CLIGNOTEMENT DE LED AVEC BOUTON POUSSOIR
## Objectif:
Créer un programme MicroPython permet de gérer le volume d’une mélodie jouée sur un buzzer. Le
volume est contrôlé par un potentiomètre. 

## Matériel:
 - Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
 - Module potentiomètre
 - Buzzer
 - Câbles

## Programme:

### melody_volume
ce programme permet de jouer une mélodie sur un buzzer. 
le volume de la mélodie est controlé par un potentiomètre.
le potentiomètre est connecté a la pin 26 du Raspberry Pi Pico. 
le buzzer est connecté a la pin 27.
le programme utilise la librairie PWM pour controler le volume de la mélodie.



### Bonus_change_melody
Ce programme basé sur melody_volume permet de changer en plus la melodie
le programme utilise un bouton poussoir pour changer la melodie jouée sur le buzzer.
le bouton poussoir est connecté a la pin 16 du Raspberry Pi Pico.
le programme utilise la librairie PWM pour controler le volume de la mélodie.
le buzzer est connecté a la pin 27.

### Bonus_Led_Rythm
Ce programme basé sur Bonus_change_melody permet de faire briller une led de façon rythmique
la led est dimmée de façon rythmique en fonction de la mélodie jouée sur le buzzer.
la frequence de la note joué permet de determiner le dimmage de la led.
le programme utilise un bouton poussoir pour changer la melodie jouée sur le buzzer.
le bouton poussoir est connecté a la pin 16 du Raspberry Pi Pico.
le programme utilise la librairie PWM pour controler le volume de la mélodie.
le buzzer est connecté a la pin 27.
la led est connecté a la pin 15.
