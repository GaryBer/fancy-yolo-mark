from kivy.uix.button import Button
from kivy.app import App
from ..mixins.ToolTipBehavior import ToolTipBehavior

class NextFrameButton(ToolTipBehavior, Button):
  def __init__(self, **kwargs):
    kwargs['tooltip_text'] = 'Next Frame'
    super(NextFrameButton, self).__init__(**kwargs)
