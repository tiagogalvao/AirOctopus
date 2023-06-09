from internals.appContext import AppContext
from util.helper import Helper


class NetworksTable:
    def __init__(self, context: AppContext, helper: Helper):
        self.app_context = context
        self.helper = helper
        self.internal_timer = 0

    def print(self):
        self.helper.move_cursor(0)
        table_len = len(self.app_context.network_list)+2
        if len(self.app_context.network_list) > 0:
            self.print_header()
            for index, item in enumerate(self.app_context.network_list):
                self.helper.print_text(f'[{str(index).zfill(len(str(table_len)))}]\t{item}')
        else:
            self.internal_timer += 1
            self.helper.print_text(f'[{self.internal_timer}] No networks have been found... yet')

    def print_header(self):
        self.helper.print_text('----- HEADER -----')
