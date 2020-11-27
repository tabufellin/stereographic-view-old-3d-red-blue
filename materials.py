from color_module import color

class Material(object):
  def __init__(self, diffuse=color(0,0,0), albedo=(1, 0), spec=0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec



ivory = Material(diffuse=color(100, 100, 80), albedo=(0.5,  0.4), spec=30)
rubber = Material(diffuse=color(180, 0, 0), albedo=(0.6,  0.3), spec=10)
white_skin = Material(diffuse=color(255, 255, 255), albedo=(0.5,  0.4), spec=30)
brown_skin = Material(diffuse=color(255, 170, 60), albedo=(0.2,  0.3), spec=10)
eye = Material(diffuse=color(50, 50, 50), albedo=(0.2,  0.3), spec=10)
brown_skin_detail = Material(diffuse=color(255, 204, 153), albedo=(0.2,  0.3), spec=10)
