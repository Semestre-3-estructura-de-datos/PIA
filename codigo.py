




menu=1
separador=("*"*30)
contador=1
try:
    while menu==1:
        print(separador+"Bienvenido al Menu Principal" +separador)
        print("Opciones del menu")
        print("1=Registrar una Venta\n2=Consultar ventas de un día específico\n3=Salir")
        opcion=int(input("Que opcion eliges : "))
        listasumaprecio=[]
        
        if opcion==1:
            ciclo=1
            print(separador+"Bienvenido al registrador de ventas"+separador)
            while ciclo==1:
                print(f"VENTA {contador}")
                
                clave=int(input("Dime la clave : "))
                descripcion=input("Dime la descripcion del articulo : ")
                cantidad=int(input("Dime la cantidad de piezas vendidas : "))
                precio=float(input("Dime el precio de venta unitario : "))
                
                
                ahora = datetime.datetime.now()
                tiempo=ahora.strftime('%d/%m/%Y')
                
                insertardatos(clave,descripcion,cantidad,precio,tiempo)
                listasumaprecio.append(precio*cantidad)
        
                contador=contador+1            
                print(separador)
                print("Ingresa el numero 1 si deseas seguir registrando ventas\nIngresa el numero 0 si deseas salir del registrador de ventas")
                ciclo=int(input(":"))
                print(separador)
                print("")
            
            print(separador)
            print(f"Este es el monto total a pagar : {sum(listasumaprecio)}")
            print(separador)
            

        elif opcion==2:
            try:
                print(separador+"Bienvenido al consultador de ventas"+separador)
                print("-"*20)
                dia=(input("Dime el dia en el que registraste la venta : "))
                mes=input("Dime el mes en el que registraste la venta : ")
                año=input("Dime el año en el que registraste la venta : ")
                
                if len(mes)==1:
                    mes=("0"+ mes)
                    
                if len(dia)==1:
                    dia2=("0"+dia+"/")
                    fecha=(dia2+mes+"/"+año)
                else:
                    fecha=(dia+"/"+mes+"/"+año)
                print("")
                
                validacion(fecha)
                
            except Error as e:
                print(e)
        
        
        elif opcion==3:
            break
               
except:
    print(f"Ocurrió un problema {sys.exc_info()[0]}")

finally:
    print("FIN DEL CODIGO")