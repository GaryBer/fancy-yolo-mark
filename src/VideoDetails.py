import cv2
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class VideoDetails(GridLayout):
  def update_all(self, capture):
    self.update_length(int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    self.update_pos(int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
    self.update_width(int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    self.update_height(int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    self.update_fps(capture.get(cv2.CAP_PROP_FPS))

  def update_length(self, length):
    self.ids.length.text = str(length)

  def update_pos(self, pos):
    self.ids.frame_pos.text = str(round(pos))

  def update_width(self, width):
    self.ids.width.text = str(width)

  def update_height(self, height):
    self.ids.height.text = str(height)

  def update_fps(self, fps):
    self.ids.fps.text = str(round(fps))