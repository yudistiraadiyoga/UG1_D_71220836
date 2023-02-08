print('-'*8, "Nilai ke 1", '-'*8)
nh1 = int(input('Nilai Harian :'))
nuts1 = int(input('Nilai UTS :'))
nuas1 = int(input('Nilai UAS :'))
print('-'*8, "Nilai ke 2", '-'*8)
nh2 = int(input('Nilai Harian :'))
nuts2 = int(input('Nilai UTS :'))
nuas2 = int(input('Nilai UAS :'))
def t_n():
    tn = int(nh1+nh2+nuts1+nuts2+nuas1+nuas2)/6
    print('Total nilai yang didapat :', tn)
    if tn>=80:
        print("Total Nilai Dalam Huruf : A")
    elif tn>=60:
        print('Total Nilai Dalam Huruf : B')
    elif tn>=40:
        print('Total Nilai Dalam Huruf : C')
    elif tn<=19:
        print('Total Nilai Dalam Huruf : E')
    elif tn<=39:
        print('Total Nilai Dalam Huruf : D')
    else:
        print('error')
print('-'*8, "Total Nilai", '-'*8)
t_n()