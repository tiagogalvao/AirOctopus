from dataclasses import dataclass

import colorama


@dataclass
class AppSettings:
    # BASIC INFO
    app_name = 'AirOctopus'
    app_version = '0.1.1'

    # FONT STYLING
    fs_black = colorama.Fore.LIGHTBLACK_EX
    fs_red = colorama.Fore.RED
    fs_green = colorama.Fore.LIGHTGREEN_EX
    fs_yellow = colorama.Fore.LIGHTYELLOW_EX
    fs_blue = colorama.Fore.LIGHTBLUE_EX
    fs_magenta = colorama.Fore.LIGHTMAGENTA_EX
    fs_cyan = colorama.Fore.LIGHTCYAN_EX
    fs_white = colorama.Fore.LIGHTWHITE_EX
    fs_reset = colorama.Fore.RESET
    fs_bold = colorama.Style.BRIGHT
    fs_normal = colorama.Style.NORMAL
    fs_reset_all = colorama.Style.RESET_ALL

    font_switches = {'&30': fs_black, '&31': fs_red, '&32': fs_green,
                     '&33': fs_yellow, '&34': fs_blue, '&35': fs_magenta,
                     '&36': fs_cyan, '&37': fs_white, '&40': fs_reset_all,
                     '&01': fs_bold, '&02': fs_normal, '&10': fs_reset}

    def __init__(self):
        colorama.init()
