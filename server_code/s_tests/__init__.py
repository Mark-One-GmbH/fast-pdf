import anvil.server

@anvil.server.callable
def get_basic_pdf():
  test_import()
  from ..tests import basic_pdf_test
 #get Header logo
  import anvil.media
  company_logo = anvil.URLMedia('https://static.wixstatic.com/media/7a2c3b_422826ce39644fc080d206c80ce59612~mv2.png/v1/fill/w_462,h_455,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Kopie%20von%20M1_standard_black_transparent%20background_low.png')
  
  doc = basic_pdf_test.basic_document(company_logo)
  return doc.to_blob()

def test_import():
  from ..fast_pdf import Document
  #simple test to constrct a pdf server side
  doc = Document()
  doc.add_page()
  doc.set_font('Arial',12)
  doc.cell(100,200,'Hello world')
  pdf_blob = doc.to_blob()

  
