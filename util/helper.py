import subprocess

from main.appOptions import AppOptions
from main.appSettings import AppSettings


class Helper:
    def __init__(self, options: AppOptions, settings: AppSettings):
        self.app_settings = settings
        self.app_options = options

    def execute_command(self, command):
        if self.app_options.is_verbose:
            separator = ' '
            self.print_text(separator.join(command))
        subprocess.run(command)

    def execute_command_with_result(self, command):
        if self.app_options.is_verbose:
            separator = ' '
            self.print_text(separator.join(command))
        return subprocess.check_output(command, stderr=subprocess.DEVNULL, universal_newlines=True)

    def print_text(self, *text):
        separator = ' '
        text = separator.join([word for word in text if word is not None]) + '&10&40'
        for switch, value in self.app_settings.font_switches.items():
            text = text.replace(switch, value)
        print(text)

    @staticmethod
    def string_equals_ignore_case(str1, str2):
        return str1.casefold() == str2.casefold()

    @staticmethod
    def string_contains_ignore_case(value, value_to_search):
        return value_to_search.casefold() in value.casefold()
