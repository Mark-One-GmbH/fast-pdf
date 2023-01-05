import anvil.media
from .. import fast_pdf


def _basic_pdf():
  doc = fast_pdf.Document()
  doc.add_page()
  doc.set_font('Times',30)
  for i in range(100):
    doc.cell(10,10,'Hello World')
    
  return doc

def run():
  '''returns an anvil blob media pdf'''
  doc = _basic_pdf()
  doc.print()

  server_doc = anvil.server.call('get_basic_pdf')
  print(server_doc)