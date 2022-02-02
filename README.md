# Estructura de Datos
En el repositorio se encuentran todos los proyectos, tareas y ejercicios en los que trabajé durante el transcurso de la clase de 'Estructura de Datos'. El lenguaje que utilicé fue Python.
En cada uno de los archivos se puede encontrar el código, un video de demostración de la ejecución, profiling y pruebas unitarias.

# Contenido
1. [Práctica 1](#Practica-1)
2. [Práctica 2] (#Practica-2)

# Practica 1
- Algoritmo en donde se puede calcular la suma de los primeros numeros de 'N' que el usuario ingrese.
- **Prueba Unitaria** unittest
- **Profiling** comando cProfile

## Cómo ejecutarlo?
1. Encontrar el file con el código del algoritmo
```
cd Practice1
cd sumNnumbers.py
```

2. Ejecutar el algoritmo
```
python3 sumNnumbers.py
```

3. Para realizar el Profiling ejecute lo siguiente
```
python3 -m cProfile sumNnumbers.py
```

4. Para realizar la Prueba Unitaria dirijase a el file en donde se encuentra el mismo
```
cd tests
cd pruebaUnitaria.py
```

5. Ejecute el algoritmo
```
python3 pruebaUnitaria.py
```

## Recursos
- https://realpython.com/python-testing/ 
- https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/ 


# Practica 2
- Algoritmo en donde se pueden hacer debitos y creditos. Permite ver la suma de los debitos y creditos, saldos pendientes, promedio de Débitos, el débito más grande, cantidad de operacionesrealizadas y elimitar créditos. Todo fue trabajado con arrays unidimensionales de numpy.
- Algoritmo en donde se pueden llevar a cabo compras y pagos y se obtiene un recibo de transacciones. Se puede ver la suma de las compras, pagos realizados y su metodo, un catalogo de productos con codigo, nombre y precio, saldo pendiente por pagar, producto mas caro, promedio de precios de los productos comprados y eliminar pago. Todo fuetrabajado con arrays multidimensionales de numpy.
- **Prueba Unitaria** pytest
- **Profiling** comando cProfile

## Cómo ejecutarlo?
### Unidimensionales
1. Encontrar el file con el código del algoritmo
```
cd Practice2
cd unidimensionales.py
```

2. Ejecutar el algoritmo
```
python3 unidimensionales.py
```

3. Para realizar el Profiling ejecute lo siguiente
```
python3 -m cProfile unidimensionales.py
```

4. Para realizar la Prueba Unitaria dirijase a el file en donde se encuentra el mismo
```
cd tests
cd test_Uni.py
```

5. Ejecute las pruebas
```
pytest
```
### Multidimensionales
1. Encontrar el file con el código del algoritmo
```
cd Practice2
cd multidimensionales.py
```

2. Ejecutar el algoritmo
```
python3 multidimensionales.py
```

3. Para realizar el Profiling ejecute lo siguiente
```
python3 -m cProfile multidimensionales.py
```

4. Para realizar la Prueba Unitaria dirijase a el file en donde se encuentra el mismo
```
cd tests
cd test_Multi.py
```

5. Ejecute las pruebas
```
pytest
```

## Recursos
- https://realpython.com/numpy-tutorial/
