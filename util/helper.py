import subprocess

from main.appData import AppData


class Helper:
    def __init__(self, app_data: AppData):
        self.appData = app_data

    def execute_command(self, command):
        if self.appData.isVerbose:
            separator = ' '
            self.output_text(separator.join(command))
        subprocess.run(command)

    def output_text(self, *text):
        separator = ' '
        text = separator.join(text) + '&10&40'
        for switch, value in self.appData.font_switches.items():
            text = text.replace(switch, value)
        print(text)
