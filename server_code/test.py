import anvil.server


@anvil.server.callable
def get_basic_pdf():
  from .tests import basic_pdf
  return basic_pdf.create()
