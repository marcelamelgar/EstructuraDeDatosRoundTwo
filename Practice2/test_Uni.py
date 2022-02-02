import numpy as np

def test_promedio():
    cuenta = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22])
    prueba = np.sum(cuenta) / cuenta.size
    assert prueba == 17.473

def test_sumDebitos():
    debitos = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22])
    suma = np.sum(debitos)
    assert suma == 174.73

def test_sumCreditos():
    creditos = np.array([100,200,300,400,500])
    suma = np.sum(creditos)
    assert suma == 1500

def test_saldo():
    debitos = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22])
    creditos = np.array([100,200,300,400,500])
    prueba = np.sum(creditos) - np.sum(debitos)
    assert prueba == 1325.27

def test_maximo():
    debitos = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22])
    prueba = np.max(debitos)
    assert prueba == 66.75

def test_cantidad():
    debitos = np.array([12.55, 23.99, 66.75, 10.15, 9.99, 5.50, 0.99, 8.35, 16.24, 20.22])
    creditos = np.array([100,200,300,400,500])
    pruebad = debitos.size
    pruebac = creditos.size
    assert pruebad == 10 
    assert pruebac == 5