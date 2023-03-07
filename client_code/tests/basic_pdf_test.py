import anvil.media
from ..fast_pdf import Document
from datetime import datetime


def basic_document():
  '''
  Returns a Document Instance that contains basic layouts
  '''
  
  #1. Define Header and Footer Functions  -> called for each new page
  def footer_func(pdf):
    pdf.cell(10,10,'My Footer !')
    
  def header_func(pdf):
    pdf.cell(10,10,'My Header!')

  #2. Create document Instance and set initial settings
  doc = Document()
  doc.set_footer_function(footer_func)
  doc.set_header_function(header_func)
  doc.set_font('Times',30)
  
  #3. Main Document Body
  doc.add_page()
  for i in range(100):
    doc.cell(10,10,'Hello World',ln=1)
    
    
  return doc


##################
#Run Client and Server Tests with basic pdf doc
#################
def run_test():
  '''returns an anvil blob media pdf'''
  client_start = datetime.now()
  doc = basic_document()
  client_blob = doc.to_blob()
  print('client done',datetime.now()-client_start)

  server_start = datetime.now()
  server_blob = anvil.server.call('get_basic_pdf')
  print('server took ',datetime.now()-server_start)
  #return media objs
  return client_blob,server_blob