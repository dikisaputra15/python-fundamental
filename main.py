# sekuensial

print('ibu berkata, "pergi ke toko"')
print('budi menjawab, "baik, apa yang harus saya lakukan di toko?"')
print('ibu menjawab, "beli satu botol susu, dan jika ada telor beli 6"')
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")

# percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("budi mengecek harganya, dan ternyata uang nya cukup")
    if jumlah_telur == 0:
        print("budi membeli 1 botol susu")
    else:
        print("budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli 1 botol susu")

print("budi pulang ke rumah")
print("menyampaikan hasilnya kepada ibu")