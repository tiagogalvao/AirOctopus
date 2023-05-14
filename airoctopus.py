#!/usr/bin/env python3
import atexit
import time

import click
import elevate
import re
import sys

from internals.appContext import AppContext
from internals.appOptions import AppOptions
from internals.appSettings import AppSettings
from main.wifiScanner import WiFiScanner
from model.wifiInterface import WifiInterface
from tools import ipTool, iwTool, iwconfigTool, iwlistTool
from ui.networksTable import NetworksTable
from util.helper import Helper
from util.osUtils import OsUtils


class AirOctopus:
    def __init__(self, options: AppOptions):
        # Registering exit event
        atexit.register(self.exit_gracefully)

        # Main initialization
        self.app_context = AppContext()
        self.app_options = options
        self.app_settings = AppSettings()
        self.helper = Helper(self.app_options, self.app_settings)

        # Tools initialization
        self.ip_tool = ipTool.IpTool(self.helper)
        self.iw_tool = iwTool.IwTool(self.helper)
        self.iwconfig_tool = iwconfigTool.IwconfigTool(self.helper)
        self.iwlist_tool = iwlistTool.IwlistTool(self.helper)

        # Utils initialization
        self.ui_networks = NetworksTable(self.app_context, self.helper)
        self.os_utils = OsUtils(self.app_context, self.app_settings, self.helper)

    def start(self):
        try:
            elevate.elevate(graphical=False)
            self.print_leet_banner()
            self.os_utils.check_platform()
            self.os_utils.preload_system_data()
            self.print_interface_selection()

            if len(self.app_context.iface_selected_wifi_interfaces) > 0:
                for iface in self.app_context.iface_selected_wifi_interfaces:
                    iface.enable_mode_monitor()

            print('\n\n')
            scanners = []
            for item in self.app_context.iface_selected_wifi_interfaces:
                scanner = WiFiScanner(self.app_context, self.helper, self.iwlist_tool, item, 0.5)
                scanners.append(scanner)

            while True:
                for item in scanners:
                    item.start_scan()

                self.ui_networks.print()
                # network = model.network.Network(self.helper)
                # self.app_context.network_list.append(network)
                time.sleep(0.5)

        except KeyboardInterrupt:
            print('\n')
            self.helper.print_text_warning(self.app_settings.app_name, 'has been aborted.')
        # except Exception as e:
        #     print('')
        #     if self.app_options.is_verbose:
        #         self.helper.print_text_error(e)
        finally:
            print('')

    def print_leet_banner(self):
        banner = '&30&01\n\n'
        banner += '       _    _       ___       _                        \n'
        banner += '      / \\  (_)_ __ / _ \\  ___| |_ ___  _ __  _   _ ___ \n'
        banner += "     / _ \\ | | '__| | | |/ __| __/ _ \\| '_ \\| | | / __|\n"
        banner += '    / ___ \\| | |  | |_| | (__| || (_) | |_) | |_| \\__ \\\n'
        banner += '   /_/   \\_\\_|_|   \\___/ \\___|\\__\\___/| .__/ \\__,_|___/\n'
        banner += '                                      |_|              \n'
        banner += '\n\n'
        self.helper.print_text(banner)

    def print_interface_selection(self):
        self.query_interfaces_and_store_data()
        if len(self.app_context.iface_system_wifi_interfaces) > 0:
            print('')
            self.helper.print_text('Available interfaces:')
            for index, item in enumerate(self.app_context.iface_system_wifi_interfaces):
                self.helper.print_text(f'{index+1}: {item}')

            selection = input(f'\n  Select from [1-{len(self.app_context.iface_system_wifi_interfaces)}]'
                              f', using comma-separated input: ')
            if re.match(r'^[\d,]+$', selection):
                numbers = [int(x) for x in selection.split(',')]
                numbers = list(set(numbers))
                for n in numbers:
                    if n > 0 and n <= len(self.app_context.iface_system_wifi_interfaces):
                        self.app_context.iface_selected_wifi_interfaces\
                            .append(self.app_context.iface_system_wifi_interfaces[n-1])

                if len(self.app_context.iface_selected_wifi_interfaces) < 1:
                    print()
                    self.helper.print_text_information('No valid wireless interfaces have been selected.')
                    sys.exit(0)
            else:
                print()
                self.helper.print_text_warning('Invalid selection. Please, use only comma-separated numbers.')
                sys.exit(0)
        else:
            print()
            self.helper.print_text_information('No wireless interfaces have been found.')
            sys.exit(0)

    def query_interfaces_and_store_data(self):
        if self.app_options.use_iwconfig:
            interfaces = self.iwconfig_tool.list_interfaces()
        else:
            interfaces = self.iw_tool.list_interfaces()

        for interface in interfaces:
            iface = WifiInterface(interface, self.app_options, self.helper, self.os_utils,
                                  self.ip_tool, self.iw_tool, self.iwconfig_tool, self.iwlist_tool)
            self.app_context.iface_system_wifi_interfaces.append(iface)

    def exit_gracefully(self, signum=None, frame=None):
        self.helper.print_text_warning('Shutting down gracefully... please wait.')
        self.exit_iface_cleaning()

    def exit_iface_cleaning(self):
        if not self.app_options.iface_keep_monitor:
            if len(self.app_context.iface_selected_wifi_interfaces) > 0:
                for iface in self.app_context.iface_selected_wifi_interfaces:
                    if iface.InModeMonitor:
                        iface.disable_mode_monitor()


@click.command()
@click.option('--keep-monitor', is_flag=True, help='Keep interfaces in monitor-mode after quitting')
@click.option('--use-iwconfig', is_flag=True, help='Force the use of iwconfig instead of iw')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose mode')
def run_app(keep_monitor, use_iwconfig, verbose):
    options = AppOptions()
    options.is_verbose = verbose
    options.iface_keep_monitor = keep_monitor
    options.use_iwconfig = use_iwconfig
    octopus = AirOctopus(options)
    octopus.start()


if __name__ == '__main__':
    run_app()
