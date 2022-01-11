
class usuario:
    """
    Clase que recibe un nombre de usuario y la lista de tarjeta asociadas a este.
    :param name: Nombre del usuario.
    :param cards_list: Lista con las tarjetas del usuario. Cada una de ellas es un
                       diccionario creado con la clase tarjeta_credito.
    """

    def __init__(self, name, cards_list):
        self.__name = name
        self.__cards = cards_list

    def get_name(self):
        return self.__name

    def get_cards(self):
        return self.__cards

    def __str__(self, P):
        if P:
            print("Reporte general de usuario.")
            print(f"Usuario: {self.__name}.\nNo. tarjetas: {len(self.__cards)}.\n\n")
            if len(self.__cards):
                for i, card in enumerate(self.__cards):
                    print(f"Tarjeta {i + 1}: {card.get_card_name()}.\n")
        else:
            values = [f"No. tarjetas: {len(self.__cards)}"]
            if len(self.__cards):
                for i, card in enumerate(self.__cards):
                    values.append(f"Tarjeta {i + 1}: {card.get_card_name()}.")
            return values

    def add_card(self, card):
        """
        Método que agregue una nueva tarjeta a la lista de tarjetas del usuario.
        :param card: Tarjeta en formato diccionario a añadir.
        """
        self.__cards.append(card)

    def remove_card(self, idx):
        """
        Método que elminina una tarjeta de la lista.
        :param idx: Índice de donde borrar la tarjeta de la lista.
        """
        self.__cards.pop(idx)
