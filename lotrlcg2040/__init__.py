from lotrlcg2040.data import eye_icon
from lotrlcg2040.widgets.app import MyApp

root_dir = '/'.join(__file__.rsplit('/')[:-1])
assets_dir = f'{root_dir}/assets'

def start():
  eye_icon.load()

  app = MyApp()
  while True:
    app.update()
