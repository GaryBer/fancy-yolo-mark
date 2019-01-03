from kivy.uix.button import Button
from kivy.app import App
from ..mixins.ToolTipBehavior import ToolTipBehavior

class SaveFrameLabelsButton(ToolTipBehavior, Button):
  def __init__(self, **kwargs):
    kwargs['tooltip_text'] = 'Save Frame Labels'
    super(SaveFrameLabelsButton, self).__init__(**kwargs)
