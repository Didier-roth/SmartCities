# Devoir 1 : CLIGNOTEMENT DE LED AVEC BOUTON POUSSOIR
## Objectif:
Créer un programme MicroPython qui permet de faire clignoter une LED à différentes vitesses en
fonction du nombre de pressions sur un bouton poussoir.

## Matériel:
- Microcontrôleur compatible MicroPython (Raspberry Pi Pico)
- Module LED
- Module bouton poussoir
- Câbles

## Programme:

### Blink_push_Button 
ce programme permet de faire clignoter une LED lorsqu'on appuie sur un bouton poussoir.
lors d'un premier appui, la LED clignote a 0.5Hz. 
lors d'un second appui, la LED clignote a 2Hz.
le troisième appui éteint la LED.

<img src="https://github.com/Didier-roth/SmartCities/blob/ressources/Devoirs/Devoir%201/Blink_push_button.gif" width=200 align="center">


### Bonus_effect
le programme principal reste le meme que Blink_push_Button. 
la seul difference est que lorsqu'on appuie sur le bouton poussoir, la LED clignote a 0.5Hz. 
lorsqu'on appuie une seconde fois, la LED clignote a 2Hz. 
lorsqu'on appuie une troisième fois, la LED fait un petit effet de lumiere pour signaler
le changement de mode. elle clignotera de plus en plus vite 5 fois avant de passer au mode suivant.

<img src="https://github.com/Didier-roth/SmartCities/blob/ressources/Devoirs/Devoir%201/Bonus_effect.gif" width=200 align="center">

### Bonus_Press_Number
le programme principal reste le meme que Bonus_effect. 
la difference etant que le nombre d'appuis pour passer au mode suivant doit etre de 2.
le double appuis doit etre realisé en moins de 0.5 secondes. il y a egalement un filtre
pour eviter les rebonds du bouton poussoir.

<img src="https://github.com/Didier-roth/SmartCities/blob/ressources/Devoirs/Devoir%201/Bonus_press_number.gif" width=200 align="center">

