import time
import cv2
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.app import App

class KivyCamera(Image):
  def __init__(self, capture, clock_fps = 60, **kwargs):
    super(KivyCamera, self).__init__(**kwargs)
    self.clock_fps = clock_fps
    self.start_time = time.time()
    self.update_counter = 0
    self.capture = capture
    self.paused = False
    Clock.schedule_interval(self.update, 1.0 / clock_fps)

  def update(self, dt):
    if self.paused:
      return
    self.render(dt)

  def set_frame_pos(self, frame_pos):
    root = App.get_running_app().root
    root.capture.set(cv2.CAP_PROP_POS_FRAMES, round(frame_pos))
    root.ids.video_details.update_pos(frame_pos)

  def update_frame_pos(self, frame_pos):
    self.set_frame_pos(frame_pos)
    Clock.schedule_once(self.render)

  def render(self, dt):
    root = App.get_running_app().root
    video_frame_pos = int(root.capture.get(cv2.CAP_PROP_POS_FRAMES))
    root.ids.video_details.update_pos(video_frame_pos)
    root.ids.video_frame_slider.value = video_frame_pos
    #
    ret, frame = self.capture.read()
    if ret:
      # convert it to texture
      buf1 = cv2.flip(frame, 0)
      buf = buf1.tostring()
      image_texture = Texture.create(
        size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
      image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
      # display image from the texture
      self.texture = image_texture
      self.calculate_fps()

  def calculate_fps(self):
    self.update_counter += 1
    if (time.time() - self.start_time) > 1:
      fps = self.update_counter / (time.time() - self.start_time)
      self.update_counter = 0
      self.start_time = time.time()
      self.update_camera_details_fps(fps)

  def update_camera_details_fps(self, fps):
    root = App.get_running_app().root
    root.ids.kivy_camera_details.update_fps(fps)

  def play(self):
    self.paused = False

  def pause(self):
    self.paused = True

  def step_forward(self):
    root = App.get_running_app().root
    frame_pos = int(root.capture.get(cv2.CAP_PROP_POS_FRAMES))
    self.set_frame_pos(frame_pos)
    self.update_frame_pos(frame_pos)

  def step_backward(self):
    root = App.get_running_app().root
    frame_pos = int(root.capture.get(cv2.CAP_PROP_POS_FRAMES)) - 2
    self.set_frame_pos(frame_pos)
    self.update_frame_pos(frame_pos)
