import numpy as np 
from math import *

xi = float(input('Xi: '))
xu = float(input('Xu: '))
fx = input('f(x): ')
y = lambda x: eval(fx)

def bisection(a,b,epsilon,errA,it):
    '''Bisection method '''
    fxi = y(a) 
    fxu = y(b)
    check = fxi * fxu

    xm_1 = 0.0
    i = 1

    if check > 0:
        return 'No cumple las condiciones iniciales del metodo de Biseccion abs(b-a)>= epsilion '
    else:
        print('{:^10} {:^10} {:^13} {:^10} {:^10} {:^14} {:^10}'
        .format('|iteracion','Xi','Xu','f(Xi)','Xm','f(Xm)','Ea'))
        while (abs(b-a)>= epsilon):
            fxi = y(a) 
            xm = (a + b) / 2.0
            ea = abs((xm - xm_1)/xm) * 100
            fxm = y(xm) 
            signo = fxi * fxm

            print(f'|  {i:05}  |  {a:.5f}  |  {b:.5f}  |  {fxi:.5f}  |  {xm:.5f}  |  {fxm:.5f}  |  {ea:.5f}  |')

            #fxi*fxm = 0
            if (fxi * fxm) == 0:
                break
            #for error rate (%)
            if ea <= errA:
                break
            #for iteration
            if i == it:
                break

            if signo < 0:
                b = xm
            else:
                a = xm
            
            xm_1 = xm
            i += 1
            #print(xm)
    return xm


def falsePosition(a,b,epsilon,errA,it):
    ''' False Position method '''
    i = 1
    xm_1 = 0.0
    condition = True
    if y(a) * y(b) < 0:
        print('{:^10} {:^10} {:^13} {:^10} {:^10} {:^10} {:^14} {:^10}'
        .format('|iteracion','Xi','Xu','f(Xi)','f(Xu)','Xm','f(Xm)','Ea'))
        while condition:
            fxi = y(a)
            fxu = y(b)
            xm = a - (((b-a) * fxi)/(fxu - fxi))
            ea = abs((xm - xm_1)/xm) * 100
            fxm = y(xm)
            print(f'|  {i:05}  |  {a:.5f}  |  {b:.5f}  |  {fxi:.5f}  |  {fxu:.5f}  |  {xm:.5f}  |  {fxm:.5f}  |  {ea:.5f}  |')
            #fxi*fxm = 0
            condition = abs(fxm) > epsilon
            #for error rate (%)
            if ea <= errA:
                break
            #for iteration
            if i == it:
                break

            if fxi*fxm < 0:
                b = xm
            else:
                a = xm
            
            xm_1 = xm
            i += 1
        return xm
    else:
        return 'No cumple las condiciones iniciales del metodo de falsa posision'


def fixedPoint(a,epsilon,errA,it):
    ''' Fixed Point method '''
    g = input('g(x): ')
    gx = lambda x: eval(g)
    i = 1
    gxi_1 = 0.0
    condition = True
    print('{:^10} {:^10} {:^10} {:^10} {:^10}'
        .format('|iteracion','Xi','g(Xi)','f(Xi)','Ea'))
    while condition:
        gxi = gx(a)
        fxi = gxi - (gxi_1)
        ea = abs((gxi - a)/gxi) * 100
        print(f'|  {i:05}  |  {a:.5f}  |  {gxi:.5f}  |  {fxi:.5f}  |  {ea:.5f}  |')
        a = gxi
        gxi_1 = gxi
        #fxi*fxm = 0
        condition = abs(fxi) > epsilon
        #for error rate (%)
        if ea <= errA:
            break
        #for iteration
        if i == it:
            break
        i += 1
    return gxi
        

def newtonRapshon(a,epsilon,errA,it):
    ''' Newthon Raphson method '''
    f = input("f'(x): ")
    dfx = lambda x: eval(f)
    i = 1
    condition = True
    print('{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10}'
        .format('|iteracion','Xi','f(Xi)',"f'(Xi)",'Xi+1','|Xi+1-Xi|','Ea'))
    while condition:
        fxi = y(a)
        dfxi = dfx(a)
        xN = a - (fxi/dfxi)
        ea = abs((xN - a)/xN) * 100
        print(f'|  {i:05}  |  {a:.5f}  |  {fxi:.5f}  |  {dfxi:.5f}  |  {xN:.5f}  |  {abs(xN - a):.5f}  |  {ea:.5f}  |')
        a = xN
        #fxi*fxm = 0
        condition = abs(fxi) > epsilon
        #for error rate (%)
        if ea <= errA:
            break
        #for iteration
        if i == it:
            break
        i += 1
    return xN



def options():
    method = input('Selecciona un metodo\n1.Biseccion\n2.Falsa posision\n3.Punto fijo\n4.Newton Rapshon\n')
    if method == '1':
        stop = input('1.F(xi)*F(xm)=0\n2.Iteraciones\n3.Error aproximado\n')
        if stop == '1':
            print(bisection(xi,xu,0,0,-1))
        elif stop == '2':
            iterations = int(input('Numero de iteraciones: '))
            print(bisection(xi,xu,0,0,iterations))
        elif stop == '3':
            aproximateError = float(input('Ea: '))
            print(bisection(xi,xu,0,aproximateError,-1))
        else:
            input('selecciona una opcion correcta\n')
            options()
    elif method == '2':
        stop = input('1.F(xi)*F(xm)=0\n2.Iteraciones\n3.Error aproximado\n')
        if stop == '1':
            print(falsePosition(xi,xu,0,0,-1))
        elif stop == '2':
            iterations = int(input('Numero de iteraciones: '))
            print(falsePosition(xi,xu,0,0,iterations))
        elif stop == '3':
            aproximateError = float(input('Ea: '))
            print(falsePosition(xi,xu,0,aproximateError,-1))
        else:
            input('selecciona una opcion correcta\n')
            options()
    elif method == '3':
        stop = input('1.F(xi)*F(xm)=0\n2.Iteraciones\n3.Error aproximado\n')
        if stop == '1':
            print(fixedPoint(xi,0,0,-1))
        elif stop == '2':
            iterations = int(input('Numero de iteraciones: '))
            print(fixedPoint(xi,0,0,iterations))
        elif stop == '3':
            aproximateError = float(input('Ea: '))
            print(fixedPoint(xi,0,aproximateError,-1))
        else:
            input('selecciona una opcion correcta\n')
            options()
    elif method == '4':
        stop = input('1.F(xi)*F(xm)=0\n2.Iteraciones\n3.Error aproximado\n')
        if stop == '1':
            print(newtonRapshon(xi,0,0,-1))
        elif stop == '2':
            iterations = int(input('Numero de iteraciones: '))
            print(newtonRapshon(xi,1e-10,0,iterations))
        elif stop == '3':
            aproximateError = float(input('Ea: '))
            print(newtonRapshon(xi,0,aproximateError,-1))
        else:
            input('selecciona una opcion correcta\n')
            options()

options()