from ticket import Ticket

class System():
    def __init__(self, name):
        self.name = name
        self.ticket_mgr = Ticket()    
    def run(self):
        while True:
            
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