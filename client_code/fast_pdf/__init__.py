"""
Main Document Class that acts as a wrapper for client and server side PDF Creation
Browser Library: JSPDF
Server Library: FPDF2 (Reference implementation)

Fpdf2 https://pyfpdf.github.io/fpdf2/index.html is strictly used as a reference implementation
The goal is to create pdfs client and server side without round trips and a unified sdk.

Subtle differences between server and client side implementation/results are possible!
"""

import anvil.server
import anvil.js
import anvil.media

from . import utils


class Document:
  def __init__(self):
    self.server_side = anvil.is_server_side()
    self._set_base_library(anvil.is_server_side())
    
  def _set_base_library(self,is_server_side):
    '''
    Sets the base implementaion of the library as a doc object
    This class primary purpose is to provide a common interface & code completion
    between fpdf2 and the python implementation of jspdf
    '''
    if not self.server_side:
      from .jspdf import jsPdf
      self.doc = jsPdf()
      self._proxy_doc = self.doc.doc
    else:
      from fpdf import FPDF
      self.doc = FPDF()
      self._proxy_doc = self.doc


  def add_page(self):
    self.doc.add_page()

  def set_font(self,font_name,size):
    self.doc.set_font(font_name,size=size)
      
  def cell(self,width,height,text):
    self.doc.cell(width,height, text, border = 0, ln = 1)

  
  def to_blob(self,file_name = 'file'):
    '''returns an anvil blob media'''
    if self.server_side:
      byte_string = bytes(self.doc.output())
      return anvil.BlobMedia("application/pdf", byte_string, name=f"{file_name}.pdf")
    else:
      return anvil.js.to_media(self._proxy_doc.output('blob'),content_type="application/pdf", name=f"{file_name}.pdf")

  def _to_base_64(self):
    return doc.output('bloburi')

  ###########################
  #Display modes of the pdf
  ############################
  
  def print(self):
    '''prints the pdf to the browser window'''
    try:
      from anvil.js.window import printJS
      printJS({'printable': base_string, 'type': 'pdf', 'base64': True})
    except Exception as e:
      print('Warning could not print document',e)


  def download(self):
    '''downloads the pdf file'''
    import anvil.media
    anvil.media.download(self.to_blob())

  def preview(self):
    pass