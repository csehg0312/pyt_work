#from search_try import lista_kereses, binarisv02
from search_try03 import binaris_kereses
import os

utv = os.getcwd()
adat:list
adat = os.listdir(utv)
rendezett:list = sorted(adat)

keresett:str = input("Keresett fajl/mappa: ")
talalat:list = []
#lista_kereses(adat, keresett)
talalat = binaris_kereses(rendezett, keresett)
print(talalat)