# Serie sumatoria de n

def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l


#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l
    
#funciones integradas
edadclientes= [45, 35, 25, 18, 36, 45, 28, 38]

longitud= len(edadclientes)
print("existen: ",longitud, "numero de edades ingresadas por ANDRES CARRASCO")

elmasmayor=max(edadclientes)
print("el cliente de mas edad tiene: ",elmasmayor, "años de edad")

elmenor=min(edadclientes)
print("el cliente de menor edad tiene: ",elmenor, "años de edad")    