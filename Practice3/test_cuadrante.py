def test_cuadrante4():
    x = 34
    y = -12
    if (x > 0 and y > 0):
        n = 1
        return n
    elif (x < 0 and y > 0):
        n = 2
        return n
    elif (x < 0 and y < 0):
        n = 3
        return n
    elif (x > 0 and y < 0):
        n = 4
        return n
    else:
        n = 0
    assert 4

def test_cuadrante3():
    x = -34
    y = -12
    if (x > 0 and y > 0):
        n = 1
        return n
    elif (x < 0 and y > 0):
        n = 2
        return n
    elif (x < 0 and y < 0):
        n = 3
        return n
    elif (x > 0 and y < 0):
        n = 4
        return n
    else:
        n = 0
    assert 3

def test_cuadrante2():
    x = -34
    y = 12
    if (x > 0 and y > 0):
        n = 1
        return n
    elif (x < 0 and y > 0):
        n = 2
        return n
    elif (x < 0 and y < 0):
        n = 3
        return n
    elif (x > 0 and y < 0):
        n = 4
        return n
    else:
        n = 0
    assert 2

def test_cuadrante1():
    x = 34
    y = 12
    if (x > 0 and y > 0):
        n = 1
        return n
    elif (x < 0 and y > 0):
        n = 2
        return n
    elif (x < 0 and y < 0):
        n = 3
        return n
    elif (x > 0 and y < 0):
        n = 4
        return n
    else:
        n = 0
    assert 2