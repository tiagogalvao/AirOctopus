#!/usr/bin/env python3
import atexit
import click
import signal

from main.appData import AppData
from tools import ipTool, iwTool, iwconfigTool
from util.helper import Helper
from util.osUtils import OsUtils


class AirOctopus:
    def __init__(self, app_data: AppData):
        # Registering exit events
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGINT, self.exit_gracefully)
        atexit.register(self.exit_gracefully)

        # Starting/Loading things
        self.appData = app_data
        self.helper = Helper(app_data)
        self.ipTool = ipTool.IpTool(app_data)
        self.iwTool = iwTool.IwTool(app_data)
        self.iwconfigTool = iwconfigTool.IwconfigTool(app_data)
        self.osUtils = OsUtils(app_data, self.helper)

    def start(self):
        self.print_leet_banner()
        self.osUtils.check_platform()
        self.osUtils.check_privileges()

    def print_leet_banner(self):
        banner = '\n\n&30&01'
        banner += '       _    _       ___       _                        \n'
        banner += '      / \  (_)_ __ / _ \  ___| |_ ___  _ __  _   _ ___ \n'
        banner += "     / _ \ | | '__| | | |/ __| __/ _ \| '_ \| | | / __|\n"
        banner += '    / ___ \| | |  | |_| | (__| || (_) | |_) | |_| \__ \\\n'
        banner += '   /_/   \_\_|_|   \___/ \___|\__\___/| .__/ \__,_|___/\n'
        banner += '                                      |_|              \n'
        banner += '\n\n'
        self.helper.print_text(banner)

    def exit_gracefully(self, signum=None, frame=None):
        self.helper.print_text('Shutting down gracefully...', 'Sig:', signum, 'Frame:', frame)


@click.command()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose mode')
def run_app(verbose):
    params = AppData()
    params.isVerbose = verbose
    my_app = AirOctopus(params)
    my_app.start()


if __name__ == '__main__':
    # Start octopus
    run_app()
