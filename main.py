from kivy.app import App
from src.RootWidget import RootWidget

class FancyYoloMark(App):
  title = 'FancyYoloMark'
  kv_directory = './template'

  def build(self):
    self.icon = './assets/app.png'
    root = RootWidget()
    return root

  # def on_stop(self):
    #without this, app will not exit even if the window is closed
    # self.capture.release()

if __name__ == '__main__':
  FancyYoloMark().run()
