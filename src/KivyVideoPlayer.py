from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from .KivyCamera import KivyCamera

class KivyVideoPlayer(GridLayout):
  def __init__(self, **kwargs):
    super(KivyVideoPlayer, self).__init__(**kwargs)
    root = App.get_running_app().root
    self.capture = root.capture
    self.my_camera = KivyCamera(capture=self.capture)
    self.add_widget(self.my_camera)

