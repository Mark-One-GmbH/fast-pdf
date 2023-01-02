"""
Main Document Class that acts as a wrapper for client and server side PDF Creation
Browser Library: JSPDF
Server Library: FPDF2
"""
import anvil.js
import anvil.server

class Document:
  def __init__(self,implementation='auto'):
    from anvil.js.window import jspdf
    if implementation not in ['server','client']:
      #auto detection
      self.server_side = anvil.is_server_side()
    elif implementation == 'server':
      self.server_side = True
    else:
      self.server_side = False

    self.proxy_pdf = jspdf.jsPDF('p', 'mm')

    


  def text(self,text,height,width):
    self.proxy_pdf.text(text,height,width)

  def to_blob(self,file_name = 'file'):
    '''returns an anvil blob media'''
    return anvil.js.to_media(self.proxy_pdf.output('blob'),content_type="application/pdf", name=f"{file_name}.pdf")
    
  def print(self):
    '''prints the pdf to the browser window'''
    pass

  def download(self):
    '''downloads the pdf file'''
    import anvil.media
    anvil.media.download(self.to_blob())