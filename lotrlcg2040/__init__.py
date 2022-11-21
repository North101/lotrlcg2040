from lotrlcg2040.data import eye_icon
from lotrlcg2040.widgets.app import MyApp

root_dir = '/'.join(__file__.rsplit('/')[:-1])

def start():
  eye_icon.load()

  app = MyApp()
  while True:
    app.update()
