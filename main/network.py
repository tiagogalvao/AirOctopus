from main.appOptions import AppOptions


class Network:
    def __init__(self, options: AppOptions):
        self.Channel = ''
        self.Clients = 0
        self.MAC = ''
        self.Name = ''
        self.Power = ''
        self.WpsStatus = ''
