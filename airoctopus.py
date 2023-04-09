#!/usr/bin/env python3
import click

from main.appData import AppData
from tools import ipTool, iwTool, iwconfigTool
from util.osUtils import OsUtils


class AirOctopus:
    def __init__(self, params: AppData):
        self.appData = params
        self.ipTool = ipTool.IpTool(params)
        self.iwTool = iwTool.IwTool(params)
        self.iwconfigTool = iwconfigTool.IwconfigTool(params)
        self.osUtils = OsUtils(params)

    def start(self):
        self.print_leet_banner()
        self.osUtils.check_platform()
        self.osUtils.check_privileges()

    @staticmethod
    def print_leet_banner():
        print('\n\n')
        print('       _    _       ___       _                        ')
        print('      / \  (_)_ __ / _ \  ___| |_ ___  _ __  _   _ ___ ')
        print("     / _ \ | | '__| | | |/ __| __/ _ \| '_ \| | | / __|")
        print('    / ___ \| | |  | |_| | (__| || (_) | |_) | |_| \__ \\')
        print('   /_/   \_\_|_|   \___/ \___|\__\___/| .__/ \__,_|___/')
        print('                                      |_|              ')
        print('\n\n')


@click.command()
def run_app():
    # Create an instance of the AppParams dataclass
    params = AppData()

    # Create an instance of the MyApp class with the AppParams dataclass instance as a parameter
    my_app = AirOctopus(params)

    # Run the application by calling the process method of the MyApp instance
    my_app.start()


# TODO: Remove this at some point
# @click.command()
# @click.argument('required_param_1', type=str)
# @click.argument('required_param_2', type=int)
# @click.option('--optional_param_1', type=float, help='An optional parameter of type float')
# @click.option('--optional_param_2', type=bool, help='An optional parameter of type bool')
# def run_app(required_param_1, required_param_2, optional_param_1=None, optional_param_2=None):
#     # Create an instance of the AppParams dataclass
#     params = AppData(required_param_1, required_param_2, optional_param_1, optional_param_2)
#
#     # Create an instance of the MyApp class with the AppParams dataclass instance as a parameter
#     my_app = AirOctopus(params)
#
#     # Run the application by calling the process method of the MyApp instance
#     my_app.start()


if __name__ == '__main__':
    run_app()
