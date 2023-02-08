print('='*20, 'KASIR', '='*20)
hb = int(input('Harga Barang :'))
pil = input('Apakah anda membeli barang lagi? [yes/no]')
while pil=='yes':
    print('='*20, 'KASIR', '='*20)
    hb = input('Harga Barang :')
    pil = input('Apakah anda membeli barang lagi? [yes/no]')
    if pil=='no':
       tb=hb+hb
       print('Total BELANJA :',tb) 
else:
    print('INVALID')