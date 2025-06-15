class Login_Menu():
    @staticmethod
    def show_menu():
        print("Login Menu")
        print("----------")
        print("1 - Login")
        print("2 - Register")
        print("3 - Exit")
        return input("Choose one option: ")

class Main_Menu():
    @staticmethod
    def show_menu():
        print("\n--- Main Menu ---")
        print("1 - Event Menu")
        print("2 - Exit")
        return input("Choose one option: ")
    
class Event_Menu():
    @staticmethod
    def show_menu(is_admin: bool = False):
        if is_admin:
            print("1 - Create Event")
            print("2 - Remove Event")
            print("3 - Show Events")
            print("4 - Show Reviews")
            print("5 - Exit")
            return input("Choose one option: ")
        else:
            print("1 - Show Events")
            print("2 - Buy tickets")
            print("3 - Show Reviews")
            print("4 - Write Review")
            print("5 - Exit")
            return input("Choose one option: ")
            

      

