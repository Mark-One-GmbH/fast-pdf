from ._anvil_designer import previewTemplate
from anvil import *
import anvil.js

class preview(previewTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.call_js('display_pdf', self.url)