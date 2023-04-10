from main.appOptions import AppOptions
from tools.ipTool import IpTool
from tools.iwconfigTool import IwconfigTool
from tools.iwTool import IwTool
from util.helper import Helper


class WifiInterface:
    def __init__(self, options: AppOptions, helper: Helper,
                 ip_tool: IpTool, iw_tool: IwTool, iwconfig_tool: IwconfigTool):
        self.app_options = options
        self.helper = helper
        self.ip_tool = ip_tool
        self.iw_tool = iw_tool
        self.iwconfig_tool = iwconfig_tool

        # Properties
        self.Chipset = ''
        self.Driver = ''
        self.InModeMonitor = False
        self.MAC = ''
        self.Name = ''

    def disable_mode_monitor(self):
        self.ip_tool.set_iface_down(self.Name)
        if self.app_options.use_iwconfig:
            self.iwconfig_tool.disable_mode_monitor(self.Name)
        else:
            self.iw_tool.disable_mode_monitor(self.Name)
        self.ip_tool.set_iface_up(self.Name)

    def enable_mode_monitor(self):
        self.ip_tool.set_iface_down(self.Name)
        if self.app_options.use_iwconfig:
            self.iwconfig_tool.enable_mode_monitor(self.Name)
        else:
            self.iw_tool.enable_mode_monitor(self.Name)
        self.ip_tool.set_iface_up(self.Name)
