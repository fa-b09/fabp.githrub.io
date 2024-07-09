import time
def calculoMpa():
    for c in range(0,3):
        valor1= float(input())
    calibração = 9.8066
    areacp = 7854
    fck= (valor1 * calibração )/areacp  
    res = fck
    return res


        

def imprimir():
    for c in range(1,2):
        pos = c
        resultado  = calculoMpa()
        print(f' o {pos}ª resultado é  {resultado:.2f} Mpa ')
  
 
                    
calculoMpa()
imprimir()

