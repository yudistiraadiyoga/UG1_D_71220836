count = int(input('Masukkan Angka: '))
print()
  
for lubang in range(count):
  for i in range(count-lubang):
    print(' ',end='')
      
  for j in range(lubang+1):
    print('* ',end='')
  print()
 
for lubang in range(1,count):
  for i in range(lubang+1):
    print(' ',end='')
      
  for j in range(count-lubang):
    print('* ',end='')
  print()