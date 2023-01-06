import anvil.media
from ..fast_pdf import Document


def create_basic_doc():
  '''
  Returns a Document that contains basic layouts
  '''
  doc = Document()
  doc.set_font('Times',30)
  for i in range(100):
    doc.cell(10,10,'Hello World',ln=1)
    
  return doc


##################
#Run Client and Server Tests with basic pdf doc
#################
def run_test():
  '''returns an anvil blob media pdf'''
  doc = create_basic_doc()
  client_blob = doc.to_blob()
  server_blob = anvil.server.call('get_basic_pdf')
  #return media objs
  return client_blob,server_blob