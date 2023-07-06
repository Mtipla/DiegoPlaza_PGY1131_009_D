import numpy
import time
import os
import msvcrt

escenario=numpy.zeros((10,10),int)
lst_rut=[]
lst_fila=[]
lst_columna=[]

def menu_p():
    os.system("cls")
    print("""MENU PRINCIPAL
    1.Comprar entradas
    2.Mostrar ubicaiones disponbles
    3.Ver listado de asientos
    4.Mostrar ganancias totales
    5.Salir""")

def validar_num(p_min,p_max,cnt_1,cnt_2):
    while True:
        try:
            opc=int(input(f"ingrese {cnt_1}: "))
            if opc>=p_min and opc<=p_max:
                return opc
            else:
                print("ERROR! ",cnt_2)
        except:
            print("ERROR! INGRESE UN NUMERO ENTERO!")

def ver_asientos_d(t):
    os.system("cls")
    print("ASIENTOS DISPONIBLES")
    print("Columna   1  2  3  4  5  6  7  8  9  10")
    for x in range(10):
        print("Fila",x+1,end="\t: ")
        for y in range(10):
            if escenario[x][y]==0:
                print(escenario[x][y],end="  ")
            else:
                print("X",end="  ")
        print()
    time.sleep(t)

def comprar_e():
    os.system("cls")
    cont=0
    print("COMPRAR ENTRADAS")
    if 0 not in escenario:
        print("LO SENTIMOS TODOS LOS ASIENTOS HAN SIDO OCUPADOS... ")
        return
    rut=validar_num(1000000,99999999,"su rut","RUT DEBE ESTAR ENTRE 1000000 Y 99999999!")
    numero_e=validar_num(1,100,"la cantidad de entradas que quiere comprar","CANTIDAD DE ENTRADAS INVALIDA!")
    while numero_e!=cont:
        ver_asientos_d(1)
        fila=validar_num(1,10,"la fila que se quiere sentar","FILA INVALIDA!")
        columna=validar_num(1,10,"la columna que se quiere sentar","COLUMNA INVALIDA!")
        if escenario[fila-1][columna-1]==0:
            escenario[fila-1][columna-1]=1
            lst_rut.append(rut)
            lst_fila.append(fila)
            lst_columna.append(columna)
            cont+=1
            print("Asiento reservado con exito")
            time.sleep(2)
        else:
            print("Asiento ocupado por favor seleccione otro asiento")
            time.sleep(3)

def ver_listado():
    lst_rut.sort()
    print("LISTADO DE ASISTENTES")
    print(lst_rut)
    print("Pulse una tecla para continuar...")
    msvcrt.getch()

def mostrar_ganancias():
    os.system("cls")
    print("GANANCIAS TOTALES")
    con_pltnm=0
    acum_pltnm=0
    con_gld=0
    acum_gld=0
    con_slvr=0
    acum_slvr=0
    for x in range(10):
        for y in range(10):
            if escenario[x][y]==1:
                if x in range(0,1):
                    con_pltnm+=1
                    acum_pltnm+=120000
                elif x in (2,3,4):
                    con_gld+=1
                    acum_gld+=80000
                else:
                    con_slvr+=1
                    acum_slvr+=50000
    print(f"""\tTIPO ENTRADA  | CANTIDAD | TOTAL  
    Platinum $120.000 |    {con_pltnm}     |  {acum_pltnm}  
    Gold $80.000      |    {con_gld}     |  {acum_gld}  
    Silver $50.000    |    {con_slvr}     |  {acum_slvr}  
    TOTAL             |    {con_gld+con_pltnm+con_slvr}     |  {acum_pltnm+acum_gld+acum_slvr}  
    """)
    print("preisone una tecla para continuar...")
    msvcrt.getch()