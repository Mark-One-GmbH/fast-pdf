from fpdf import FPDF

class CustomFPDF(FPDF):    
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
