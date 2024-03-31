import pickle
from datetime import datetime
from time import sleep


class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()
        state['saved'] = datetime.now()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.restored = datetime.now()


if __name__ == '__main__':
    r = RememberAll(1, 2, 3, 4)
    r_dump = pickle.dumps(r)
    sleep(1)
    r_load = pickle.loads(r_dump)
    print(r_load.saved, r_load.restored)


