import os 

flag=True
while(flag):
    print(f"{'Menu':^20}")
    
    match(input()):
        case "n":
            os.system("cls")
        case _:
            flag=False