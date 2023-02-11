# -*- coding: utf-8 -*-


class State:

    def __init__(self, mashine):
        self.mashine = mashine

    def insert_quarter(self):
        raise NotImplementedError()

    def eject_quarter(self):
        raise NotImplementedError()

    def turn_crank(self):
        raise NotImplementedError()

    def dispense(self):
        raise NotImplementedError()


class NoQuarterState(State):

    def insert_quarter(self):
        print('Вы положили монетку')
        new_state = HasQuarterState(mashine=self.mashine)
        self.mashine.state = new_state

    def eject_quarter(self):
        print('Нет монетки')

    def turn_crank(self):
        print('Нельзя повернуть - нет монеты')

    def dispense(self):
        print('Вы должны сначала заплатить')


class SoldOutState(State):

    def insert_quarter(self):
        print('Нет больше жевачек, обратитесь к администратору')

    def eject_quarter(self):
        print('Нет больше жевачек, обратитесь к администратору')

    def turn_crank(self):
        print('Нет больше жевачек, обратитесь к администратору')

    def dispense(self):
        print('Нет больше жевачек, обратитесь к администратору')


class SoldState(State):

    def insert_quarter(self):
        print('Пожалуста ждите, мы уже выдаем вам жевачку')

    def eject_quarter(self):
        print('Извините, вы уже повернули рычаг')

    def turn_crank(self):
        print('Повторное поворачивание не даст вам еще одну жевачку!!!')

    def dispense(self):
        if self.mashine.number_gumballs > 0:
            print('Вот ваша жевачка!!!')
            self.mashine.number_gumballs -= 1
            new_state = NoQuarterState(mashine=self.mashine)
            self.mashine.state = new_state
        else:
            print('Извините, все продано...')
            new_state = SoldOutState(mashine=self.mashine)
            self.mashine.state = new_state


class HasQuarterState(State):

    def insert_quarter(self):
        print('Вы не можете вставить другую монету')

    def eject_quarter(self):
        print('Монетка возвращена')
        new_state = NoQuarterState(mashine=self.mashine)
        self.mashine.state = new_state

    def turn_crank(self):
        print('Вы повернули рычаг, можно забирать жевачку')
        new_state = SoldState(mashine=self.mashine)
        self.mashine.state = new_state

    def dispense(self):
        print('Нет жевачки для выдачи... Возможно вам нужно повернуть рычаг.')


class GumballMashine:

    def __init__(self, number_gumballs):
        self.number_gumballs = number_gumballs
        self.state = NoQuarterState(mashine=self)

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()

    def dispense(self):
        self.state.dispense()


mash = GumballMashine(number_gumballs=2)

mash.insert_quarter()
mash.turn_crank()
mash.dispense()

mash.insert_quarter()
mash.turn_crank()
mash.dispense()

mash.insert_quarter()
mash.turn_crank()
mash.dispense()

mash.insert_quarter()
mash.turn_crank()
mash.dispense()
