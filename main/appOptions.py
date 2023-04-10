from dataclasses import dataclass


@dataclass
class AppOptions:
    # OPTIONS
    is_verbose = False

    # HW Interface Options
    use_iwconfig = False
