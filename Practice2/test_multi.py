import numpy as np

def test_multiplica():
    costo = 12.75
    cantidad = 5
    precio = costo * cantidad
    assert precio == 63.75

def test_sumcompras():
    mult = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 7.99, 8.35, 16.24, 20.22])
    suma = np.sum(mult)
    assert suma == 181.73

def test_sumpagos():
    puni = np.array([0.50,12.35,25.05,0.99,1.75])
    sum1 = np.sum(puni)
    assert sum1 == 40.64

def test_saldo():
    mult = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 7.99, 8.35, 16.24, 20.22])
    puni = np.array([0.50,12.35,25.05,0.99,1.75])
    prueba = round(np.sum(mult) - np.sum(puni),2)
    assert prueba == 141.09

def test_caro():
    mult = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 7.99, 8.35, 16.24, 20.22])
    prueba = np.max(mult)
    assert prueba == 66.75