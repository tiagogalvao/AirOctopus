from dataclasses import dataclass


@dataclass
class AppContext:
    iface_selected_wifi_interfaces = []
    iface_system_wifi_interfaces = []

    network_list = []

    output_lsusb = None
    output_lspci = None
