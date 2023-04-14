from util.helper import Helper


class IpTool:
    def __init__(self, helper: Helper):
        self.helper = helper

    def set_iface_up(self, iface):
        command = ['sudo', 'ip', 'link', 'set', iface, 'up']
        self.helper.execute_command(command)

    def set_iface_down(self, iface):
        command = ['sudo', 'ip', 'link', 'set', iface, 'down']
        self.helper.execute_command(command)

    def get_mac_address(self, iface):
        command = ['ip', 'link', 'show', iface]
        return self.helper.execute_command_with_result(command)
