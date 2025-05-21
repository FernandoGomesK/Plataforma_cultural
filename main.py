import uuid
from datetime import date, datetime, timedelta

from person import Person
from organizer import Organizer
from participant import Participant
from event import Event
from liveEvent import LiveEvent
from onlineEvent import OnlineEvent
from interactiveEvent import InteractiveEvent
from ticket import Ticket
from transaction import Transaction
from review import Review

# --- Global Variables ---
all_organizers = []
all_participants = []
all_events = {} # Dictionary: event_id -> Event Object

# --- Input Functions ---
def get_string_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Entrada não pode ser vazia.")

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, insira um número decimal válido.")

def get_date_input(prompt: str) -> date:
    while True:
        date_str = input(prompt + " (YYYY-MM-DD): ").strip()
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de data inválido. Use YYYY-MM-DD.")

# --- Selection Functions ---
def select_organizer():
    if not all_organizers:
        print("Nenhum organizador cadastrado.")
        return None
    print("\nSelecione um Organizador:")
    for i, org in enumerate(all_organizers):
        print(f"{i + 1}. {org.name} (CPF: {org.cpf})")
    while True:
        try:
            choice = get_int_input("Escolha o número do organizador: ")
            if 1 <= choice <= len(all_organizers):
                return all_organizers[choice - 1]
            print("Escolha inválida.")
        except IndexError:
            print("Escolha inválida.")

def select_participant():
    if not all_participants:
        print("Nenhum participante cadastrado.")
        return None
    print("\nSelecione um Participante:")
    for i, part in enumerate(all_participants):
        print(f"{i + 1}. {part.name} (CPF: {part.cpf})")
    while True:
        try:
            choice = get_int_input("Escolha o número do participante: ")
            if 1 <= choice <= len(all_participants):
                return all_participants[choice - 1]
            print("Escolha inválida.")
        except IndexError:
            print("Escolha inválida.")

def select_event():
    if not all_events:
        print("Nenhum evento cadastrado.")
        return None
    print("\nSelecione um Evento:")
    event_ids = list(all_events.keys())
    for i, event_id in enumerate(event_ids):
        event = all_events[event_id]
        print(f"{i + 1}. {event.name} (ID: {event.event_id}, Tipo: {event.event_type})")
    while True:
        try:
            choice = get_int_input("Escolha o número do evento: ")
            if 1 <= choice <= len(event_ids):
                return all_events[event_ids[choice - 1]]
            print("Escolha inválida.")
        except IndexError:
            print("Escolha inválida.")


# --- Management Functions for Organizers ---
def create_organizer():
    print("\n--- Criar Novo Organizador ---")
    name = get_string_input("Nome: ")
    cpf = get_string_input("CPF: ")
    age = get_string_input("Idade: ")
    address = get_string_input("Endereço: ")
    role = get_string_input("Função (Role): ")
    
    # Verify if CPF already exists
    if any(org.cpf == cpf for org in all_organizers):
        print(f"Erro: Organizador com CPF {cpf} já existe.")
        return

    organizer = Organizer(name, cpf, age, address, role)
    all_organizers.append(organizer)
    print(f"Organizador '{name}' criado com sucesso!")

def view_organizers():
    print("\n--- Lista de Organizadores ---")
    if not all_organizers:
        print("Nenhum organizador cadastrado.")
        return
    for org in all_organizers:
        print(f"- Nome: {org.name}, CPF: {org.cpf}, Função: {org.role}")

# --- Management Functions for Participants ---
def create_participant():
    print("\n--- Criar Novo Participante ---")
    name = get_string_input("Nome: ")
    cpf = get_string_input("CPF: ")
    # Verify if CPF already exists
    if any(p.cpf == cpf for p in all_participants):
        print(f"Erro: Participante com CPF {cpf} já existe.")
        return
        
    age = get_string_input("Idade: ")
    address = get_string_input("Endereço: ")
    
    participant = Participant(name, cpf, age, address)
    all_participants.append(participant)
    print(f"Participante '{name}' criado com sucesso!")

def view_participants():
    print("\n--- Lista de Participantes ---")
    if not all_participants:
        print("Nenhum participante cadastrado.")
        return
    for part in all_participants:
        print(f"- Nome: {part.name}, CPF: {part.cpf}, Endereço: {part.address}")
        if part.tickets:
            print(f"  Ingressos ({len(part.tickets)}):")
            for ticket in part.tickets:
                event_name = all_events[ticket.event_id].name if ticket.event_id in all_events else "Evento Desconhecido"
                print(f"    - ID: {ticket.ticket_id}, Evento: '{event_name}', Tipo: {ticket.ticket_type}")
        else:
            print("  Nenhum ingresso.")


