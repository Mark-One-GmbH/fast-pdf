import anvil.server


@anvil.server.callable
def get_basic_pdf():
  from .tests.basic_pdf_test import _basic_pdf
  doc = _basic_pdf()
  return doc.to_blob()
