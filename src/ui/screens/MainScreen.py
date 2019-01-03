from kivy.uix.screenmanager import ScreenManager, Screen
from ..player.VideoControlWidget import VideoControlWidget
from ..player.VideoFrameSlider import VideoFrameSlider
from ..player.VideoDetailsWidget import VideoDetailsWidget
from ..player.KivyCameraDetailsWidget import KivyCameraDetailsWidget
from ..player.KivyCameraWidget import KivyCameraWidget

class MainScreen(Screen):
  def __init__(self, **kwargs):
    super(MainScreen, self).__init__(**kwargs)
    
