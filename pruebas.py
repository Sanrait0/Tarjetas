import random
from paquete.tarjeta import *
from paquete.Usuario import *
from paquete.tarjeta_servicios import *
import json
from Genera_usuarios import Genera_usuarios

card_1 = tarjeta_credito('BBVA', 0, 3000, 250, 150)
card_2 = tarjeta_credito('BANORTE', 15, 2000, 850, 420)
card_3 = tarjeta_credito('SANTANDER', 6, 1200, 1100, 25)
card_5 = tarjeta_credito('BBVA', 10, 4000, 1250, 150)

my_card = {"Tarjeta": "ABC",
          "Tasa": 12,
          "Deuda": 2500,
          "Pago": 800,
          "Cargos": 210}


ejemplo = 'json'

if ejemplo == 'card':
    #d_card1 = card_1.captura_nueva_deuda()
    #d_card2 = card_2.captura_nueva_deuda()

    card_1.pagos_multiples([200, 400, 300, 400, 800, 500, 1000, 400])
    #card_1.generar_reporte()
    #card_2.__str__()
    #print(card_3.get_card_name())
elif ejemplo == 'user':
    cards = [card_1, card_2]
    user = usuario('ALBERTO', cards)
    user.add_card(card_3)
    user.remove_card(1)
    user.__str__()
elif ejemplo == 'servicio':
    card_4 = tarjeta_de_servicios('INBURSA', 1500)
    #card_4.generar_reporte()
    #card_4.pago_recurrente()
    card_4.pagos_multiples()
elif ejemplo == 'json':
    with open("card.json", "w") as fjson:
        json.dump(my_card, fjson, indent=4)

    card_1.generar_reporte()
    card_1.json_to_card('card', True)
    card_1.generar_reporte()
elif ejemplo == 'genera':
    n_user = random.randint(1, 8)  # Número aleatorio de usuarios
    Users = Genera_usuarios(n_user)
    for k in Users:
        cards = [c.get_card_name() for c in Users[k].get_cards()]
        print(cards)
        #print(Users[k]['short_name'])
elif ejemplo == 'imprime':
    L = [card_1, card_2]
    card_1.imprime_reportes(L)
elif ejemplo == 'recurrente':
    card_1.pago_recurrente()

