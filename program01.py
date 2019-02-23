modal=100000000
sum=0
m=0
laba = [int(0), int(0), int(modal) * .1, int(modal) * .1, int(modal) * .5, int(modal) * .5, int(modal) * .5, int(modal) * .2]
print('MODAL AWAL PENGUSAHA :', modal)
for i in laba :
    sum=sum+i
    m+=1
    print('laba bulan ke: ', m ,'sebesar :',i)
print('TOTAL LABA / UNTUNG  YANG DIDAPATKAN :', sum)