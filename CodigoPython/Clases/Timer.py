import threading
import time

class Timer(threading.Thread):
    def __init__(self):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()
    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)

    def stop(self):
        self._timer_runs.clear()

class HelloWorldTimer(Timer):
    interval = 3   # Intervalo en segundos.

    # Función a ejecutar.
    def timer(self):
        print("¡Hola, mundo!")

hello_world_timer = HelloWorldTimer()
hello_world_timer.start()   # Iniciar el timer.
time.sleep(10)
hello_world_timer.stop()    # Detenerlo.
