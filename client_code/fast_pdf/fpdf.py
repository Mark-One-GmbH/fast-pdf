from fpdf import FPDF

class CustomFPDF(FPDF):    
  def footer(self):
    try:
      if not hasattr(self, 'footer_callback') or self.header_callback is None: return
      self.footer_callback(self)
    except Exception as e:
      print('footer error',e)
      
  def header(self):
    try:
      if not hasattr(self, 'header_callback') or self.header_callback is None: return
      self.header_callback(self)
    except Exception as e:
      print('header error',e)
      
  def add_image(self,image_data,x=0,y=0,w=0,h=0,alias='',compression='MEDIUM',rotation=0):
    '''Takes an image in form of a blob and prints it on the pdf'''
    from . import utils
    pil_img = utils.media_obj_to_pil(image_data)
    self.image(pil_img,x,y,w,h)
    
  def vertical_text(self,width,height,text,border=0,ln=0,align='L',fill=False):
    self.rotate(90)
    self.cell(width, height, text, border =border, ln=ln, align=align, fill=fill)
    self.rotate(0)
