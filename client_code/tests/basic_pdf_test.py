import anvil.media
from ..fast_pdf import Document


def basic_document():
  '''
  Returns a Document that contains basic layouts
  '''
  class myDocument()

  #Define Footer
  def footer_func(**kw_args):
    print('hello from footer',kw_args)
    self.cell(10,10,'My Header!')
    pass
    
  doc.set_footer_function(footer_func)

  #Define Header
  def header_func(self):
    self.cell(10,10,'My Header!')
    pass
    
  #doc.set_header_function(header_func)

  #Main Document Body
  doc.set_font('Times',30)
  for i in range(100):
    doc.cell(10,10,'Hello World',ln=1)
    
    
  return doc


##################
#Run Client and Server Tests with basic pdf doc
#################
def run_test():
  '''returns an anvil blob media pdf'''
  doc = basic_document()
  client_blob = doc.to_blob()
  server_blob = anvil.server.call('get_basic_pdf')
  #return media objs
  return client_blob,server_blob