import os
import platform
import re
import sys

from elevate import elevate

from internals.appContext import AppContext
from internals.appSettings import AppSettings
from util.helper import Helper


class OsUtils:
    def __init__(self, context: AppContext, settings: AppSettings, helper: Helper):
        self.app_context = context
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
            self.helper.print_text(self.app_settings.app_name, 'is running under Windows..... .. ..')
            sys.exit(0)
        else:
            self.helper.print_text('Unknown operating system detected. Bye.')
            sys.exit(0)

    def check_privileges(self):
        return os.geteuid()

    def preload_system_data(self):
        self.app_context.output_lspci = self.helper.execute_command_with_result(['lspci'])
        self.app_context.output_lsusb = self.helper.execute_command_with_result(['lsusb'])

    def check_iface_module(self, iface: str):
        command = ['ls', '-l', f'/sys/class/net/{iface}/device/driver']
        output = self.helper.execute_command_with_result(command)
        return output.replace('../', '').replace('\n', '').split('/')[-1]

    def check_iface_device(self, iface: str):
        command = ['cat', f'/sys/class/net/{iface}/device/uevent']
        output = self.helper.execute_command_with_result(command)
        iface_id = self.check_iface_usb_device(output)
        if self.helper.string_equals_ignore_case('unknown', iface_id):
            iface_id = self.check_iface_pci_device(output)
        return iface_id

    def check_iface_usb_device(self, output):
        iface_id = self.check_iface_usb_id(output)
        regex_pattern = r'^.*\bID\s+' + str(iface_id) + r'\s+(.*)$'
        has_interface = re.search(regex_pattern, self.app_context.output_lsusb, re.MULTILINE)
        if has_interface:
            name = has_interface.group(1).strip()
        else:
            name = 'Unknown'
        return name

    def check_iface_pci_device(self, output):
        iface_id = self.check_iface_pci_id(output)
        regex_pattern = r'^.*' + str(iface_id) + r'\s+(.*)$'
        has_interface = re.search(regex_pattern, self.app_context.output_lspci, re.MULTILINE)
        if has_interface:
            name = has_interface.group(1).strip()
        else:
            name = 'Unknown'
        return name

    def check_iface_usb_id(self, output):
        has_product = re.search(r'^PRODUCT=(.*)$', output, re.MULTILINE)
        if has_product:
            product = has_product.group(1)
            product = product.split('/')
            product_id = f"{product[0].zfill(4)}:{product[1].zfill(4)}"
        else:
            product_id = 'Unknown'
        return product_id

    def check_iface_pci_id(self, output):
        has_product = re.search(r'^PCI_SLOT_NAME=(.*)$', output, re.MULTILINE)
        if has_product:
            product = has_product.group(1)
            product = product.split(':')
            product_id = f"{product[1]}:{product[2]}"
        else:
            product_id = 'Unknown'
        return product_id
