# lecture d'un bouton
ce programme permet d'allumer une LED si le bouton est pressé. 
les elements interessant a retenir ici sont :
le constructeur de la classe Pin
la fonction Value de la classe Pin

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
