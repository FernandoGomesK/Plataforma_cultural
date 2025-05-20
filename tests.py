# tt_tickets = 0
# print(tt_tickets)

# def remove_tickets():
#   global tt_tickets
#   tt_tickets -= 1
#   print(tt_tickets)
  
# def add_tickets():
#   global tt_tickets
#   tt_tickets += 1
#   print(tt_tickets)
  
# while True:
#     print("1 - add tickets")
#     print("2 - remove tickets")
#     print("3 - exit")
    
#     choice = input("select the choice: ")
    
#     if choice == '1':
#         add_tickets()
#     elif choice == '2':
#         remove_tickets()
#     elif choice == '3':
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")

class Ticket:
    def __init__(self):
        self.tt_tickets = 0
        
    def remove_tickets(self):
        self.tt_tickets -= 1
        print(self.tt_tickets)
    
    def add_tickets(self):
        self.tt_tickets += 1
        print(self.tt_tickets)

    def show_tickets(self):
        print(self.tt_tickets)
        
    def run(self):
        while True:
            self.show_tickets()
            print("\nOptions:")
            print("1 - Add a ticket")
            print("2 - Remove a ticket")
            print("3 - Exit")
            
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                self.add_tickets()
            elif choice == '2':
                self.remove_tickets()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
tiquet = Ticket()
tiquet.run()