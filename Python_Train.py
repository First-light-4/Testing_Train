class Train():

    def __init__(self, lokomotiv, carriage):
        if type(lokomotiv) not in [int] or carriage not in [int]:
            raise TypeError("Please enter correction data")
        self._lokomotiv = lokomotiv
        self.carriage = carriage


    def info(self):
        return f'Номер Локомотива: {self._lokomotiv}\nКолличество вагонов: {self.carriage}'

    def station(self, plus_minus_cargo):
        self.plus_minus_cargo = plus_minus_cargo
        self.carriage += self.plus_minus_cargo
        return self.carriage

class Cargo_carriage(Train):

    def __init__(self, lokomotiv, carriage, amount):
        super().__init__(lokomotiv, carriage)
        self.amount = amount

    def info_cargo(self):
        return self.amount

    # def station_car(self, plus_minus):
    #

class Passenger_carriage(Cargo_carriage):

    def __init__(self, lokomotiv, carriage, amount):
        super().__init__(lokomotiv, carriage)
        self.amount = amount

    def info_cpassenger(self):
        return self.amount