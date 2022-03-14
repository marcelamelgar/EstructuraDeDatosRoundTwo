import random 

class Queue:  
  
    def __init__(self):  
        self.queue = list()  
    
    def add_element(self,ingreso): 
        if ingreso not in self.queue:  
            self.queue.insert(0,ingreso)  
            return True  
        return False 
    

    def remove_element(self):  
        chosen = random.randint(0, len(self.queue)-1)
        if len(self.queue)>0:
            return self.queue.pop(chosen)  
        return ("None") 
  
def skey(TheQueue):
    return TheQueue['social']

def main():
    TheQueue = Queue()
    social = int(input("ingrese su numero social:\n"))
    nombre = str(input("ingrese su nombre:\n"))
    dias = int(input("ingrese la cantidad de dias que trabajo:\n"))
    TheQueue.add_element({"social":123,"nombre":"Marcela", "ds":5})
    TheQueue.add_element({"social":543,"nombre":"Isabel", "ds":3})
    TheQueue.add_element({"social":678,"nombre":"Jose", "ds":7})

    TheQueue.add_element({"social":social, "nombre":nombre, "ds":dias})
    TheQueue.queue.sort(key=skey)
    print("Queue: ")
    for i in TheQueue.queue:
        print("----------------------")
        print(i)

    for k in range(len(TheQueue.queue)):
        print("\nAsignacion: ")
        print(f"\n\trepartidor tomado: {TheQueue.remove_element()}")
        print("Queue: ")
        for i in TheQueue.queue:
            print("----------------------")
            print(i)
main()