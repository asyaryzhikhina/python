import numpy as np
import matplotlib.pyplot as plt


x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plot1 = []
plot2 = []
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f1 = str(np.poly1d(p)).split()
print(p_f1)
for i in x:
    plot1.append(float(p_f1[0])*i+float(p_f1[3]))
plt.plot(x, plot1, color='red',
         label=r'$Приближение\ по\ многочленам\ 1-й\ степени$')
p, v = np.polyfit(x, y, deg=2, cov=True)
p_f2 = str(np.poly1d(p)).split()
print(p_f2)
for i in x:
    plot2.append(float(p_f2[1])*i - float(p_f2[4])*i + float(p_f2[-1]))
plt.plot(x, plot2, color='orange',
         label=r'$Приближение\ по\ многочленам\ 2-й\ степени$')
plt.errorbar(x, y, xerr=0.05, yerr=0.1, color='blue')
plt.legend(loc='best', fontsize=13)
plt.title(r'Графики приближений в цветах флага Армении')
plt.grid()
plt.show()
