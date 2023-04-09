from dataclasses import dataclass


@dataclass
class AppData:
    appName = 'AirOctopus'
    appVersion = '0.0.1'
    isVerbose = False

    # required_param_1: str
    # required_param_2: int
    optional_param_1: float = None
    optional_param_2: bool = None
