import anvil.js

class jsPdf:
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
    
    self.footer_callback = parent.footer_function
    self.header_callback = parent.header_function

    #JS PDF Proxy Object
    from anvil.js.window import jspdf
    self.doc = jspdf.jsPDF('p', 'mm',[self.page_width,self.page_height])
    
    #Cursor position
    self.current_x = 0
    self.current_y = 0
    self._reset_x()
    self._reset_y()

    #Helper Flags
    self.auto_page_break = True
    self.first_page = True
    self.current_font = None
    self.page_number = 0

  def header(self): 
    # get current font attributes
    font_tuple = self.current_font
    
    self._reset_x()
    self.current_y = self.margin_top
    self.header_callback(self)

    #reset current font attributes
    if font_tuple:
      font_name,size,style = font_tuple
      self.set_font(font_name,size,style)
    


  def footer(self):
    # get current font attributes
    font_tuple = self.current_font
    
    self._reset_x()
    self.current_y = self.page_height - self.margin_bottom - self.footer_height
    self.auto_page_break = False
    self.footer_callback(self)
    self.auto_page_break = True

    #reset current font attributes
    if font_tuple:
      font_name,size,style = font_tuple
      self.set_font(font_name,size,style)

    
  def add_page(self):
    self.page_number += 1
    
    #ignore first page since fpdf start with 0 pages but js pdf with 1
    if self.first_page:
      self.first_page = False
    else:
      self.doc.addPage()
      
    self.footer()
    self._reset_y()
    self.header()
    self._reset_x()

  def add_font(self,file_name,font_name,base_64_font,font_style=''):
    self.doc.addFileToVFS(file_name, base_64_font)
    self.doc.addFont(file_name, font_name, font_style)
    
  def set_font(self,font_name,size=10,style=''):
    self.current_font = (font_name,size,style)
    self.doc.setFont(font_name,style)
    self.doc.setFontSize(size)

  def _check_new_page(self,offset):
    if self.auto_page_break and self.current_y + offset + self.margin_bottom + self.footer_height >= self.page_height: 
      self.add_page()

  def _reset_x(self):
    self.current_x = self.margin_left

  def _reset_y(self):
    self.current_y = self.margin_top + self.header_height
    
  def cell(self,width,height,text,border = 0, ln = 1, align='L'):
    #check if new page must be added
    self._check_new_page(height)

    if align == 'C':
      self.doc.text(text,self.current_x + width/2,self.current_y,'center')
    elif align == 'R':
      self.doc.text(text,self.current_x + width,self.current_y,'right')
    else:
      self.doc.text(text,self.current_x,self.current_y,'left')
    
    self.current_x += width
    if ln==1: 
      self.current_y += height
      self._reset_x()

  def line(self,x_start,y_start,x_end,y_end):
    self.doc.line(x_start,y_start,x_end,y_end)

  def set_text_color(self,color_1,color_2=None,color_3=None):
    self.doc.setTextColor(color_1,color_2,color_3)

  def set_draw_color(self,color_1,color_2=None,color_3=None):
    self.doc.setDrawColor(color_1,color_2,color_3)
    
  def doc(self,width, height, text):
    self.doc.text(text,height,width)

  def add_image(self,image_data,x=0,y=0,w=0,h=0,alias='',compression='FAST',rotation=0):
    '''Takes an image in form of a blob and prints it on the pdf'''
    from . import utils
    b64_image = utils.media_obj_to_base64(image_data)
    self.doc.addImage(b64_image,'JPEG',x,y,w,h,alias,compression,rotation)

  def page_no(self):
    return self.page_number

