import anvil.server

@anvil.server.callable
def get_basic_pdf():
  test_import()
  from ..tests import basic_pdf_test

  doc = basic_pdf_test.basic_document()
  return doc.to_blob()

def test_import():
  from ..fast_pdf import Document
  #simple test to constrct a pdf server side
  doc = Document()
  doc.add_page()
  doc.set_font('Arial',12)
  doc.cell(100,200,'Hello world')
  pdf_blob = doc.to_blob()

  
