from cmath import phase 
z = input()

print('%.3f' % abs(complex(z)))
print('%.3f' % phase(complex(z)))