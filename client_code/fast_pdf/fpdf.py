from fpdf import FPDF

class CustomFPDF(FPDF):    
  def footer(self):
    try:
      if not hasattr(self, 'footer_callback') or self.header_callback is None: return
      self.footer_callback(self)
    except Exception as e:
      print('footer error',e,self.page_no())
      pass

  def cell(self,width,height,text,border = 0, ln = 1, align='L'):
    
    self.text(self.get_x(),self.get_y(),text)

    
    self.set_x(self.get_x()+width)
    if ln==1: 
      self.set_y(self.get_y()+height)
      self.set_x(10)

  def header(self):
    try:
      if not hasattr(self, 'header_callback') or self.header_callback is None: return
      self.header_callback(self)
    except Exception as e:
      print('header error',e,self.page_no())

  def add_image(self,image_data,x=0,y=0,w=0,h=0,alias='',compression='MEDIUM',rotation=0):
    '''Takes an image in form of a blob and prints it on the pdf'''
    from . import utils
    pil_img = utils.media_obj_to_pil(image_data)
    self.image(pil_img,x,y,w,h)
