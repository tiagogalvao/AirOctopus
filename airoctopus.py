#!/usr/bin/env python3
import sys

import click
import os
import platform

from main.AppData import AppData
from util.StringUtils import StringUtils


class AirOctopus:
    __appName = "AirOctopus"
    __appVersion = "0.0.1"

    def __init__(self, params: AppData):
        self.params = params

    def start(self):
        self.print_leet_banner()
        self.check_platform()
        self.check_privileges()

        # Mock the use of the parameters to process something
        # print(f"Processing {self.params.required_param_1} with {self.params.required_param_2} and optional param 1 = {self.params.optional_param_1} and optional param 2 = {self.params.optional_param_2}")

    @staticmethod
    def print_leet_banner():
        print("\n\n")
        print("       _    _       ___       _                        ")
        print("      / \  (_)_ __ / _ \  ___| |_ ___  _ __  _   _ ___ ")
        print("     / _ \ | | '__| | | |/ __| __/ _ \| '_ \| | | / __|")
        print("    / ___ \| | |  | |_| | (__| || (_) | |_) | |_| \__ \\")
        print("   /_/   \_\_|_|   \___/ \___|\__\___/| .__/ \__,_|___/")
        print("                                      |_|              ")
        print("\n\n")

    def check_platform(self):
        system = platform.system()
        if StringUtils.equals_ignore_case(system, "Linux"):
            if StringUtils.contains_ignore_case("Microsoft", platform.release()):
                print("Keep in mind that", self.__appName, "was not tested under WSL.")
            else:
                print(self.__appName, "is running under *Unix... good.")
        elif StringUtils.equals_ignore_case(system, "Windows"):
            print(self.__appName, "is running under Windows. This is not a really smart idea.")
            sys.exit(0)
        else:
            print("Unknown operating system detected. Bye.")
            sys.exit(0)

    def check_privileges(self):
        if os.geteuid() != 0:
            print("Information:", self.__appName, "is not running as root.\nYou will be asked for a password when privileges are needed.")
            sys.exit(0)


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