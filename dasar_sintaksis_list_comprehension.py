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

print('\nmembuat list baru dengan comprehension: buang diujung')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4dx']
daftar_buku_baru = daftar_buku[0:-1:2] #start:end:step
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku[i])