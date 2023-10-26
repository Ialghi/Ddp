#1
kendaraan = ['Beat','Motor','Honda',110]
print(kendaraan)

#2
kendaraan.append ('Hitam')
kendaraan.insert (5,2)
kendaraan.append ('18.000.000')
print(kendaraan)

kendaraan.pop (1)
print(kendaraan)

#3
pilihan = input('pilih luas bangunan?')
match pilihan:
  case '1':
    s = int(input('masukan sisi'))
    print(s*s) 
  case '2':
    phi = 3.14
    r = int(input('masukan jari-jari'))
    print(phi*r*r)
  case '3':
    a = int(input('masukan alas'))
    t = int(input('masukan tinggi'))
    print(1/2*a*t)
  case _:
    print('pilih yang lain')