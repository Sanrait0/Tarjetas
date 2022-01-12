import json
import os

'''CALCULADORA DE INTERESES'''

class tarjeta_credito:
    """
        Crea una nueva tarjeta con ciertas características.
        :param card_name: Nombre del titular de la tarjeta.
        :param irate: Tasa de inteŕes anual.
        :param debt: Deuda actual.
        :param payment: Monto del pago.
        :param charges: Cargos adicionales.
    """

    def __init__(self, card_name, irate, debt, payment, charges):
        self.__card_name = card_name
        self.__irate = irate
        self.__debt = debt
        self.__payment = payment
        self.__charges = charges

    def get_card_name(self):
        return self.__card_name

    def get_irate(self):
        return self.__irate

    def get_debt(self):
        return self.__debt

    def get_payment(self):
        return self.__payment

    def get_charges(self):
        return self.__charges

    def __str__(self):
        d_tarjeta = {'_tarjeta_credito__card_name': 'Tarjeta', '_tarjeta_credito__irate': 'Tasa',
                     '_tarjeta_credito__debt': 'Deuda', '_tarjeta_credito__payment': 'Pago',
                     '_tarjeta_credito__charges': 'Cargos', 'new_debt': 'Nueva Deuda'}
        for key in self.__dict__:
            print(f"{d_tarjeta[key]}: {self.__dict__[key]}")

    def crea_tarjeta(self, *args):
        """
        Crea una nueva tarjeta con ciertas características.
        :param *args: Monto del pago (Payment).
        """
        payment = args[0] if len(args) else self.__payment
        e = 0
        try:
            self.__card_name + 'ABC'
        except TypeError:
            print("El nombre de la tarjeta debe ser una cadena. Intente de nuevo.")
            e += 1

        try:
            self.__irate + 100
        except TypeError:
            print("La tasa de interés debe ser un valor numérico. Intente de nuevo.")
            e += 1

        try:
            self.__debt + 100
        except TypeError:
            print("La deuda ingresada debe ser un valor numérico. Intente de nuevo.")
            e += 1

        try:
            payment + 100
        except TypeError:
            print("La pago ingresado debe ser un valor numérico. Intente de nuevo.")
            e += 1

        try:
            self.__charges + 100
        except TypeError:
            print("Los cargos ingresados deben ser un valor numérico. Intente de nuevo.")
            e += 1

        if e > 0:
            exit()

        if payment <= self.__debt:
            tarjeta = {'Card_name': self.__card_name,
                    'irate': self.__irate,
                    'debt': self.__debt,
                    'payment': payment,
                    'charges': self.__charges}
            return tarjeta
        else:
            print("ERROR. El monto del pago excede al de la deuda. Ingrese sus datos de nuevo.")
            new_payment = float(input("Ingrese el monto a pagar: "))
            return self.crea_tarjeta(new_payment)

    def captura_nueva_deuda(self, *args):
        """
        Captura la deuda actualizada sobre una tarjeta.
        """
        dic_card = args[0] if len(args) else self.crea_tarjeta()
        monthly_irate = dic_card['irate']/(12 * 100)
        rec_debt = (dic_card['debt'] - dic_card['payment'])
        rec_debt = rec_debt*(1 + monthly_irate) if rec_debt >= 0 else rec_debt
        dic_card['new_debt'] = max(rec_debt + dic_card['charges'], 0)

        return dic_card

    def generar_reporte(self, P, *args):
        """
        Imprime la información de una tarjeta contenida en un diccionario.
        :param *args: Tarjeta en forma de diccionario.
        """
        d_tarjeta = {'Card_name': 'Tarjeta', 'irate': 'Tasa', 'debt': 'Deuda',
                    'payment': 'Pago', 'charges': 'Cargos', 'new_debt': 'Nueva Deuda'}
        card = args[0] if len(args) else self.captura_nueva_deuda()
        values = []
        for key in card:
            if P:
                print(f"{d_tarjeta[key]}: {card[key]}")
            else:
                try:
                    values.append(f"{d_tarjeta[key]}: {round(card[key], 3)}")
                except TypeError:
                    values.append(f"{d_tarjeta[key]}: {card[key]}")
        return values

    def imprime_reportes(self, cards):
        """
        Genera un reporte para cada tarjeta que se la pasa a la función.
        :param cards: Lista con tarjetas en forma de diccionario.
        """
        for ind, card in enumerate(cards):
            print(f"\nTarjeta {ind + 1}:")
            if isinstance(card, dict):
                self.generar_reporte(True, card)
            else:
                self.generar_reporte(True, card.captura_nueva_deuda())

    def pago_recurrente(self, *args):
        """
        Función que construye una sucesión de pagos constantes y recurrentes para una tarjeta que
        no genera más cargos adicionales. Imprime los reportes mensuales.
        :param *args: Tarjeta en forma de diccionario.
        """
        card = args[0] if len(args) else self.captura_nueva_deuda()
        card['new_debt'] = (card['debt'] - card['payment'])*(1 + card['irate']/(12 * 100))
        if 'charges' in card:
            card['charges'] = 0

        print(f"\nMes 0: ")
        self.generar_reporte(True, card)

        i = 0
        while card['new_debt'] > 0:
            print(f"\nMes {i + 1}: ")
            card['debt'] = card['new_debt']
            card = self.captura_nueva_deuda(card)
            self.generar_reporte(True, card)
            i += 1


    def pagos_multiples(self, pagos, *args):
        """
        Función que proyecta múltiples pagos distintos sobre una tarjeta a través de los meses.
        :param pagos: Lista de pagos a aplicar a la tarjeta.
        :param *args: Diccionario con las características de la tarjeta.
        """
        card = args[0] if len(args) else self.captura_nueva_deuda()
        print(f"\nMes 1: ")
        card['payment'] = pagos[0]
        card = self.captura_nueva_deuda(card)
        self.generar_reporte(True, card)

        for i, p in enumerate(pagos[1:]):
            print(f"\nMes {i + 2}: ")
            card['payment'] = p
            card['debt'] = card['new_debt']
            card = self.captura_nueva_deuda(card)
            self.generar_reporte(True, card)
            if card['new_debt'] == 0:
                break

    def card_to_json(self, json_file, *args):
        """
        Método que convierte la información de la tarjeta a un archivo .json.
        :param json_file: Nombre del archivo con extensión .json a guardar
        """

        d_tarjeta = {'Card_name': 'Tarjeta', 'irate': 'Tasa', 'debt': 'Deuda',
                    'payment': 'Pago', 'charges': 'Cargos', 'new_debt': 'Nueva Deuda'}
        card = args[0] if len(args) else self.captura_nueva_deuda()
        Card = {d_tarjeta[key]: card[key] for key in card}

        with open(f"{json_file}.json", "w") as fjson:
            json.dump(Card, fjson, indent=4)

    def json_to_card(self, json_file, replace):
        """
        Método que lee un archivo .json y lo almacena en un objeto.
        :param json_file: Nombre del archivo .json a leer
        :param replace: Indica si se reemplaza la información de la tarjeta
        o se crea una nueva.
        """

        abspath = os.path.abspath(f"{json_file}.json")
        try:
            with open(abspath, 'r') as fjson:
                json_c = json.load(fjson)
        except FileNotFoundError:
            print("El archivo solicitado no existe. Favor de verificarlo.")
            return None
        else:
            values = list(json_c.values())
            if replace:
                self.__card_name = values[0]
                self.__irate = values[1]
                self.__debt = values[2]
                self.__payment = values[3]
                self.__charges = values[4]
            else:
                return tarjeta_credito(values[0], values[1], values[2], values[3], values[4])
