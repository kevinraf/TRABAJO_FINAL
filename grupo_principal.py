
#lista para almacenar los productos y precios que se esta comprando
productos=[]
precios=[]
##############
def partes_de_pc():
    kevin3=True
    while kevin3:
        print("""
        |========================================================================|
        |                             PARTES DE PC                               |
        |========================================================================|       
        | A |MOTHERBOARD ASUS PRIME B560M-A INTEL                      |S/450    |    
        | B |PLACA MADRE GIGBAYTE A320M-S2H SOCKET AM4                 |S/295    | 
        | C |MEMORIA RAM KINGSTON FURY BEAST, 16GB DDR4, 3200 MHZ      |S/290    | 
        | D |MEMORIA KINGSTON FURY BEAST, 8GB DDR4, 3200MHZ            |S/112    | 
        | E |TARJETA DE VIDEO ZOTAC GEFORCE RTX 3060 8GB               |S/1359   | 
        | F |TARJETA DE VIDEO ASUS DUAL NVIDIA GEFORCE GTX1650 4GB     |S/1299   | 
        | G |FUENTE DE PODER 650 Bronze Cooler Máster 80 Plus Bronze   |S/436    | 
        | j |========= SALIR ====================================================| 
        |========================================================================|""")
        opa=input("|OPCION:..:").upper()
        if opa=="A":             
            precios.append(450)
            productos.append("| * |MOTHERBOARD ASUS PRIME B560M-A INTEL                      |S/450    |")         
        elif opa == "B":             
            precios.append(295)
            productos.append("| * |PLACA MADRE GIGBAYTE A320M-S2H SOCKET AM4                 |S/295    |")   
        elif opa == "C":             
            precios.append(290)
            productos.append("| * |MEMORIA RAM KINGSTON FURY BEAST, 16GB DDR4, 3200 MHZ      |S/290    |")           
        elif opa == "D":             
            precios.append(112)  
            productos.append("| * |MEMORIA KINGSTON FURY BEAST, 8GB DDR4, 3200MHZ            |S/112    | ")        
        elif opa == "E":             
            precios.append(1359) 
            productos.append("| * |TARJETA DE VIDEO ZOTAC GEFORCE RTX 3060 8GB               |S/1359   |")        
        elif opa == "F":             
            precios.append(1299) 
            productos.append("| * |TARJETA DE VIDEO ASUS DUAL NVIDIA GEFORCE GTX1650 4GB     |S/1299   |")        
        elif opa == "G":             
            precios.append(436)   
            productos.append("| * |Fuente De Poder 650 Bronze Cooler Máster 80 Plus Bronze   |S/436    |")       
        elif opa == "J":             
            bkevin3=True         
        else:             
            print("OPCION INCORRECTA")     
        return total 
##############
def perifericos_de_entrada():   
    kevin2=True  
    while kevin2:         
        print("""
        |========================================================================|
        |                       PERIFERICOS DE ENTRADA                           |
        |========================================================================|       
        | A |TECLADO-GAMING GK500 RGB NEGRO-MECANICO                   |S/182    |     
        | B |TECLADO-ASUS RX TKL Wireless Deluxe-MECANICO              |S/685    | 
        | C |TECLADO-LOGITECH K120 BUSINESS-MEMBRANA                   |S/55     | 
        | D |MOUSE-Logitech M185-INALAMBRICO                           |S/61     | 
        | E |MOUSE-Logitech M330 Silent Plus-INALAMBRICO               |S/120    | 
        | F |MOUSE-Logitech  MX Anywhere 3-INALAMBRICO                 |S/400    | 
        | G |MOUSE-Logitech M90-CABLE                                  |S/23     | 
        | j |========= SALIR ====================================================| 
        |========================================================================|""")
        opb = input("|OPCION:..:").upper()
        if opb == "A":             
            precios.append(182)
            productos.append("| * |TECLADO-GAMING GK500 RGB NEGRO-MECANICO                   |S/182    |")         
        elif opb == "B":             
            precios.append(685)  
            productos.append("| * |TECLADO-ASUS RX TKL Wireless Deluxe-MECANICO              |S/685    |")     
        elif opb == "C":             
            precios.append(55)
            productos.append("| * |TECLADO-LOGITECH K120 BUSINESS-MEMBRANA                   |S/55     |")        
        elif opb == "D":             
            precios.append(61)
            productos.append("| * |MOUSE-Logitech M185-INALAMBRICO                           |S/61     |")       
        elif opb == "E":             
            precios.append(120)
            productos.append("| * |MOUSE-Logitech M330 Silent Plus-INALAMBRICO               |S/120    |")        
        elif opb == "F":             
            precios.append(400) 
            productos.append("| * |MOUSE-Logitech  MX Anywhere 3-INALAMBRICO                 |S/400    |")       
        elif opb == "G":             
            precios.append(23)
            productos.append("| * |MOUSE-Logitech M90-CABLE                                  |S/23     |")        
        elif opb == "J":             
            kevin2=True         
        else:             
            print("OPCION INCORRECTA")     
        return total
