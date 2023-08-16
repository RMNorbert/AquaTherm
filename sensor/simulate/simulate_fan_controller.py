import time


class FanControllerSimulator:
    def __init__(self):
        self.ser_f = None

    def connect(self):
        self.ser_f = True

    def disconnect(self):
        if self.ser_f is not None:
            self.ser_f = None

    def is_connected(self):
        return self.ser_f is not None

    def switch_fan(self, command):
        retries = 3
        while retries > 0:
            try:
                if self.ser_f is None:
                    self.connect()

                if command == "off":
                    self.disconnect()

                return f'Fan: turned {command}'

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                retries -= 1

            except Exception as error:
                self.disconnect()
                raise error

            return None
