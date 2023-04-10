#!/usr/bin/env python3
import atexit
import click
import signal

from main.appOptions import AppOptions
from tools import ipTool, iwTool, iwconfigTool
from util.helper import Helper
from util.osUtils import OsUtils

from main.wifiInterface import WifiInterface


class AirOctopus:
    def __init__(self, options: AppOptions):
        # Registering exit events
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGINT, self.exit_gracefully)
        atexit.register(self.exit_gracefully)

        # Starting/Loading things
        self.appOptions = options
        self.helper = Helper(options)
        self.ipTool = ipTool.IpTool(options, self.helper)
        self.iwTool = iwTool.IwTool(options, self.helper)
        self.iwconfigTool = iwconfigTool.IwconfigTool(options, self.helper)
        self.osUtils = OsUtils(options, self.helper)

    def start(self):
        self.print_leet_banner()
        self.osUtils.check_platform()
        self.osUtils.check_privileges()

        iface1 = WifiInterface(self.appOptions, self.helper, self.ipTool, self.iwTool, self.iwconfigTool)
        iface1.Name = 'wlan1'
        iface1.enable_mode_monitor()
        iface1.disable_mode_monitor()

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
@click.option('--use-iwconfig', is_flag=True, help='Force the use of iwconfig instead of iw')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose mode')
def run_app(use_iwconfig, verbose):
    params = AppOptions()
    params.isVerbose = verbose
    params.useIwconfig = use_iwconfig

    my_app = AirOctopus(params)
    my_app.start()


if __name__ == '__main__':
    # Start octopus
    run_app()
