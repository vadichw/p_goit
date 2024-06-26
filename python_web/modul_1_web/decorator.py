import datetime


class Event:
    _observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self._observers:
            observer(event, data)


def logger(event, data):
    print(event, data)


class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, 'w') as file:
            file.write(f"{datetime.datetime.now()}: {event} - {data}")


if __name__ == '__main__':
    event = Event()
    event.register(logger)
    fl = FileLogger('logs.log')
    event.register(fl)

    event.notify('TICK', 65)
    event.notify('TICK', 84)
    event.notify('ERROR', 'Fatal Error')

    event.unregister(fl)
    event.notify('TICK', 65)
                                                                                                                                                                            