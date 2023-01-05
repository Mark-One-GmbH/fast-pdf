from ._anvil_designer import previewTemplate
from anvil import *
import anvil.js

class preview(previewTemplate):
  def __init__(self,url, **properties):
    self.url = url
    self.init_components(**properties)

  
  def form_show(self, **event_args):
    self.call_js('display_pdf', self.url)

