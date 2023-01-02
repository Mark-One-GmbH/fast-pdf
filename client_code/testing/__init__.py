from ._anvil_designer import testingTemplate
from anvil import *
from datetime import datetime
from .. import PDF

class testing(testingTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    

  def test_btn_click(self, **event_args):
    start = datetime.now()
    doc = PDF.Document()
    for i in range(100):
      doc.text('hello',10,i*10)
    doc.download()
    print('took',datetime.now()-start)
    


