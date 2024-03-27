from scapy.all import *
import random

from scapy.layers.dot11 import Dot11Beacon, Dot11Elt

from src.internals.appContext import AppContext
from src.model.network import Network
from src.model.wifiInterface import WifiInterface
from src.tools.iwlistTool import IwlistTool
from src.util.helper import Helper


class WiFiScanner:
    def __init__(self, context: AppContext, helper: Helper, iwlist_tool: IwlistTool,
                 interface: WifiInterface, timeout=5.0):
        self.app_context = context
        self.helper = helper
        self.interface = interface
        self.iwlist_tool = iwlist_tool
        self.timeout = timeout
        self.results = []

    def start_scan(self):
        self._scan_channel()

    def _scan_channel(self):
        l_channel = random.choice(self.interface.Channels)
        self.interface.change_channel(l_channel)
        sniff(iface=self.interface.Name, prn=self._packet_handler, timeout=self.timeout,
              lfilter=lambda x: x.haslayer(Dot11Beacon) and x.getlayer(Dot11Beacon).info != b'')

    def _packet_handler(self, pkt):
        if pkt.haslayer(Dot11Beacon):
            network = Network(self.helper)
            network.Name = pkt.getlayer(Dot11Elt).info.decode()
            network.MAC = pkt.addr2.upper()
            network.Power = pkt.notdecoded[-4:-3]
            network.Channel = pkt.notdecoded[28:29]
            exist = False
            for item in self.app_context.network_list:
                if item.Name == network.Name:
                    exist = True
                    item.Power = network.Power
                    item.Channel = network.Channel
            if not exist:
                self.app_context.network_list.append(network)

    def get_results(self):
        return self.results

    def clear_results(self):
        self.results = []
