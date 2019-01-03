from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from .PreviousFrameButton import PreviousFrameButton
from .NextFrameButton import NextFrameButton

class VideoFrameSlider(GridLayout):
  def __init__(self, **kwargs):
    super(VideoFrameSlider, self).__init__(**kwargs)
