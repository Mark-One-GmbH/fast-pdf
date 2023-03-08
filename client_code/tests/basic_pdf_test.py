import anvil.media
from ..fast_pdf import Document
from datetime import datetime


def basic_document():
  '''
  Returns a Document Instance that contains basic layouts
  '''

  #get Header logo
  import anvil.media
  company_logo = anvil.URLMedia('https://static.wixstatic.com/media/7a2c3b_422826ce39644fc080d206c80ce59612~mv2.png/v1/fill/w_462,h_455,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Kopie%20von%20M1_standard_black_transparent%20background_low.png')
  
  #0. Define some common variables
  line_h = 5 #standard line height
  
  #1. Define Header and Footer Functions  -> called for each new page
  def footer_func(pdf):
    pdf.cell(80,line_h,'Bestellung Nr 255')
    
  def header_func(pdf):
    pdf.cell(80,line_h,'Bäckerei Breuß',ln=1)  
    pdf.cell(80,line_h,'Alemannenstraße 33',ln=1)
    pdf.cell(80,line_h,'office@markone.at',ln=1)
    pdf.cell(80,line_h,'0676/76 28 996',ln=1)
    pdf.add_image(company_logo,x=165,y=5,h=30,w=34)
  
  #2. Create document Instance and set initial settings
  doc = Document(header_height=20,footer_height=5,header_function=header_func,footer_function=footer_func)
  doc.add_font()
  doc.set_font('poppins',9)
  
  #3. Main Document Body
  for i in range(50):
    doc.add_page()
    #Adress Block
    doc.spacer(20)
    doc.cell(150,line_h,'Herberts Dorfmetz GmbH')
    doc.cell(100,line_h,'LFS 12345',ln=1)
    doc.cell(150,line_h,'am Dorfplatz 7')
    doc.cell(100,line_h,'Kunde Nr.: 1234',ln=1)
    doc.cell(150,line_h,'6830 Rankweil')
    doc.cell(100,line_h,'Tel: 06767628966',ln=1)
    doc.spacer(10)
    
    #Order Details
    doc.cell(150,line_h,'Mi, 08.03.2023',ln=1)
    doc.cell(100,line_h,'Abholung',ln=1)
    doc.cell(100,line_h,'Bitte alles in Kunststoffsäcke einpacken!',ln=1)
    doc.spacer(15)
    
    #Article Table
    doc.cell(20,line_h,'PLU')
    doc.cell(100,line_h,'Artikel')
    doc.cell(25,line_h,'Stk.')
    doc.cell(25,line_h,'Ret')
    doc.cell(100,line_h,'Kommentar',ln=1)

    for i in range(50):
      doc.cell(20,line_h,str(i))
      doc.cell(100,line_h,'Handsemmel')
      doc.cell(25,line_h,'620')
      doc.cell(25,line_h,'0')
      doc.cell(100,line_h,'',ln=1)    
    
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