import RPi.GPIO as GPIO #Llamar a allibreria que permite utilizar los pines de GPIO y renombrarla de la manera mas simple
import time #Llamar a la libreria que permite trabajar con funciones de maenejo del tiempo

PIN_LED = 7
PIN_BOTON = 3

estadoBoton = 0 # Inicialiazar una variable para almacenar el esatdo del boton.

GPIO.setmode(GPIO.BOARD) # Configurar los pines de  Raspberry segun la enumeracion fisica.
GPIO.setup(PIN_LED, GPIO.OUT) # Configurar el PIN FISICO 7 como salida.
GPIO.setuo(PIN_BOTON, GPIO.IN) # Configurar el PIN FISICO 3 como entrada.
while true: # Ciclo infinito (Void loop).
	estadoBoton = GPIO.input(PIN_BOTON) # Leer entrada digital
        GPIO.output(7, estadoBoton) # Enviar un uno logico a la salida (PIN) 7 (digitalWrite)
	if estadoBoton == 1: # si el boton esta presionado entonces:
		print("ENCENDIDO")
		 time.sleep(1) #Realizar una pausa de 1 segundo
	else: # si no
		print("APAGADO")  # imprima menasje de apagado
		time.sleep(1)

