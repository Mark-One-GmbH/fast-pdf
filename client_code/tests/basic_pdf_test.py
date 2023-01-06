import anvil.media
from ..fast_pdf import Document


def _basic_pdf():
  doc = Document()
  doc.add_page()
  doc.set_font('Times',30)
  for i in range(100):
    doc.cell(10,10,'Hello World')
    
  return doc

def run_test():
  '''returns an anvil blob media pdf'''
  doc = _basic_pdf()
  #doc.download()
  #doc.print()
  #doc.preview()

  server_blob = anvil.server.call('get_basic_pdf')
  return doc.to_blob(),server_blob