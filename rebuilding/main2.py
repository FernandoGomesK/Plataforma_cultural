from menus2 import Menus
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
class System:
    def __init__(self):
        self.menus = Menus()
          
    def run(self):
        clear_terminal()
        self.menus.main_menu()


if __name__ == "__main__":
    sistema = System()
    sistema.run()
    
