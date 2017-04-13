from sense_hat import SenseHat, ACTION_RELEASED

class SenseHatInput:

    def __init__(self):
        self.sense_hat = SenseHat()

    def get_events(self):
        return [event.direction for event in self.sense_hat.stick.get_events()
                                if event.action != ACTION_RELEASED]
