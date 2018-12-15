from kivy.uix.slider import Slider
from kivy.app import App

class VideoFrameSlider(Slider):
  def __init__(self, **kwargs):
    super(VideoFrameSlider, self).__init__(**kwargs)
    self.was_paused = False
    self.released = False

  def pause(self):
    self.released = False
    root = App.get_running_app().root
    if root.my_camera.paused:
      self.was_paused = True
    root.ids.video_control.pause()

  def moving(self):
    self.released = False

  def set_frame_pos(self):
    root = App.get_running_app().root
    if root.my_camera.paused:
      root.my_camera.set_frame_pos(self.value)

  def update_frame_pos(self):
    if self.released:
      return
    root = App.get_running_app().root
    if root.my_camera.paused:
      root.my_camera.update_frame_pos(self.value)
      if self.was_paused:
        self.was_paused = False
        self.released = True
      else:
        root.ids.video_control.play()
        self.released = True
