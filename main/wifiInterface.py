from main.appOptions import AppOptions
from tools.ipTool import IpTool
from tools.iwconfigTool import IwconfigTool
from tools.iwTool import IwTool
from util.helper import Helper


class WifiInterface:
    def __init__(self, options: AppOptions, helper: Helper,
                 ip_tool: IpTool, iw_tool: IwTool, iwconfig_tool: IwconfigTool):
        self.appData = options
        self.helper = helper
        self.ipTool = ip_tool
        self.iwTool = iw_tool
        self.iwconfigTool = iwconfig_tool

        # Properties
        self.Chipset = ''
        self.Driver = ''
        self.InModeMonitor = False
        self.MAC = ''
        self.Name = ''

    def disable_mode_monitor(self):
        self.ipTool.set_iface_down(self.Name)
        if self.appData.useIwconfig:
            self.iwconfigTool.disable_mode_monitor(self.Name)
        else:
            self.iwTool.disable_mode_monitor(self.Name)
        self.ipTool.set_iface_up(self.Name)

    def enable_mode_monitor(self):
        self.ipTool.set_iface_down(self.Name)
        if self.appData.useIwconfig:
            self.iwconfigTool.enable_mode_monitor(self.Name)
        else:
            self.iwTool.enable_mode_monitor(self.Name)
        self.ipTool.set_iface_up(self.Name)
