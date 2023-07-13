class window:
  def __init__(self, screen='main', all_screen=['main']):
    
    self.screen = screen
    self.all_screen = all_screen
  def move(self, to='main'):
    if to in self.all_screen:
      self.screen = to
    else:
      print('Screen Error 1')
  def add_screen(self, screen_name)
