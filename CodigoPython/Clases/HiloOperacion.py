import threading

class MiHilo(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.capital = args[0]
        self.stop = args[1]
        self.profit = args[2]
        self.subida = args[3]
        self.bajada = args[4]
        self.criptomoneda = args[5]


    def run(self):
        threading.current_thread().setName("Hilo 1:")
        print(self.capital)
        print(self.stop)
        print(self.profit)
        print(self.subida)
        print(self.bajada)
        print(self.criptomoneda)