##############
def perifericos_de_salida():
    kevin1=True
    while kevin1:         
        print("""
        |========================================================================|
        |                        PERIFERICOS DE SALIDA                           |
        |========================================================================|       
        | A |MONITOR-Monitor curvo Lenovo G27qc-30                     |S/1000   |    
        | B |MONITOR-MONITOR HP LED IPS P22 G5                         |S/452    | 
        | C |MONITOR-Acer SA220QBbmix 22" IPS Monitor                  |S/500    | 
        | D |PARLANTES-JBL GO 2                                        |S/90     | 
        | E |PARLANTES-Sony SRS-XB13                                   |S/210    | 
        | F |PARLANTES-XDOBO X8 PLUS                                   |S/350    | 
        | G |PARLANTES-Parlante Jbl Bluetooth Altavoz Go 3             |S/220    | 
        | j |========= SALIR ====================================================| 
        |========================================================================|""")
        opc=input("|OPCION:..:").upper()         
        if opc == "A":             
            precios.append(1000) 
            productos.append("| * |MONITOR-Monitor curvo Lenovo G27qc-30                     |S/1000   |")      
        elif opc == "B":             
            precios.append(452)
            productos.append("| * |MONITOR-MONITOR HP LED IPS P22 G5                         |S/452    |")          
        elif opc == "C":             
            precios.append(500)
            productos.append("| * |MONITOR-Acer SA220QBbmix 22  IPS Monitor                  |S/500    |")         
        elif opc == "D":             
            precios.append(90)
            productos.append("| * |PARLANTES-JBL GO 2                                        |S/90     |")        
        elif opc == "E":             
            precios.append(210)
            productos.append("| * |PARLANTES-Sony SRS-XB13                                   |S/210    |")         
        elif opc == "F":             
            precios.append(350)
            productos.append("| * |PARLANTES-XDOBO X8 PLUS                                   |S/350    |") 
        elif opc == "G":
            precios.append(220)
            productos.append("| * |PARLANTES-Parlante Jbl Bluetooth Altavoz Go 3             |S/220    |")       
        elif opc == "J":             
            kevin1=False        
        else:             
            print("OPCION INCORRECTA")     
        return total
#############
total = 0 
partes_de_pcs = 0 
perifericos_de_entradas = 0 
perifericos_de_salidas = 0
continuar=True
nombre=str(input("ingrese los APELLIDOS Y NOMBRES del cliente: "))
dni=str(input("ingrese el D.N.I.  del cliente: "))

while continuar:     
    print("""
    |========================================================================|
    |======================"BIENBENIDOS A TEKCENTRO"=========================|
    |========================================================================|
    |                                  MENU                                  |
    |========================================================================|
    | A |PARTES DE PC                                                        | 
    | B |PERIFERICOS DE ENTRADA                                              | 
    | C |PERIFERICOS DE SALIDA                                               | 
    |"P"|========= SALILIR Y GENERAR BOLETA DE VENTAS =======================| 
    |========================================================================|""")     
    opm = input("|OPCION:..:").upper()     
    if opm == "A":         
        partes_de_ps = partes_de_pc()     
    elif opm == "B":         
        perifericos_de_entradas = perifericos_de_entrada()     
    elif opm == "C":         
        perifericos_de_salidas = perifericos_de_salida()    
    elif opm == "P":         
        continuar=False     
    else:         
        print("OPCION INCORRECTA")  
print("""
|========================================================================|
|                          BOLETA DE VENTAS                              |     
|========================================================================|""")
print("|Sr. ",nombre," Identificado con DNI: ",dni)
print("|========================================================================|") 
print("""
\n|======== BOLSA DE PRODUCTOS COMPRADOS:                  ================|""")
for producto in productos:
    print(producto)
print("|========================================================================| ") 
neto=sum(precios)
igv=0.18*neto 
total=neto+igv 
print("| SUB TOTAL     : S/","{0:.2f}".format(neto),"                           ") 
print("| IGV           : S/","{0:.2f}".format(igv),"                            ") 
print("| TOTAL A PAGAR : S/","{0:.2f}".format(total),"                            ") 
print("""
|========================================================================|
|==================== GRACIAS POR SU COMPRA =============================|
|========================================================================|""")