from gnuradio import gr, blocks

class gnu_dev_hackrf_binding(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="gnu_dev_hackrf_binding",
            in_sig=[],
            out_sig=None
        )
        self.data = []

    def work(self, input_items, output_items):
        # input_items enthält die empfangenen Nachrichten
        # Speichere die empfangenen Daten in der Variable
        self.data.extend(input_items[0])
        return len(input_items[0])

# Erstelle eine Instanz des Python-Blocks
gnu_dev_hackrf_binding = gnu_dev_hackrf_binding()

# Hier wird der Message Debug Block erstellt
msg_debug = blocks.message_debug()

# Verbinde den Message Debug Block mit dem Python-Block
msg_debug.msg_connect((gnu_dev_hackrf_binding, 'store'))

# Füge save_to_variable zu deinem Flowgraph hinzu