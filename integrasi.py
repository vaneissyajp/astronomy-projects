#import
from math import exp


#pendefinisian fungsi
def f(x):
#fx=6*1.44/(x**2)*(x**1.44)/(3e-3**1.44)*exp(-((x/(3e-3))**1.44) disederhanakan menjadi 
    fx=(6*1.44/0.003**1.44)*exp(-((x/(0.003))**1.44))/(x**0.56)
    return fx

#meminta masukkan batas atas, batas bawah, dan jumlah segmen
a=float(input('masukkan dmin (cm): '))
b=float(input('masukkan dmax (cm): '))
n=int(input('masukkan banyak segmen yang diinginkan: '))
 
#pendefinisian komponen-komponen yang dibutuhkan 
d=(a+b)/n  #Lebar segmen
fxa=f(a)   #pendefinisian nilai awal
fxb=f(b)

if n==1: #jika segmen yang diinginkan 1 maka
    Luas=(fxa+fxb)*d/2
else: #jika segmen yang diinginkan bukan 1 maka
    '''
    berasal dari integrasi metode trapesium 2 segmen
    Luas=((f(a)+f(b))*d/2)+f(a1)*d
    dengan f(a1)*d didefinisikan sebagai suku sisa yang akan bertambah dengan
    banyaknya segmen yang diminta
    '''
    Luas1=(fxa+fxb)*d/2
    sisa1=0.0 #pendefinisian awal jumlah suku sisa
    for i in range (1,n,1):
        fx1=f(a+i*d)
        sisa=fx1*d
        sisa1=sisa+sisa1
    Luas=Luas1+sisa1 #hasil integrasi
print ()
print ('Luas permukaan per massa debu berbentuk bola adalah ', Luas,' cm^2/g')
