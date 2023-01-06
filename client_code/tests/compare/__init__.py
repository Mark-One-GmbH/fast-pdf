from ._anvil_designer import compareTemplate
from anvil import *
from .. import basic_pdf_test

class compare(compareTemplate):
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.client_pdf = None
    self.server_pdf = None


  def run_test(self):
    self.client_pdf,self.server_pdf = basic_pdf_test.run_test()
    self.server_preview.pdf_media = self.client_pdf
    self.client_preview.pdf_media = self.server_pdf


    