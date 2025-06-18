from m5stack import lcd, btnA, btnB, btnPWR
import time

menu_items = ["Sniffing", "Spoofing", "Scan", "Info"]
selected = 0

def draw_menu():
    lcd.clear()
    for i, item in enumerate(menu_items):
        prefix = " > " if i == selected else "   "
        lcd.print(prefix + item + "\n", color=lcd.YELLOW if i == selected else lcd.WHITE)

def run_menu():
    global selected
    draw_menu()

    while True:
        if btnA.wasPressed():
            selected = (selected - 1) % len(menu_items)
            draw_menu()
        elif btnB.wasPressed():
            selected = (selected + 1) % len(menu_items)
            draw_menu()
        elif btnPWR.wasPressed():
            lcd.clear()
            lcd.print("Entrando a:\n" + menu_items[selected], color=lcd.GREEN)
            time.sleep(1)
            return menu_items[selected]  
        time.sleep(0.1)
