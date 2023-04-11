import psutil
import scapy.all as scapy

from main.appOptions import AppOptions
from tools.ipTool import IpTool
from tools.iwconfigTool import IwconfigTool
from tools.iwTool import IwTool
from util.helper import Helper
from util.osUtils import OsUtils


class WifiInterface:
    def __init__(self, name: str, options: AppOptions, helper: Helper, utils: OsUtils,
                 ip_tool: IpTool, iw_tool: IwTool, iwconfig_tool: IwconfigTool):
        # Inject
        self.app_options = options
        self.helper = helper
        self.os_utils = utils
        self.ip_tool = ip_tool
        self.iw_tool = iw_tool
        self.iwconfig_tool = iwconfig_tool

        # Get details
        interface_details = psutil.net_if_stats()[name]

        # Properties
        self.Name = name
        self.Flags = interface_details[4]
        self.InModeMonitor = False
        self.MAC = scapy.get_if_hwaddr(name)
        self.MTU = interface_details.mtu
        self.Speed = interface_details.speed

        self.Module = self.os_utils.check_iface_module(name)
        self.Device = self.os_utils.check_iface_device(name)

    def __str__(self):
        return f'{self.Name} (Driver: {self.Module}  MAC: {self.MAC}  Device: {self.Device})'

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
