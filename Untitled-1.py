"""class orden :

    def __init__(self,fecha,cliente) -> None:
        self.fecha=fecha
        self.cliente=cliente
"""
    
    
def listarOrdenes(ordenes):
    print("******************************************************************")
    i=1
    for o in ordenes:
        print(str(i)+". cliente:"+o["cliente"])
        print( "fecha: "+o["fecha"])
        
    

flag=True
ordenes=[]
while flag:
    print ("**********************************************************")
    print("1. Ingresar orden")
    print("2. Leer ordenes")
    print("3. Editar orden")
    print("4. Cancelar orden")

    a1=input()
    match a1:
        case "1":
            orden={}
            print("ingrese el tipo: ")
            print("1. Normal")
            print("2. Con garantia")
            tipo=input()
            if tipo=="1":
                orden["tipo"]="Normal"
            elif tipo=="2":
                orden["tipo"]="Con garantia"
            orden["tipo"]=input()
            orden["fecha"]=input("ingresar fecha:")
            orden["cliente"]=input("ingrese nombre del cliente: ")
            
            ordenes.append(orden)
        case "2":
            listarOrdenes(ordenes)
        case "3":
            listarOrdenes(ordenes)
            print("****************************************************************************")
            a2=input("Seleccione su orden :")
            print("1.Cambiar nombre")
            print("2.Cambiar fecha")
            print("3.Dar fecha de inicio de reparacion")
            print("4.Dar fecha de finalizacion de reparacion")
            print("5.Dar fecha de retiro de cliente")
            a3=input()
            match a3:
                case "1":
                    ordenes[a2]["cliente"]=input()
                case "2":
                    ordenes[a2]["fecha"]=input()
                case "3":
                    print("ingresa la fecha de inicio de la reparacion: ")
                    ordenes[a2]["fechaInicioReparacion"]=input()
                case "4":
                    print("ingresa la fecha de finalizacion de la reparacion: ")
                    ordenes[a2]["fechaOrdenLista"]=input()
                case "5":
                    print("ingresa la fecha de retiro: ")
                    ordenes[a2]["fechaClienteRetiro"]=input()
        case "4":
            listarOrdenes(ordenes)
            print("seleciona la orden a borrar :")
            a3=input()
            ordenes.remove(ordenes[int(a3)])
                

                
            