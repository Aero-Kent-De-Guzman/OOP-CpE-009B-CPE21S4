# -*- coding: utf-8 -*-
"""
Created on Mon Nov 4 08:00:00 2024

@author: Aero Kent De Guzman
"""

def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp
    
    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32
    
    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

# Kelvin & Fahrenheit to Celcius (CLASS)

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp / 9) * 5 - 32
        
    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15
    
    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    
    convert = CelsiusToKelvin(tempInCelsius)
    C2K = float(convert.conversion())
    print(C2K)
    print(" Kelvin (Celsius  to Kelvin)")
    
    convert = CelsiusToFahrenheit(tempInCelsius)
    C2F = float(convert.conversion())
    print(C2F)
    print(" Fahrenheit (Celsius to Fahrenheit)")

# Kelvin & Fahrenheit to Celcius

    convert = FahrenheitToCelsius(C2F)
    C2F = float(convert.conversion())
    print(tempInCelsius)
    print(" Celsius (Fahrenheit To Celsius)")
    
    convert = KelvinToCelsius(C2K)
    K2C = float(convert.conversion())
    print(K2C)
    print(" Celsius (Kelvin to Celsius)")

main()