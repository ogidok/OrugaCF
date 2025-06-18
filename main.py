from menu import menu

def main():
    selected = menu.run_menu()

    
    if selected == "Sniffing":
        print("Iniciando Sniffing")
        
    elif selected == "Spoofing":
        print("Iniciando Spoofing")
    

main()
