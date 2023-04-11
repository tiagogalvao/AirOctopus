import os
import platform
import re
import sys

from main.appSettings import AppSettings
from util.helper import Helper


class OsUtils:
    def __init__(self, settings: AppSettings, helper: Helper):
        self.app_settings = settings
        self.helper = helper

    def check_platform(self):
        system = platform.system()
        if self.helper.string_equals_ignore_case(system, 'Linux'):
            if self.helper.string_contains_ignore_case('Microsoft', platform.release()):
                self.helper.print_text('Keep in mind that', self.app_settings.app_name, 'was not tested under WSL.')
            else:
                self.helper.print_text(self.app_settings.app_name, 'is running under *Unix... good.')
        elif self.helper.string_equals_ignore_case(system, 'Windows'):
            self.helper.print_text(self.app_settings.app_name, 'is running under Windows. This is not a really smart idea.')
            sys.exit(0)
        else:
            self.helper.print_text('Unknown operating system detected. Bye.')
            sys.exit(0)

    def check_privileges(self):
        if os.geteuid() != 0:
            self.helper.print_text('Information:', self.app_settings.app_name, 'is not running as root. Good.')
            self.helper.print_text('You will be asked for a password when privileges are needed.\n')
        else:
            self.helper.print_text("You don't need to run this as root ;)\n")

    def check_iface_module(self, iface: str):
        command = ['ls', '-l', f'/sys/class/net/{iface}/device/driver']
        output = self.helper.execute_command_with_result(command)
        return output.replace('../', '').replace('\n', '').split('/')[-1]

    def check_iface_device(self, iface: str):
        iface_id = self.check_iface_usb_device(iface)
        if self.helper.string_equals_ignore_case('unknown', iface_id):
            iface_id = self.check_iface_pci_device(iface)
        return iface_id

    def check_iface_usb_device(self, iface: str):
        iface_id = self.check_iface_usb_id(iface)
        command = ['lsusb']
        output = self.helper.execute_command_with_result(command)
        regex_pattern = r'^.*\bID\s+' + str(iface_id) + r'\s+(.*)$'
        has_interface = re.search(regex_pattern, output, re.MULTILINE)
        if has_interface:
            name = has_interface.group(1).strip()
        else:
            name = 'Unknown'
        return name

    def check_iface_pci_device(self, iface: str):
        iface_id = self.check_iface_pci_id(iface)
        command = ['lspci']
        output = self.helper.execute_command_with_result(command)
        regex_pattern = r'^.*' + str(iface_id) + r'\s+(.*)$'
        has_interface = re.search(regex_pattern, output, re.MULTILINE)
        if has_interface:
            name = has_interface.group(1).strip()
        else:
            name = 'Unknown'
        return name

    def check_iface_usb_id(self, iface: str):
        command = ['cat', f'/sys/class/net/{iface}/device/uevent']
        output = self.helper.execute_command_with_result(command)
        has_product = re.search(r'^PRODUCT=(.*)$', output, re.MULTILINE)
        if has_product:
            product = has_product.group(1)
            product = product.split('/')
            product_id = f"{product[0].zfill(4)}:{product[1].zfill(4)}"
        else:
            product_id = 'Unknown'
        return product_id

    def check_iface_pci_id(self, iface: str):
        command = ['cat', f'/sys/class/net/{iface}/device/uevent']
        output = self.helper.execute_command_with_result(command)
        has_product = re.search(r'^PCI_SLOT_NAME=(.*)$', output, re.MULTILINE)
        if has_product:
            product = has_product.group(1)
            product = product.split(':')
            product_id = f"{product[1]}:{product[2]}"
        else:
            product_id = 'Unknown'
        return product_id
