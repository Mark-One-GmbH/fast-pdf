import anvil.server

@anvil.server.callable
def get_basic_pdf():
  from ..tests import basic_pdf_test

  doc = basic_pdf_test.create_basic_doc()
  return doc.to_blob()


