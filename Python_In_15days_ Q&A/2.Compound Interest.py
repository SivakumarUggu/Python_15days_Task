#calculate the compound interest of given principal(p),time period(t), and interest(I)

P=float(input('enter principal:'))
T=float(input('enter time period:'))
R=float(input('enter rate of interest:'))
N=float(input('enter the number of times interest compounded per year:'))
Amount=P*(1+(R/N))**(N*T)
print('total amount is: %.4f'%Amount)
CI=Amount-P
print('Compound interest(CI) is: %.4f'%CI)