from tools.ipTool import IpTool
from tools.iwlistTool import IwlistTool
from tools.iwTool import IwTool
from tools.iwconfigTool import IwconfigTool


class DependencyCheck:
    def __init__(self, ip_tool: IpTool, iwconfig_tool: IwconfigTool, iwlist_tool: IwlistTool, iw_tool: IwTool):
        self.ip_tool = ip_tool
        self.iwconfig_tool = iwconfig_tool
        self.iwlist_tool = iwlist_tool
        self.iw_tool = iw_tool

    def check_all(self):
        self.ip_tool.check_existence()
        self.iwconfig_tool.check_existence()
        self.iwlist_tool.check_existence()
        self.iw_tool.check_existence()
