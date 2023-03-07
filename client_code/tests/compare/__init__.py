from ._anvil_designer import compareTemplate
from anvil import *
from .. import basic_pdf_test
from ...fast_pdf import utils

class compare(compareTemplate):
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_pdf = 'basic'
    self.client_pdf = None
    self.server_pdf = None
    self.pdf_dd.items = [('Basic PFD','basic')]
    self.pdf_dd.selected_value = 'basic'

    self.run_test()

  def pdf_dd_change(self, **event_args):
    self.selected_pdf = self.pdf_dd.selected_value
    self.run_test()
    
  def run_test(self):
    self.client_pdf,self.server_pdf = basic_pdf_test.run_test()
    self.server_preview.pdf_media = self.server_pdf
    self.client_preview.pdf_media = self.client_pdf

  def server_print_btn_click(self, **event_args):
    utils.print_pdf(self.server_pdf)

  def server_download_btn_click(self, **event_args):
    utils.download_pdf(self.server_pdf)

  def client_print_btn_click(self, **event_args):
    utils.print_pdf(self.client_pdf)

  def client_download_btn_click(self, **event_args):
    utils.download_pdf(self.client_pdf)

  def server_preview_btn_click(self, **event_args):
    comp = utils.pdf_to_component(self.server_pdf)
    alert(comp,large=True)

  def client_preview_btn_click(self, **event_args):
    comp = utils.pdf_to_component(self.client_pdf)
    alert(comp,large=True)













    