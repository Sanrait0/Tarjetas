import random
import numpy as np
import names
import scipy.stats as stats
from paquete.tarjeta import *
from paquete.Usuario import *

def Genera_usuarios(n_user):
    """
    Función que genera un número específico de usuarios y hasta 10 tarjetas para cada uno.
    :param n_user: Número de usuarios a generar
    """

    'Diccionario de usuarios'
    Users = {}

    'Lista de bancos posibles'
    Bancos = ['ABC', 'American Express', 'Afirme', 'Mifel', 'Actinver', 'Autofin', 'Azteca', 'Bajio',
              'Inbursa', 'Invex', 'Multiva', 'BBVA', 'Santander', 'HSBC', 'BanCoppel', 'Citibanamex',
              'Scotianbank', 'CIBanco']

    Names = []
    for i in range(n_user):
        b = True
        while b:
            name = names.get_full_name()  # Nombre aleatorio de usuario
            short_name = name.split(' ')[0]
            if short_name not in Names:
                b = False
        Names.append(short_name)
        n_cards = random.randint(1, 8)  # Número aleatorio de tarjetas
        bank = random.sample(Bancos, n_cards)  # Muestreo aleatorio simple de bancos
        irate = np.random.randint(5, 40, size=n_cards)  # Tasa de interés para cada tarjeta
        debt = stats.gamma.rvs(size=n_cards, a=3, scale=1800)  # Distribución gamma con media = 5400 y desv = 3117.7
        payment = debt*stats.beta.rvs(size=n_cards, a=1.05, b=2)  # Distribución beta con media = 0.344 y var = 0.0557
        charges = debt*stats.beta.rvs(size=n_cards, a=1.05, b=2)**2

        'Tarjetas del usuario'
        cards = [tarjeta_credito(bank[c], irate[c], debt[c], payment[c], charges[c]) for c in range(n_cards)]

        'Creando usuario'
        Users[short_name] = usuario(name, cards)

    return Users