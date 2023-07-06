import funciones as fn

while True:
    fn.menu_p()
    opc=fn.validar_num(1,5,"una opcion","OPCION INVALIDA!")
    if opc==1:
        fn.comprar_e()
    elif opc==2:
        fn.ver_asientos_d(4)
    elif opc==3:
        fn.ver_listado()
    elif opc==4:
        fn.mostrar_ganancias()
    else:
        print("GRACIAS POR PREFERIRNOS TENGA UN BUEN DIA \nDiego Plaza 06-07-2023")
        break