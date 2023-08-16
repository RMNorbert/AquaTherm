import time


class TapControllerSimulator:
    def __init__(self):
        self.ser_t = None

    def connect(self):
        self.ser_t = True

    def disconnect(self):
        if self.ser_t is not None:
            self.ser_t = None

    def is_connected(self):
        return self.ser_t is not None

    def switch_tap(self, command):
        retries = 5
        while retries > 0:
            try:
                if self.ser_t is None:
                    self.connect()

                self.disconnect()
                return f'Tap: turned {command}'

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()
                raise error

            return None