# --- Management Functions for Events ---
def create_event():
    print("\n--- Criar Novo Evento ---")
    organizer = select_organizer()
    if not organizer:
        return

    name = get_string_input("Nome do Evento: ")
    event_type_str = get_string_input("Tipo do Evento (ex: Show, Workshop): ")
    description = get_string_input("Descrição: ")
    start_date = get_date_input("Data de Início")
    end_date = get_date_input("Data de Fim")
    if end_date < start_date:
        print("Data de fim não pode ser anterior à data de início.")
        return
    total_tickets = get_int_input("Total de Ingressos: ")

    print("Qual tipo de evento específico?")
    print("1. Evento ao Vivo (Live)")
    print("2. Evento Online")
    print("3. Evento Interativo")
    type_choice = get_string_input("Escolha o tipo: ")

    event = None
    if type_choice == '1':
        venue = get_string_input("Local do Evento ao Vivo: ")
        capacity = get_int_input("Capacidade do Local: ")
        event = LiveEvent(name, event_type_str, description, start_date, end_date, organizer.cpf, total_tickets, venue, capacity)
    elif type_choice == '2':
        link = get_string_input("Link da Transmissão Online: ")
        platform = get_string_input("Plataforma: ")
        event = OnlineEvent(name, event_type_str, description, start_date, end_date, organizer.cpf, total_tickets, link, platform)
    elif type_choice == '3':
        interaction = get_string_input("Tipo de Interação: ")
        max_interaction_participants = get_int_input("Máximo de Participantes na Interação: ")
        event = InteractiveEvent(name, event_type_str, description, start_date, end_date, organizer.cpf, total_tickets, interaction, max_interaction_participants)
    else:
        print("Tipo de evento inválido.")
        return

    if event:
        all_events[event.event_id] = event
        print(f"Evento '{event.name}' (ID: {event.event_id}) criado com sucesso!")

def view_all_events():
    print("\n--- Lista de Todos os Eventos ---")
    if not all_events:
        print("Nenhum evento cadastrado.")
        return
    for event_id, event in all_events.items():
        org_name = "Desconhecido"
        for org in all_organizers:
            if org.cpf == event.organizer_id:
                org_name = org.name
                break
        print(f"\nID: {event.event_id}")
        print(f"  Nome: {event.name} (Tipo: {event.event_type})")
        print(f"  Organizador: {org_name} (ID: {event.organizer_id})")
        print(f"  Datas: {event.start_date} a {event.end_date}")
        print(f"  Ingressos: {event.remaining_tickets}/{event.total_tickets} disponíveis")
        print(f"  Descrição: {event.description}")
        if isinstance(event, LiveEvent):
            print(f"  Local: {event.venue}, Capacidade do Local: {event.capacity}")
        elif isinstance(event, OnlineEvent):
            print(f"  Link: {event.streaming_link}, Plataforma: {event.platform}")
        elif isinstance(event, InteractiveEvent):
            print(f"  Interação: {event.interaction_type}, Máx. Interação: {event.max_participants_interaction}")
        if event.reviews:
            print(f"  Avaliações ({len(event.reviews)}):")
            for review in event.reviews:
                reviewer_name = "Desconhecido"
                for p in all_participants:
                    if p.cpf == review.reviewer_id:
                        reviewer_name = p.name
                        break
                print(f"    - {reviewer_name}: {review.rating} estrelas - '{review.comment}'")


# --- Management Functions for Tickets ---
def buy_ticket_action():
    print("\n--- Comprar Ingresso ---")
    participant = select_participant()
    if not participant:
        return
    
    event = select_event()
    if not event:
        return

    print(f"Evento selecionado: {event.name}, Ingressos restantes: {event.remaining_tickets}")
    if event.remaining_tickets == 0:
        print("Desculpe, este evento está esgotado.")
        return

    ticket_type = get_string_input("Tipo do Ingresso (ex: VIP, Pista): ")
    quantity = get_int_input("Quantidade de ingressos: ")
    price_per_ticket = get_float_input("Preço por ingresso: ")
    payment_method = get_string_input("Método de Pagamento: ")

    try:
        bought_tickets = participant.buy_ticket(event, ticket_type, quantity, price_per_ticket, payment_method)
        print(f"{len(bought_tickets)} ingresso(s) comprado(s) com sucesso por {participant.name}!")
        for t in bought_tickets:
            print(f"  - Ticket ID: {t.ticket_id}, Transação ID: {t.transaction_id}")
    except Exception as e:
        print(f"Erro ao comprar ingresso: {e}")

