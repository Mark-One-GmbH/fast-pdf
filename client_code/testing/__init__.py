from ._anvil_designer import testingTemplate
from anvil import *
from datetime import datetime
from .. import tests

class testing(testingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    tests.run()

  def button_1_click(self, **event_args):
    tests.run()



    


