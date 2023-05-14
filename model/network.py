from util.helper import Helper


class Network:
    def __init__(self, helper: Helper):
        self.helper = helper
        self.Channel = 0
        self.Clients = 0
        self.MAC = '00:00:00:00:00:00'
        self.Name = 'Random name'
        self.Power = 50
        self.WpsStatus = False

    def __str__(self):
        return f'{self.Name}\t\t\t{self.MAC}\t\t{self.Channel}\t{self.Power}db'
