from ticket import Ticket

class System():
    def __init__(self, name):
        self.name = name
        self.ticket_mgr = Ticket()    
    def run(self):
        while True:
            print("Main Menu")
            print("1 - Event Operations")
            print("2 - Client Operations")
            print("3 - Ticket Operations")
            print("4 - Exit")
            
            choice = input("select the option: ")
            if choice == "1":
                self.event_menu()
            elif choice == "2":
                self.client_menu()
            elif choice == "3":
                self.ticket_menu()
            elif choice == "4":
                break
            else:
                print("not adequated")
            
    def ticket_menu(self):
        while True:
            print("Ticket Menu")
            print("1 - Show Ticket")
            print("2 - Add Ticket")
            print("3 - Remove Ticket")
            print("4 - Exit")
            
            menu = input("select the option: ")
            if menu == "1":
                self.ticket_mgr.show_ticket()
            elif menu == "2":
                self.ticket_mgr.add_ticket() 
            elif menu == "3":
                self.ticket_mgr.remove_ticket()
            elif menu == "4":
                break
            else:
                print("not adequated")