#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# PEP 8, PEP 263.
"""
Arduino HomeBridge

homebridge mitsubishi vac-ir control desde Arduino
version: 0.0.1

Arduino Control Script para el plugin  Mitsubihishi VAC IR Remote de homebridge
             https://github.com/kounch/homebridge-mitsubishi-vac-ir
             https://github.com/kounch/homebridge_mitsubishi_ir_arduino

licencia: ISC

    Comandos:
        'G' - Obtener temperatura
        'S,m,t,f,v,o' - Ajustar A/C donde:
            m - Modo (0-auto, 1-calor, 2-frio, 3-deshumidificador, 4-ventilador)
            t - Temperatura deseada (en grados centigrados, sin decimales)
            f - Ventilador (0-auto, 1,2,3,4,5-velocidad, 6-Silencioso)
            v - Aleta (0-auto, 1,2,3,4,5-velocidad, 6-movimiento)
            o - Encendido/Apagado (1-Encendido, 0-Apagado)
"""

import sys
import serial

SERIAL_PATH = '/dev/cu.usbmodem221'
#SERIAL_PATH = '/dev/ttyACM0'

def main():
    """Rutina principal"""
    if len(sys.argv) != 2:
        sys.exit(1)

    comando = sys.argv[1]
    result_command = send_command(comando)
    print result_command[1]
    if result_command[0] == 'KO':
        sys.exit(2)

    sys.exit(0)


def send_command(str_command):
    """send command"""
    arduino_usb = serial.Serial(SERIAL_PATH, 9600, timeout=5)
    result_usb = arduino_usb.readline()
    arduino_usb.write(str_command + '\n')
    result_usb = arduino_usb.readline()
    result_usb = result_usb.strip()
    result_usb = result_usb.split(",")
    arduino_usb.close()
    return result_usb


if __name__ == "__main__":
    main()
