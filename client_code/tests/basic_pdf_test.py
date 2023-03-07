import anvil.media
from ..fast_pdf import Document
from datetime import datetime


def basic_document():
  '''
  Returns a Document Instance that contains basic layouts
  '''

  #0. Define some common variables
  line_h = 6 #standard line height
  
  #1. Define Header and Footer Functions  -> called for each new page
  def footer_func(pdf):
    pdf.cell(80,line_h,'Bestellung Nr 255')
    
  def header_func(pdf):
    pdf.cell(80,line_h,'Bäckerei Breuß',ln=1)
    pdf.cell(80,line_h,'Alemannenstraße 33',ln=1)
    pdf.cell(80,line_h,'office@markone.at',ln=1)
    pdf.cell(80,line_h,'0676/76 28 996',ln=1)

  #2. Create document Instance and set initial settings
  doc = Document()
  doc.set_footer_function(footer_func)
  doc.set_header_function(header_func)
  doc.set_font('Times',9)
  
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