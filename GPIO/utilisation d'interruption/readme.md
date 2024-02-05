# les interuptions
ce programme a pour but d'interagir lors de l'appui sur un bouton poussoir afin d'allumer une led au travers d'interruption au niveau de la programmation

## le handler 
le handler sera simplement une méthode qui sera appelé par le système. 

## IRQ
le méthode IRQ de la classe pin permet de définir quand le système doit appeler le handler et quel handler il doit appeler.
voici le prototype de la methode:

	Pin.irq(handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False)
	
nous l'utiliserons comme ceci :

	BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=callback)
qui appele la methode nommé callback lorsque le bouton est enfoncé.

