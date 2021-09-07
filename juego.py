from Jugador import Jugador

class Juego:
    """ clase Jugador encargada de cambiar el turno y crear nuevas partidas """

    def __init__(self):
        """ constructor de la clase """
        self.jugador1 = None
        self.jugador2 = None
        self.punto_j1 = 0
        self.punto_j2 = 0
        self.juego_nuevo()
        self.cambiar_turno()

    def juego_nuevo(self):
        """ crea una nueva partida o juego """

        verificador = False
        while not verificador:
            
            #solicita y verifica los datos para crear los tableros
            try:
                ancho = int(input("Decidan, el ancho de los tableros: "))
                alto = int(input("Decidan, el alto de los tableros: "))
            except:
                print("ingrese valores numericos")
                continue
            

            # comprueba el tamaño indicado
            if ancho < 28 and alto < 28 and alto * ancho > 7 :
                verificador = True
            else:
                if alto * ancho < 8:
                    print("el minimo del tablero es 8 casillas (4*2, 2*4 o 3*3)")
                elif int(alto) * int(ancho) > 729:
                    print("el maximo del tablero es 729 casillas (27*27)")
                

        
        # crea el objeto jugador 1 
        self.jugador1 = Jugador(ancho, alto, 1)

        # comprueba la respuesta del jugador 1, respecto a colocar barcos
        while True:
            respuesta = input(self.jugador1.nombre + ". Desea colocar los barcos manualmente? (y/n)   ")
            if respuesta.lower() in ("y", "n"):
                if respuesta == "y":
                    self.jugador1.colocar_barcos()
                    for i in range(10):
                        print (

                            "Cargando"
                            )
                    break
                else:
                    self.jugador1.barcos_randoms()
                    break
            else:
                print ("Ingrese un respuesta valida porfavor")
        
        # crea le objeto jugador 2
        self.jugador2 = Jugador(ancho, alto, 2)

        # comprueba la respuesta del jugador 2, respecto a colocar barcos
        while True:
            respuesta = input(self.jugador2.nombre + ". Desea colocar los barcos manualmente? (y/n)   ")
            if respuesta.lower() in ("y", "n"):
                if respuesta == "y":
                    self.jugador2.colocar_barcos()
                    break
                else:
                    self.jugador2.barcos_randoms()
                    break
            else:
                print ("Ingrese un respuesta valida porfavor")

    def cambiar_turno(self):
        """ crea una nueva partida o juego """
        # cambia quien esta atacando, los puntajes y termina la partida 
        while True:
            print("Turno de " + self.jugador1.nombre + "    Barcos enemigos hundidos: " + str(self.punto_j1))
            termino, punto = self.jugador2.atacar()
            if punto:
                self.punto_j1 += 1
                print (str(self.punto_j1) + " punto/s") 
            if not termino:
                print ( self.jugador1.nombre + " ha ganado" )
                break
            print ("Turno de " + self.jugador2.nombre + "    Barcos enemigos hundidos: " + str(self.punto_j2))
            termino, punto = self.jugador1.atacar()
            if punto:
                self.punto_j2 += 1
                print (str(self.punto_j2) + " punto/s")
            if not termino:
                print ( self.jugador2.nombre + " ha ganado")
                break
        
        # comprueba la respuesta de los jugadores, respecto a empezar un nuevo juego
        while True:
            respuesta = input("Desea empezar un juego nuevo? (y/n)      ")
            if respuesta.lower() in ('y', 'n'):
                if respuesta.lower() == 'y':
                    self.juego_nuevo()
                    break
                else:
                    break
            else:
                print("ingrese una respuesta valida")
                
j = Juego()