#!/usr/bin/env python3
import atexit
import click
import signal

from main.appOptions import AppOptions
from main.appSettings import AppSettings
from main.wifiInterface import WifiInterface
from tools import ipTool, iwTool, iwconfigTool
from util.helper import Helper
from util.osUtils import OsUtils


class AirOctopus:
    def __init__(self, options: AppOptions):
        # Registering exit events
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGINT, self.exit_gracefully)
        atexit.register(self.exit_gracefully)

        # Main initialization
        self.app_options = options
        self.app_settings = AppSettings()
        self.helper = Helper(self.app_options, self.app_settings)

        # Tools initialization
        self.ip_tool = ipTool.IpTool(self.helper)
        self.iw_tool = iwTool.IwTool(self.helper)
        self.iwconfig_tool = iwconfigTool.IwconfigTool(self.helper)

        # Utils initialization
        self.os_utils = OsUtils(self.app_settings, self.helper)

    def start(self):
        self.print_leet_banner()
        self.os_utils.check_platform()
        self.os_utils.check_privileges()
        self.print_interface_selection()

        iface1 = WifiInterface(self.app_options, self.helper, self.ip_tool, self.iw_tool, self.iwconfig_tool)
        iface1.Name = 'wlan1'
        iface1.enable_mode_monitor()
        iface1.disable_mode_monitor()

    def print_leet_banner(self):
        banner = '\n&30&01'
        banner += '       _    _       ___       _                        \n'
        banner += '      / \\  (_)_ __ / _ \\  ___| |_ ___  _ __  _   _ ___ \n'
        banner += "     / _ \\ | | '__| | | |/ __| __/ _ \\| '_ \\| | | / __|\n"
        banner += '    / ___ \\| | |  | |_| | (__| || (_) | |_) | |_| \\__ \\\n'
        banner += '   /_/   \\_\\_|_|   \\___/ \\___|\\__\\___/| .__/ \\__,_|___/\n'
        banner += '                                      |_|              \n'
        banner += '\n\n'
        self.helper.print_text(banner)

    def print_interface_selection(self):
        interfaces = self.query_interfaces()
        for iface in interfaces:
            print(iface)

    def query_interfaces(self):
        if self.app_options.use_iwconfig:
            interfaces = self.iwconfig_tool.list_interfaces()
        else:
            interfaces = self.iw_tool.list_interfaces()
        return interfaces

    def exit_gracefully(self, signum=None, frame=None):
        self.helper.print_text('Shutting down gracefully...', 'Sig:', signum, 'Frame:', frame)


@click.command()
@click.option('--use-iwconfig', is_flag=True, help='Force the use of iwconfig instead of iw')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose mode')
def run_app(use_iwconfig, verbose):
    options = AppOptions()
    options.is_verbose = verbose
    options.use_iwconfig = use_iwconfig

    octopus = AirOctopus(options)
    octopus.start()


if __name__ == '__main__':
    run_app()
