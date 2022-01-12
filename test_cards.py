from paquete.tarjeta import *
from paquete.Usuario import *
from paquete.tarjeta_servicios import *
import json

"""TARJETA DE CREDITO"""
def test_tarjeta_parametros():
    card = tarjeta_credito('BBVA', 10, 3000, 250, 150)
    assert card.get_card_name() == 'BBVA'
    assert card.get_irate() == 10
    assert card.get_debt() == 3000
    assert card.get_payment() == 250
    assert card.get_charges() == 150

def test_crea_tarjeta():
    card = tarjeta_credito('ABC', 15, 4500, 625, 280).crea_tarjeta()
    assert card['Card_name'] == 'ABC'
    assert card['irate'] == 15
    assert card['debt'] == 4500
    assert card['payment'] == 625
    assert card['charges'] == 280

def test_captura_nueva_deuda():
    card = tarjeta_credito('ABC', 15, 4500, 625, 280).captura_nueva_deuda()
    monthly_irate = card['irate']/(12 * 100)
    rec_debt = (card['debt'] - card['payment'])
    rec_debt = rec_debt*(1 + monthly_irate) if rec_debt >= 0 else rec_debt
    assert card['new_debt'] == 4203.4375

def test_json():
    my_card = {"Tarjeta": "ABC",
          "Tasa": 12,
          "Deuda": 2500,
          "Pago": 800,
          "Cargos": 210}

    with open("card.json", "w") as fjson:
        json.dump(my_card, fjson, indent=4)

    card = tarjeta_credito('BBVA', 10, 3000, 250, 150)
    card.json_to_card('card', True)
    Card = card.crea_tarjeta()
    assert Card['Card_name'] == 'ABC'
    assert Card['irate'] == 12
    assert Card['debt'] == 2500
    assert Card['payment'] == 800
    assert Card['charges'] == 210

"""TARJETA DE SEVICIOS"""
def test_tarjeta_servicios():
    card = tarjeta_de_servicios('INBURSA', 1500).crea_tarjeta()
    assert card['Card_name'] == 'INBURSA'
    assert card['irate'] == 0
    assert card['debt'] == 1500
    assert card['payment'] == 1500
    assert card['charges'] == 0


"""CREACION DE USUARIOS"""
def test_user():
    card_2 = tarjeta_credito('BANORTE', 15, 2000, 850, 420)
    card_3 = tarjeta_credito('SANTANDER', 6, 1200, 1100, 25)
    cards = [card_2, card_3]
    user = usuario('Alberto Rios', cards)
    values = user.__str__(False)

    assert values[0] == f"No. tarjetas: {2}"
    name_cards = ['BANORTE', 'SANTANDER']
    for i, card in enumerate(name_cards):
        assert values[i + 1] == f"Tarjeta {i + 1}: {card}."

def test_add_card():
    card_2 = tarjeta_credito('BANORTE', 15, 2000, 850, 420)
    card_3 = tarjeta_credito('SANTANDER', 6, 1200, 1100, 25)
    card_4 = tarjeta_credito('BBVA', 10, 4000, 1250, 150)

    cards = [card_2, card_3]
    user = usuario('Alberto Rios', cards)
    user.add_card(card_4)
    values = user.__str__(False)

    assert values[0] == f"No. tarjetas: {3}"
    assert values[-1] == f"Tarjeta {3}: {'BBVA'}."


def test_remove_card():
    card_2 = tarjeta_credito('BANORTE', 15, 2000, 850, 420)
    card_3 = tarjeta_credito('SANTANDER', 6, 1200, 1100, 25)
    card_4 = tarjeta_credito('BBVA', 10, 4000, 1250, 150)

    cards = [card_2, card_3, card_4]
    user = usuario('Alberto Rios', cards)
    user.remove_card(1)
    values = user.__str__(False)

    assert values[0] == f"No. tarjetas: {2}"
    name_cards = ['BANORTE', 'BBVA']
    for i, card in enumerate(name_cards):
        assert values[i + 1] == f"Tarjeta {i + 1}: {card}."

# python3 -m pytest -v test_cards.py