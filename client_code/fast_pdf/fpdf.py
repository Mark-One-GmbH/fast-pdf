from fpdf import FPDF

class CustomFPDF(FPDF):
  def __init__(self,parent):
    #parent document
    self.parent = parent
    #Inherited Page layout
    self.page_height = parent.page_height
    self.page_width = parent.page_width
    self.margin_top = parent.margin_top
    self.margin_bottom = parent.margin_bottom
    self.margin_left = parent.margin_left
    self.margin_right = parent.margin_right
    self.header_height = parent.header_height
    self.footer_height = parent.footer_height
    
  
  def footer(self):
    try:
      self.footer_callback(self)
    except Exception as e:
      print('footer error',e)
      pass

  def header(self):
    try:
      self.header_callback(self)
    except Exception as e:
      print('header error',e)
