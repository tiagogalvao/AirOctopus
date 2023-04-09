import subprocess

from main.appData import AppData


class Helper:
    def __init__(self, params: AppData):
        self.appData = params

    def execute_command(self, command):
        if self.appData.isVerbose:
            separator = ' '
            print(separator.join(command))

        subprocess.run(command)
