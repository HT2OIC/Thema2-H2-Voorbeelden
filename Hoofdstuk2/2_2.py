# Onboard led aanzetten, zodat we weten wanneer het programma runt op de Pico.
from machine import Pin
led = Pin("LED", Pin.OUT)
led.value(1)