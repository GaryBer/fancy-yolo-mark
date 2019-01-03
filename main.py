from kivy.app import App
from src.ui.RootWidget import RootWidget

class FancyYoloMark(App):
  title = 'FancyYoloMark'
  kv_directory = './templates'

  def build(self):
    self.icon = './assets/icons/app.png'
    root = RootWidget()
    return root

  # def on_stop(self):
    # self.capture.release()

if __name__ == '__main__':
  FancyYoloMark().run()
