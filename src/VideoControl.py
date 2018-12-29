from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class VideoControl(GridLayout):
  def __init__(self, **kwargs):
    super(VideoControl, self).__init__(**kwargs)

  def play(self):
    root = App.get_running_app().root
    root.ids.my_camera.play()

  def pause(self):
    root = App.get_running_app().root
    root.ids.my_camera.pause()

  def step_forward(self):
    root = App.get_running_app().root
    root.ids.my_camera.step_forward()

  def step_backward(self):
    root = App.get_running_app().root
    root.ids.my_camera.step_backward()
