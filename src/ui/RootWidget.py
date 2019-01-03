from kivy.uix.boxlayout import BoxLayout
from .menus.MainMenu import MainMenu
from .ScreenManagement import ScreenManagement

class RootWidget(BoxLayout):
  def __init__(self, **kwargs):
    super(RootWidget, self).__init__(**kwargs)
    
