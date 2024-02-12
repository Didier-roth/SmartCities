# les interuptions
ce programme a pour but d'interagir lors de l'appui sur un bouton poussoir afin d'allumer une led au travers d'interruption au niveau de la programmation

<img src="https://github.com/Didier-roth/SmartCities/blob/ressources/GPIO/Interruption/426635131_7576481725729938_1565086408004881085_n.gif">

## le handler 
le handler sera simplement une méthode qui sera appelé par le système. elle est appelé lorsque l'interruption est déclenchée.
voici un exemple de handler :

    def callback(p):
        print("button pressed")


## IRQ
le méthode IRQ de la classe pin permet de définir une interruption sur un pin.
elle prend en paramètre un handler qui est appelé lorsque l'interruption est déclenchée.
elle prend également en paramètre un trigger qui est un paramètre optionnel qui permet de définir le type d'interruption.
voici les quelques types d'interruption :

- Pin.IRQ_FALLING : interruption déclenchée lorsqu'un pin passe de l'état haut à l'état bas.
- Pin.IRQ_RISING : interruption déclenchée lorsqu'un pin passe de l'état bas à l'état haut.
- Pin.IRQ_LOW_LEVEL : interruption déclenchée lorsqu'un pin est à l'état bas.
- Pin.IRQ_HIGH_LEVEL : interruption déclenchée lorsqu'un pin est à l'état haut.
- Pin.IRQ_BLOCK_LOW : interruption déclenchée lorsqu'un pin passe de l'état bas à l'état haut et reste à l'état haut pendant un certain temps.
- Pin.IRQ_BLOCK_HIGH : interruption déclenchée lorsqu'un pin passe de l'état haut à l'état bas et reste à l'état bas pendant un certain temps.
- Pin.IRQ_BLOCK_FALL : interruption déclenchée lorsqu'un pin passe de l'état haut à l'état bas et reste à l'état bas pendant un certain temps.
- Pin.IRQ_BLOCK_RISE : interruption déclenchée lorsqu'un pin passe de l'état bas à l'état haut et reste à l'état haut pendant un certain temps.
- Pin.IRQ_NONE : interruption désactivée.
- Pin.IRQ_ANYEDGE : interruption déclenchée lorsqu'un pin passe de l'état bas à l'état haut ou de l'état haut à l'état bas.

voici le prototype de la methode:

	Pin.irq(handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False)
	
nous l'utiliserons comme ceci :

	BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=callback)
qui appele la methode nommé callback lorsque le bouton est enfoncé.

