import anvil.server

@anvil.server.callable
def get_basic_pdf():
  from ..tests import basic_pdf_test

  doc = basic_pdf_test.basic_document()
  return doc.to_blob()


