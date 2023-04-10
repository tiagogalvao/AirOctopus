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
            self.print_text_verbose_command(separator.join(command))
        subprocess.run(command)

    def execute_command_with_result(self, command):
        if self.app_options.is_verbose:
            separator = ' '
            self.print_text_verbose_command(separator.join(command))
        return subprocess.check_output(command, stderr=subprocess.DEVNULL, universal_newlines=True)

    def __print_text(self, *text):
        separator = ' '
        text = separator.join([word for word in text if word is not None])
        for switch, value in self.app_settings.font_switches.items():
            text = text.replace(switch, value)
        print('', text)

    def print_text(self, *text):
        result = prepare_text(text)
        self.__print_text(f' {result}')

    def print_text_verbose_command(self, *command):
        result = prepare_text(command)
        self.__print_text(' &01&30[V] Executing command:&02&36', result)

    def print_text_information(self, *text):
        result = prepare_text(text)
        self.__print_text(' &01&36[ Info ]&02&37', result)

    def print_text_warning(self, *text):
        result = prepare_text(text)
        self.__print_text(' &01&33[Warning]&02&37', result)

    def print_text_error(self, *text):
        result = prepare_text(text)
        self.__print_text(' &01&31[ ERROR ]&02&37', result.capitalize())

    @staticmethod
    def string_equals_ignore_case(str1, str2):
        return str1.casefold() == str2.casefold()

    @staticmethod
    def string_contains_ignore_case(value, value_to_search):
        return value_to_search.casefold() in value.casefold()


def prepare_text(text):
    separator = ' '
    return separator.join([str(word) for word in text if word is not None]) + '&10&40'
