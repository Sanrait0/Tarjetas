from paquete.tarjeta import tarjeta_credito

class tarjeta_de_servicios(tarjeta_credito):
    """
    Tipo especial de tarjeta de crédito que solamente permite realizar pagos totales de la deuda y,
    por lo tanto, no aplica una tasa de interés sobre saldos remanentes.
    """

    def __init__(self, card_name, debt):
        """
        Inicializamos con irate, charges en cero y payment = debt.
        """
        super().__init__(card_name, 0, debt, debt, 0)


    def decorador(funcion):
        def nueva_funcion(*args, **kwargs):
            print("ADVERTENCIA: Solo se pueden aplicar pagos totales (por el valor de la deuda) a este tarjeta.")
            funcion(*args, **kwargs)
        return nueva_funcion

    @decorador
    def pago_recurrente(self, *args):
        """
        Función que construye una sucesión de pagos constantes y recurrentes para una tarjeta que
        no genera más cargos adicionales. En este caso solo lo hará para un pago total.
        :param *args: Tarjeta en forma de diccionario.
        """
        card = args[0] if len(args) else self.captura_nueva_deuda()
        card['new_debt'] = (card['debt'] - card['payment'])*(1 + card['irate']/(12 * 100))
        if 'charges' in card:
            card['charges'] = 0

        self.generar_reporte(card)

    @decorador
    def pagos_multiples(self, *args):
        """
        Función que proyecta múltiples pagos distintos sobre una tarjeta a través de los meses.
        En este caso, solo aplica 1 pago y es igual al monto de la deuda.
        :param pagos: Lista de pagos a aplicar a la tarjeta.
        :param *args: Diccionario con las características de la tarjeta.
        """
        card = args[0] if len(args) else self.captura_nueva_deuda()
        print(f"\nMes 1: ")
        card = self.captura_nueva_deuda(card)
        self.generar_reporte(card)
