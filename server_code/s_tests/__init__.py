import anvil.server

@anvil.server.callable
def get_basic_pdf():
  from ..tests import basic_pdf_test

  doc = basic_pdf_test._basic_pdf()
  return doc.to_blob()


