from kivy.uix.gridlayout import GridLayout

class KivyCameraDetails(GridLayout):
  def __init__(self, **kwargs):
    super(KivyCameraDetails, self).__init__(**kwargs)

  def update_fps(self, fps):
    self.ids.fps.text = str(round(fps))
