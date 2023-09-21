daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
print('tampilkan variable daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\ntampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\ntampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'kenji volume 2', -313, 3.14]
print('\ntampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal daftar_buku')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
print('\ntambahkan 1 buku baru')
daftar_buku.append('dunia matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nganti element pertama')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
daftar_buku[0] = 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nambil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang diambil tadi')
print(buku)

print('\npop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\npop -1')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[0:-2] #start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[0::2] #start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])