# Plataforma Cultural "Cultura+" - Sistema de Gestão de Eventos

## Descrição

"Cultura+" é uma plataforma digital idealizada para a promoção e gestão de eventos culturais. Este projeto em Python implementa o backend e a lógica de negócios para um sistema que permite a organizadores publicar diversos tipos de eventos (como shows, peças de teatro, workshops) e a participantes consultar a agenda, adquirir ingressos e interagir com as atividades disponíveis.

O sistema foi modelado com foco em reusabilidade, organização e extensibilidade, representando diferentes tipos de eventos e interações entre os diversos atores da plataforma (organizadores, participantes, e intermediários).

## Funcionalidades Implementadas (via `main.py`)

* **Gestão de Pessoas:**
    * Criação de Organizadores.
    * Criação de Participantes.
    * Visualização de Organizadores e Participantes cadastrados.
* **Gestão de Eventos:**
    * Criação de diferentes tipos de eventos:
        * **Eventos ao Vivo (LiveEvent):** Com local e capacidade.
        * **Eventos Online (OnlineEvent):** Com link de streaming e plataforma.
        * **Eventos Interativos (InteractiveEvent):** Com tipo de interação e máximo de participantes para interação.
    * Visualização detalhada de todos os eventos cadastrados, incluindo suas informações específicas e avaliações.
    * Edição simplificada de informações do evento (nome, descrição, total de ingressos).
* **Interação do Participante:**
    * Compra de ingressos para eventos (gera transações e tickets).
    * Escrita de avaliações (nota e comentário) para eventos.
    * Visualização dos ingressos adquiridos por um participante.
* **Sistema de Ingressos e Transações:**
    * Geração de tickets únicos para cada compra.
    * Criação de transações para registrar as compras.
    * Possibilidade de transferir a titularidade de um ingresso (alterando o `owner_id`).
* **Avaliações:**
    * Registro de avaliações de participantes para eventos.
    * Associação das avaliações aos respectivos eventos.

## Estrutura do Projeto

O projeto está organizado em módulos Python, cada um representando uma entidade ou um aspecto do sistema:

* `person.py`: Classe base abstrata `Person`.
* `organizer.py`: Classe `Organizer` que herda de `Person`.
* `participant.py`: Classe `Participant` que herda de `Person`.
* `intermediary.py`: Classe `Intermediary` que herda de `Person`.
* `event.py`: Classe base `Event`.
* `liveEvent.py`: Classe `LiveEvent` que herda de `Event`.
* `onlineEvent.py`: Classe `OnlineEvent` que herda de `Event`.
* `interactiveEvent.py`: Classe `InteractiveEvent` que herda de `Event`.
* `ticket.py`: Classe `Ticket`.
* `transaction.py`: Classe `Transaction`.
* `review.py`: Classe `Review`.
* `main.py`: Script principal com um menu interativo de console para criar, visualizar e interagir com as entidades do sistema.
* `diagrama_cultural.jpg`: Diagrama UML representando a arquitetura das classes e seus relacionamentos.

## Classes Principais e Responsabilidades

* **Person**: Classe base abstrata para todos os tipos de usuários, definindo atributos comuns e um método `authenticate`.
* **Organizer**: Representa um organizador de eventos, responsável por solicitar/criar eventos.
* **Participant**: Representa um participante de eventos, pode comprar ingressos e escrever avaliações.
* **Intermediary**: Representa um intermediário na venda de ingressos.
* **Event**: Classe base para todos os eventos, com atributos como nome, datas, total de ingressos e métodos para vender ingressos e adicionar avaliações.
    * **LiveEvent, OnlineEvent, InteractiveEvent**: Especializações de `Event` com atributos e comportamentos específicos.
* **Ticket**: Representa um ingresso para um evento, contendo informações sobre o evento, proprietário e transação.
* **Transaction**: Registra os detalhes de uma compra de ingressos.
* **Review**: Armazena as avaliações (nota e comentário) feitas por participantes sobre os eventos.

## Como Executar

1.  **Clone o repositório** (ou certifique-se de que todos os arquivos `.py` estejam no mesmo diretório).
2.  **Navegue até o diretório** do projeto pelo terminal.
3.  **Execute o script principal interativo:**
    ```bash
    python main.py
    ```
4.  Siga as instruções do menu no console para interagir com o sistema.
