#!/bin/python
# program perulangan kata

# module
import os,sys,time
from time import sleep

# tampilan
os.system('clear')
os.system('figlet Dhanz03')
sleep(1)
print('\33[31;1m    (+) BY MR DHANZ SPM (+)\33[37;1m')
print('\33[31;1m=========================================\33[37;1m')
print('    ')
print('\33[31;1mMasukan Kata"mu Bro ')
kata = input('=> ')
print('\33[37;1mMasukan Jumlah Perulangan')
jumlah = int(input('=> '))

# data
try:
   for i in range(jumlah):
       print('=> ' + kata)
       sleep(0.05)
       print('=> ' + kata)
       sleep(0.05)

except:
      print('berhasil')

