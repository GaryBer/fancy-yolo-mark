# https://gist.github.com/johanneshk/0d3d6924aa44ff1a00e86495243ee88c

from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""
<ToolTipLabel@Label>:
    size_hint: None, None
    size: self.texture_size
    text: ""
    padding: [3, 1]
    canvas.before:
        Color: 
            rgb: 0,0,0,1                                                                                                            
        Rectangle:
            size: self.size
            pos: self.pos
""")

class ToolTipBehavior(object):
  def __init__(self, **kwargs):
    tooltip_text = kwargs.get('tooltip_text')
    # if not tooltip_text:
    #   return

    self.tooltip = Factory.ToolTipLabel(text=tooltip_text)
    super(ToolTipBehavior, self).__init__()
    Window.bind(mouse_pos=self.on_mouse_pos)
    self.open = False

  def on_mouse_pos(self, *args):
    if not self.get_root_window():
      return

    pos = args[1]
    inside = self.collide_point(*self.to_widget(*pos))
    if inside and not self.open:
      self.tooltip.pos = pos
      self.display_tooltip()
      self.open = True
    elif not inside and self.open:
      #Clock.schedule_once(self.close_tooltip, .1)
      self.close_tooltip()
    elif inside and self.open:
      self.tooltip.pos = pos

  def close_tooltip(self, *args):
    self.open = False
    Window.remove_widget(self.tooltip)

  def display_tooltip(self, *args):
    Window.add_widget(self.tooltip)
