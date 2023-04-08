from dataclasses import dataclass


@dataclass
class AppData:
    required_param_1: str
    required_param_2: int
    optional_param_1: float = None
    optional_param_2: bool = None
