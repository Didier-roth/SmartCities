﻿# lecture d'un bouton
Ces programmes permettent de prendre en main la lecture d'un bouton poussoir.
pour cela, deux programmes :
- Button_Light
- Control_LED_On_Off

## Button_Light
ce programme permet d'allumer une LED lorsqu'on appuie sur un bouton poussoir.
la LED s'éteint lorsque le bouton est pressé a nouveau.
Le bouton est connecté au pin 16 et la LED au pin 18.

<img src="https://github.com/Didier-roth/SmartCities/blob/ressources/GPIO/lecture%20du%20bouton%20poussoir/Button_light.gif" width=200>

## Control_LED_On_Off
ce programme permet d'allumer et d'éteindre une LED en appuyant sur un bouton poussoir.
la LED s'allume lorsqu'on appuie sur le bouton et s'éteint lorsqu'on relache le bouton.
le bouton est connecté au pin 16 et la LED au pin 18.

<img src="https://github.com/Didier-roth/SmartCities/blob/ressources/GPIO/lecture%20du%20bouton%20poussoir/Control_On_Off_with_Button.gif" width = 200>

# Elements important utilisés
## constructeur 
afin de construire un objet de classe Pin, nous utiliserons le constructeur :

	class machine.Pin(id, mode=-1, pull=-1,*, value=None, drive=0, alt=-1)

nous l'utiliserons de la manière suivante pour instance	le pin 16 en mode sortie. nous spécifions donc uniquement les deux premier paramètres. 

	LED = machine.Pin(16,machine.Pin.OUT)


## value
une fois l'objet instancié, on peut utiliser ses méthodes. nous utiliserons ici value qui permet de mettre un pin a un niveau haut ou bas. il faut spécifié un booléen en paramètre et définir le pin en OUT au préalable. 

	LED.value(True)
    LED.value(False)

value peut également etre utilisé sans pamametre et le Pin défini en IN.
en effet, sans paramètre et en mode IN, value retourne un booléen qui reflète l'état du pin ; si une tension est appliqué sur le pin, l'état logique 1 (ou VRAI)  est retourné. dans le cas contraire, c'est 0 (ou FALSE) qui est retourné. 

	while(BUTTON.value()):
