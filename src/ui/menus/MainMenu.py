from kivy.uix.actionbar import ActionBar
from kivy.properties import ObjectProperty
from ..dialogs.AboutDialog import AboutDialog

class MainMenu(ActionBar):
  def __init__(self, **kwargs):
    super(MainMenu, self).__init__(**kwargs)
