
def welcome(display):
    """Scroll a welcome phrase across the display on load"""
    display.show_message("...arcade...", background_color=(50, 50, 0))


def game_over(display):
    display.show_message("Game Over", background_color=(50, 0, 0))
