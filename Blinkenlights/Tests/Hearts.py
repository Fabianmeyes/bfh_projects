import config
import copy

class Hearts:
    colors = [
        (  0, 0, 0), #off
        (111, 0, 0), #light red
        (255, 0, 0)  #red
    ]

    field = [x[:] for x in [[0]*config.LED_COLS]*config.LED_ROWS] 

    def __init__(self, ipcon):
        print(self.playfield)
        self.okay = False
        self.ipcon = ipcon

        if not config.UID_LED_STRIP_BRICKLET:
            print("Not Configured: LED Strip (required)")
            return

        self.led_strip = LEDStrip(config.UID_LED_STRIP_BRICKLET, self.ipcon)

        try:
            self.led_strip.get_frame_duration()
            print("Found: LED Strip ({0})".format(config.UID_LED_STRIP_BRICKLET))
        except:
            print("Not Found: LED Strip ({0})".format(config.UID_LED_STRIP_BRICKLET))
            return

        self.kp = KeyPress(self.ipcon)
        self.speaker = PongSpeaker(self.ipcon)

        self.okay = True

        self.led_strip.set_frame_duration(25)
        self.led_strip.register_callback(self.led_strip.CALLBACK_FRAME_RENDERED,
                                         self.frame_rendered)

        self.init_game()

    def frame_rendered(self, length):
        self.write_playfield() 

    def write_playfield(self):
        if not self.okay:
            return

        field = copy.deepcopy(self.playfield)

        r = []
        g = []
        b = []
        for row in range(config.LED_ROWS):
            col_range = range(config.LED_COLS)
            if row % 2 == 0:
                col_range = reversed(col_range)
            for col in col_range:
                r.append(self.COLORS[field[row][col]][config.R_INDEX])
                g.append(self.COLORS[field[row][col]][config.G_INDEX])
                b.append(self.COLORS[field[row][col]][config.B_INDEX])

        r_chunk = [r[i:i+16] for i in range(0, len(r), 16)]
        g_chunk = [g[i:i+16] for i in range(0, len(g), 16)]
        b_chunk = [b[i:i+16] for i in range(0, len(b), 16)]

        for i in range(len(r_chunk)):
            length = len(r_chunk[i])

            r_chunk[i].extend([0]*(16-len(r_chunk[i])))
            g_chunk[i].extend([0]*(16-len(g_chunk[i])))
            b_chunk[i].extend([0]*(16-len(b_chunk[i])))

            try:
                self.led_strip.set_rgb_values(i*16, length, r_chunk[i], g_chunk[i], b_chunk[i])
            except:
                break


