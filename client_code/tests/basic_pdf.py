

def create():
  '''returns an anvil blob media pdf'''
  from .. import fast_pdf
  doc = fast_pdf.Document()
  doc.add_page()
  doc.set_font('Times',30)
  for i in range(100):
    doc.cell(10,10,'Hello World')
  return doc.to_blob()