def write_review_action():
    print("\n--- Escrever Avaliação ---")
    participant = select_participant()
    if not participant:
        return

    event = select_event()
    if not event:
        return
    
    has_ticket_for_event = any(ticket.event_id == event.event_id for ticket in participant.tickets)
    if not has_ticket_for_event:
        print(f"{participant.name} não parece ter um ingresso para o evento '{event.name}'.")

    print(f"Avaliando o evento: {event.name}")
    rating = 0
    while not (1 <= rating <= 5):
        rating = get_int_input("Nota (1-5): ")
    comment = get_string_input("Comentário: ")

    try:
        review = participant.write_review(event.event_id, rating, comment)
        event.add_review(review) # Add review to the event
        print("Avaliação enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar avaliação: {e}")
        
def edit_event_action():
    print("\n--- Editar Evento ---")
    event = select_event()
    if not event:
        return

    print(f"Editando evento: {event.name} (ID: {event.event_id})")
    print("O que você gostaria de editar?")
    print("1. Nome")
    print("2. Descrição")
    print("3. Total de Ingressos (cuidado ao reduzir abaixo dos vendidos!)")
    print("0. Cancelar")

    choice = get_string_input("Escolha uma opção: ")
    if choice == '1':
        new_name = get_string_input(f"Novo nome (atual: {event.name}): ")
        event.name = new_name
        print("Nome do evento atualizado.")
    elif choice == '2':
        new_description = get_string_input(f"Nova descrição (atual: {event.description}): ")
        event.description = new_description
        print("Descrição do evento atualizada.")
    elif choice == '3':
        new_total_tickets = get_int_input(f"Novo total de ingressos (atual: {event.total_tickets}):")
        diff = new_total_tickets - event.total_tickets
        event.total_tickets = new_total_tickets
        event.remaining_tickets += diff 
        if event.remaining_tickets < 0: # Make sure it doesn't go negative
            event.remaining_tickets = 0
        print(f"Total de ingressos atualizado. Ingressos restantes: {event.remaining_tickets}")
        
    elif choice == '0':
        print("Edição cancelada.")
    else:
        print("Opção inválida.")


# --- Main Menu ---
def main_menu():
    while True:
        print("\n===== Plataforma Cultura+ =====")
        print("1. Gerenciar Eventos")
        print("2. Gerenciar Participantes")
        print("3. Gerenciar Organizadores")
        print("4. Comprar Ingresso")
        print("5. Escrever Avaliação")
        print("0. Sair")
        choice = get_string_input("Escolha uma opção: ")

        if choice == '1':
            manage_events_menu()
        elif choice == '2':
            manage_participants_menu()
        elif choice == '3':
            manage_organizers_menu()
        elif choice == '4':
            buy_ticket_action()
        elif choice == '5':
            write_review_action()
        elif choice == '0':
            print("Saindo da plataforma. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def manage_events_menu():
    while True:
        print("\n--- Gerenciar Eventos ---")
        print("1. Criar Novo Evento")
        print("2. Ver Todos os Eventos")
        print("3. Editar Evento")
        print("0. Voltar ao Menu Principal")
        choice = get_string_input("Escolha uma opção: ")

        if choice == '1':
            create_event()
        elif choice == '2':
            view_all_events()
        elif choice == '3':
            edit_event_action()
        elif choice == '0':
            break
        else:
            print("Opção inválida.")

def manage_participants_menu():
    while True:
        print("\n--- Gerenciar Participantes ---")
        print("1. Criar Novo Participante")
        print("2. Ver Todos os Participantes")
        print("0. Voltar ao Menu Principal")
        choice = get_string_input("Escolha uma opção: ")

        if choice == '1':
            create_participant()
        elif choice == '2':
            view_participants()
        elif choice == '0':
            break
        else:
            print("Opção inválida.")

def manage_organizers_menu():
    while True:
        print("\n--- Gerenciar Organizadores ---")
        print("1. Criar Novo Organizador")
        print("2. Ver Todos os Organizadores")
        print("0. Voltar ao Menu Principal")
        choice = get_string_input("Escolha uma opção: ")

        if choice == '1':
            create_organizer()
        elif choice == '2':
            view_organizers()
        elif choice == '0':
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main_menu()