import random

class ArtificialDataGenerator():
    def __init__(self):
        self.counter = 1
        self.max = 100
        self._fluid = ['oil', 'gas', 'water']

    def __iter__(self):

        return self

    def __next__(self):
        if self.counter < 4:
            if self.counter == 3:
                el = self._fluid[0]
                val = self.max
                self.counter += 1
                return (el, val)
            el = self._fluid.pop(random.randint(0, len(self._fluid) - 1))
            val = random.randint(0, self.max)
            self.max -= val
            self.counter += 1
            return (el, val)

        else:
            self.counter = 1
            self.max = 100
            self._fluid = ['oil', 'gas', 'water']
            raise StopIteration
    def gen_data(self,  number_of_wells: int):
        wells = []
        for well in range(number_of_wells):
            data = []
            for min in range(random.randint(5, 8) * 60):
                tmp = {'min': min}
                for g in self:
                    tmp[g[0]] = g[1]
                data.append(tmp)
            wells.append(data)
        return wells


