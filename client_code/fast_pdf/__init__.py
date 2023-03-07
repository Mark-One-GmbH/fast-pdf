"""
Main Document Class that acts as a wrapper for client and server side PDF Creation
Browser Library: JSPDF  ->  https://raw.githack.com/MrRio/jsPDF/master/docs/index.html
Server Library: FPDF2 (Reference implementation) ->  https://pyfpdf.github.io/fpdf2/index.html

Fpdf2  is strictly used as a reference implementation
The goal is to create pdfs client and server side without round trips and a unified sdk.

Subtle differences between server and client side implementation/results are possible!
"""

import anvil.server
import anvil.js
import anvil.media

from . import utils


class Document:
  def __init__(self,page_height=297,page_width=210,margin_top=0,margin_bottom=0,margin_left=0,margin_right=0,header_height=0,footer_height=0):
    #Initial Variables that define the basic page layout
    self.page_height = page_height
    self.page_width = page_width
    self.margin_top = margin_top
    self.margin_bottom = margin_bottom
    self.margin_left = margin_left
    self.margin_right = margin_right
    self.header_height = header_height
    self.footer_height = footer_height
    
    self.server_side = anvil.is_server_side()
    
    #Set Base Renderer
    self._set_renderer(anvil.is_server_side())

    #State Variables

    
    
  def _set_renderer(self,is_server_side):
    '''
    Sets the base implementaion of the library as a document object
    This class primary purpose is to provide a common interface & code completion
    between fpdf2 and the python implementation of jspdf
    '''

    #Set proxy classes depending if code is executed on server or client runtime
    if not self.server_side:
      self._set_jspdf_renderer()
    else:
      self._set_fpdf_renderer()

    #initializations
    self.doc.set_font('Courier',size=12)

  def _set_jspdf_renderer(self):
    from .jspdf import jsPdf
    self.doc = jsPdf(self)
    self._proxy_doc = self.doc.doc

  def _set_fpdf_renderer(self):
    from .fpdf import CustomFPDF
    self.doc = CustomFPDF(self)
    self._proxy_doc = self.doc
    
  ###########################
  #Public Methods
  ###########################

  def set_footer_function(self,footer_func):
    self.doc.footer_callback = footer_func

  def set_header_function(self,header_func):
    self.doc.header_callback = header_func

  def add_page(self):
    self.doc.add_page()

  def set_font(self,font_name,size,style=''):
    self.doc.set_font(font_name,size=size)
      
  def cell(self,width,height,text,border=0,ln=0):
    self.doc.cell(width,height,text,border=border,ln=ln)

  def build_header(self):
    pass

  def build_footer(self):
    pass

  ###########################
  #Output functions
  ###########################
  
  def to_blob(self,file_name = 'file'):
    '''returns an anvil blob media with the type application/pdf'''
    if self.server_side:
      byte_string = bytes(self.doc.output())
      return anvil.BlobMedia("application/pdf", byte_string, name=f"{file_name}.pdf")
    else:
      return anvil.js.to_media(self._proxy_doc.output('blob'),content_type="application/pdf", name=f"{file_name}.pdf")


  ###########################
  #Display modes for the pdf
  ############################
  
  def print(self):
    '''prints the pdf to the browser window'''
    utils.print_pdf(self.to_blob())

  def download(self):
    '''downloads the pdf file'''
    utils.download_pdf(self.to_blob())

  def preview(self):
    '''Opens an alert to preview'''
    pdf_form = utils.pdf_to_component(self._proxy_doc.output('blob'))
    anvil.alert(pdf_form,large=True)

  def get_form(self):
    '''Returns a nestable component wich allows the pdf to be embedded into forms'''
    return utils.pdf_to_component(self.to_blob())