# Devoir 1
ces programmes permettent de controler une LED via l'appui d'un bouton poussoir.

## Blink_push_Button 
ce programme permet de faire clignoter une LED lorsqu'on appuie sur un bouton poussoir.
lors d'un appui unique, la LED clignote a 0.5Hz. 
lors d'un second appui, la LED clignote a 2Hz.
le troisième appui éteint la LED.

## Bonus_effect
une fois l'objet instancié, on peut utiliser ses méthodes. nous utiliserons ici value qui permet de mettre un pin a un niveau haut ou bas. il faut spécifié un booléen en paramètre et définir le pin en OUT au préalable. 

	LED.value(True)
    LED.value(False)

