# contrôle d'une LED
ces programmes permettent de controler une LED.
Il y a 3 variantes de programmes :
- Light_up_LED
- Blink_While-Loop
- On_Off_for-Loop

## Light_up_LED
ce programme permet d'allumer une LED.

Avant l'execution du programme, il faut connecter la LED a la pin 16 du Raspberry PI Pico W.
On constate que la LED est eteinte au depart. une fois le programme executé, la LED s'allume.


|<img src="https://raw.github.com/Didier-roth/SmartCities/ressources/GPIO/controle%20d'une%20led/LED_OFF.jpg" width=200>| <img src="https://raw.github.com/Didier-roth/SmartCities/ressources/GPIO/controle%20d'une%20led/right_arrow.png" width=200> |<img src="https://raw.github.com/Didier-roth/SmartCities/ressources/GPIO/controle%20d'une%20led/LED_ON.jpg" width=200>|
|---|-----------------------------------------------------------------------------------------------------------------------------|---|




## Blink_While-Loop
ce programme permet de faire clignoter une LED.

## On_Off_for-Loop
ce programme permet d'allumer et d'éteindre une LED un nombre de fois determiné.


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

