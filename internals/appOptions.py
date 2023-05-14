from dataclasses import dataclass


@dataclass
class AppOptions:
    # OPTIONS
    is_verbose = False

    # HW Interface Options
    iface_keep_monitor = False
    use_iwconfig = False
