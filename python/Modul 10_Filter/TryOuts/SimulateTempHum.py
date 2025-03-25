from time import sleep_ms, ticks_ms
from random import uniform
from machine import Pin

while True:
    timestamp = ticks_ms()
    temp = round(uniform(20.0, 30.0), 1)       # Simuleret temperatur
    humidity = round(uniform(40.0, 70.0), 1)   # Simuleret fugtighed

    print(f"{timestamp},{temp},{humidity}")
    sleep_ms(500)
#💡 Denne kode sender hver 500 ms et linjeskift med `timestamp, temperatur, fugtighed` i CSV-format.