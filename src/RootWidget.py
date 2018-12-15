from kivy.uix.gridlayout import GridLayout
import cv2
from .VideoDetails import VideoDetails
from .KivyCameraDetails import KivyCameraDetails
from .KivyCamera import KivyCamera
from .VideoControl import VideoControl
from .VideoFrameSlider import VideoFrameSlider

class RootWidget(GridLayout):
  def __init__(self, **kwargs):
    super(RootWidget, self).__init__(**kwargs)
    self.capture = cv2.VideoCapture('input/1.mp4')
    #
    self.ids.video_frame_slider.max = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
    #
    self.my_camera = KivyCamera(capture=self.capture)
    self.add_widget(self.my_camera)
