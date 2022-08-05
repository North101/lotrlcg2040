import badger2040
from badger_ui import App, Offset, Size, Widget
from badger_ui.center import Center
from badger_ui.text import TextWidget
from lotrlcg2040.data import eye_icon


class TrackerScreen(Widget):
  def __init__(self):
    self.threat = 20

  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    if pressed[badger2040.BUTTON_UP]:
      self.threat = min(self.threat + 1, 50)
      return True

    elif pressed[badger2040.BUTTON_DOWN]:
      self.threat = max(self.threat - 1, 0)
      return True

    return super().on_button(app, pressed)

  def render(self, app: App, size: Size, offset: Offset):
    eye_icon.draw(app.display, Offset(((size.width - eye_icon.width) // 2) + 2, 0))

    Center(child=TextWidget(
        text=f'{self.threat}',
        line_height=60,
        scale=2,
        thickness=3,
    )).render(app, size, Offset(0, 24))
