from dataclasses import dataclass


@dataclass
class AppContext:
    iface_selected_wifi_interfaces = []
    iface_system_wifi_interfaces = []
