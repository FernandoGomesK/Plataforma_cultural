class Menus:
    def __init__(self):
        pass  
    
    def show_main_menu(self):
        print("Main Menu")
        print("----------")
        print("1 - Event Menu")
        print("2 - Exit")
        
    def show_event_menu(self):
        print("Event Menu")
        print("----------")
        print("1 - Main Menu")
        print("2 - Exit")
        
    def event_menu(self):
        while True:
            self.show_event_menu()
            choice = input("Choose one option: ")
            if choice == "1":
                break
            elif choice == "2":
                print("Logging out and returning to login menu...")
                return "exit"
            else:
                print("Invalid Option, please select one from the menu.")
        return ""
        
        
    def main_menu(self):
        while True:
            self.show_main_menu()
            choice = input("Choose one option: ")
            if choice == "1":
                if self.event_menu() == "exit":
                    break
            elif choice == "2":
                print("Logging out and returning to login menu...")
                break
            else:
                print("Invalid Option, please select one from the menu.")