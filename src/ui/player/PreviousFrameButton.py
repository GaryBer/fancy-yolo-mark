from kivy.uix.button import Button
from kivy.app import App
from ..mixins.ToolTipBehavior import ToolTipBehavior

class PreviousFrameButton(ToolTipBehavior, Button):
  def __init__(self, **kwargs):
    kwargs['tooltip_text'] = 'Previous Frame'
    super(PreviousFrameButton, self).__init__(**kwargs)
