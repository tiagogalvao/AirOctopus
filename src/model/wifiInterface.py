import psutil
import re

from internals.appOptions import AppOptions
from tools.ipTool import IpTool
from tools.iwconfigTool import IwconfigTool
from tools.iwTool import IwTool
from tools.iwlistTool import IwlistTool
from util.helper import Helper
from util.osUtils import OsUtils


class WifiInterface:
    def __init__(self, name: str, options: AppOptions, helper: Helper, utils: OsUtils,
                 ip_tool: IpTool, iw_tool: IwTool, iwconfig_tool: IwconfigTool, iwlist_tool: IwlistTool):
        # Inject
        self.app_options = options
        self.helper = helper
        self.os_utils = utils
        self.ip_tool = ip_tool
        self.iw_tool = iw_tool
        self.iwconfig_tool = iwconfig_tool
        self.iwlist_tool = iwlist_tool

        # Get details
        interface_details = psutil.net_if_stats()[name]

        # Properties
        self.Name = name
        self.MAC = None
        self.get_mac_address()
        self.Flags = interface_details[4]
        self.InModeMonitor = False
        self.MTU = interface_details.mtu
        self.Speed = interface_details.speed
        self.Module = self.os_utils.check_iface_module(name)
        self.Device = self.os_utils.check_iface_device(name)
        self.DeviceOriginalName = self.Device
        self.clean_device_name()
        self.Channels = self.iwlist_tool.check_channels(self.Name)

    def __str__(self):
        return f'{self.Name} (Driver: {self.Module}  MAC: ...{self.MAC[9:len(self.MAC)]}  Device: {self.Device})'

    def disable_mode_monitor(self):
        self.ip_tool.set_iface_down(self.Name)
        if self.app_options.use_iwconfig:
            self.iwconfig_tool.disable_mode_monitor(self.Name)
        else:
            self.iw_tool.disable_mode_monitor(self.Name)
        self.ip_tool.set_iface_up(self.Name)
        self.InModeMonitor = False

    def enable_mode_monitor(self):
        self.ip_tool.set_iface_down(self.Name)
        if self.app_options.use_iwconfig:
            self.iwconfig_tool.enable_mode_monitor(self.Name)
        else:
            self.iw_tool.enable_mode_monitor(self.Name)
        self.ip_tool.set_iface_up(self.Name)
        self.InModeMonitor = True

    def change_channel(self, channel: int):
        if self.app_options.use_iwconfig:
            self.iwconfig_tool.change_channel(self.Name, channel)
        else:
            self.iw_tool.change_channel(self.Name, channel)

    def clean_device_name(self):
        # TODO: This is ugly... please... make it better
        trash_words = ['wireless', 'adapter', 'network', 'controller']
        trash_normal = ['802.11', 'a/', '/ac', 'b/', 'g/', 'n/', ' n', 'network', 'controller', ':']
        for item in trash_normal:
            self.Device = self.Device.replace(item, '')
        for item in trash_words:
            pattern = re.compile(r'\b(' + str(item) + r')\b', flags=re.IGNORECASE)
            self.Device = pattern.sub('', self.Device)
        self.Device = self.Device.strip()

    def get_mac_address(self):
        output = self.ip_tool.get_mac_address(self.Name)
        mac_address_regex = r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"
        match = re.search(mac_address_regex, output)
        if match:
            self.MAC = match.group(0)
        else:
            self.MAC = '00:00:00:00:00:00'
