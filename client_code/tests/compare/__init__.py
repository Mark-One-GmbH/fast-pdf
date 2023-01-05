from ._anvil_designer import compareTemplate
from anvil import *
from .. import basic_pdf_test

class compare(compareTemplate):
  def __init__(self,pdf1,pdf2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    p1,p2 = basic_pdf_test.run_test()
    self.client_preview = p1
    self.server_preview = p2


    