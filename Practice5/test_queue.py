from queue import Queue

def test_add_element():
    TheQueue = Queue()
    TheQueue.add_element({"social":123,"nombre":"Marcela", "ds":5})
    assert TheQueue.queue == ({"social":123,"nombre":"Marcela", "ds":5})

def test_remove_element():
    TheQueue = Queue()
    TheQueue.remove_elementt({"social":123,"nombre":"Marcela", "ds":5})
    assert TheQueue.queue == "None"