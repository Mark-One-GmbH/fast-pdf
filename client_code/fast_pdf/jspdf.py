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
    
    self.orientation = parent.orientation

    if self.get_orientation() == 'landscape':
      self.page_width = parent.page_height
      self.page_height = parent.page_width

    #JS PDF Proxy Object
    from anvil.js.window import jspdf
    self.doc = jspdf.jsPDF(self.get_orientation(), 'mm',[self.page_width,self.page_height])
    
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

  def get_orientation(self):
    return 'portrait' if self.orientation == 'P' else 'landscape'

  def header(self): 
    # get current font attributes
    font_tuple = self.current_font
    
    self._reset_x()
    self.current_y = self.margin_top
    self.header_callback(self)

    #reset current font attributes
    if font_tuple:
      font_name,style,size = font_tuple
      self.set_font(font_name,style,size)
    


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
      font_name,style,size = font_tuple
      self.set_font(font_name,style,size)

    
  def add_page(self,orientation='P'):
    self.page_number += 1

    self.orientation = orientation
    #ignore first page since fpdf start with 0 pages but js pdf with 1
    if self.first_page:
      self.first_page = False
    else:
      self.doc.addPage('a4',self.get_orientation())
      
    self.footer()
    self._reset_y()
    self.header()
    self._reset_x()
    
  def will_page_break(self,height):
    return self.current_y + height + self.margin_bottom + self.footer_height >= self.page_height

  def add_font(self,file_name,font_name,base_64_font,font_style=''):
    self.doc.addFileToVFS(file_name, base_64_font)
    self.doc.addFont(file_name, font_name, font_style)
    
  def set_font(self,font_name,style='',size=10):
    self.current_font = (font_name,style,size)
    self.doc.setFont(font_name,style)
    self.doc.setFontSize(size)

  def _check_new_page(self,offset):
    if self.auto_page_break and self.current_y + offset + self.margin_bottom + self.footer_height >= self.page_height: 
      self.add_page(orientation=self.orientation)

  def _reset_x(self):
    self.current_x = self.margin_left

  def _reset_y(self):
    self.current_y = self.margin_top

  def vertical_text(self,width,height,text,border = 0, ln = 1, align='L', fill=False):
    self.cell(width,height,text,border=border,ln=ln,align=align,fill=fill, rotate = 90)
    
  def cell(self,width,height,text,border = 0, ln = 1, align='L', fill=False, rotate=0):
    #check if new page must be added
    self._check_new_page(height)

    if fill:
      rect_height = self.doc.getTextDimensions(text).get('w') + 2 if rotate == 90 else height
      add_height = self.doc.getTextDimensions(text).get('w') + 1 if rotate == 90 else 0
      rect_width = height if rotate == 90 else width
      self.doc.rect(self.current_x, self.current_y - add_height, rect_width, rect_height, 'F')

    font_name,style,font_size = self.current_font
    add_height = (height/2 + font_size * 0.106) if isinstance(height,(int,float)) and isinstance(font_size,(int,float)) else 4

    #consider rotate
    add_height -= height if rotate == 90 else 0
    add_width = (height/2 + font_size * 0.106) if rotate == 90 else 0
    add_height = 0 if rotate == 90 else add_height

    if align == 'C':
      self.doc.text(text,self.current_x + width/2, self.current_y+add_height,{'align':'center', 'angle':rotate})
    elif align == 'R':
      self.doc.text(text + ' ',self.current_x + width, self.current_y+add_height,{'align':'right', 'angle':rotate})
    else:
      self.doc.text(text,self.current_x + add_width, self.current_y+add_height,{'align':'left', 'angle':rotate})

    
    self.current_x += width
    if ln==1: 
      self.current_y += height
      self._reset_x()

  def multi_cell(self,width,height,text,border = 0, ln = 1, align='L'):
    # splits the text into parts
    words_list = text.split(' ')

    current_row_text = ''
    for word in words_list:
      # in new lines when text is longer that actual cell -> shorten text until it fits and redo it until whole word is done
      if not current_row_text and self.doc.getTextDimensions(word).get('w') > width:
        current_row_text = word
        while self.doc.getTextDimensions(current_row_text).get('w') > width: # loop over and cut last character of word
          current_row_text = current_row_text[:-1]
          if self.doc.getTextDimensions(current_row_text).get('w') <= width: # if word fits -> make cell and set remaining word - if it is shorter than cell -> continue, if it is larger -> redo cycle
            self.cell(width,height,current_row_text,border=border,ln=1)
            word = word[len(current_row_text):]
            current_row_text = word
        current_row_text += ' '
        continue

      # if text plus word is larger than cell -> append cell and start new row
      if self.doc.getTextDimensions(current_row_text + word).get('w') >= width:
        self.cell(width,height,current_row_text,border=border,ln=1)
        current_row_text = ''
        
      current_row_text += word + ' '

    # in the end if there is still a text to append
    if current_row_text:
      self.cell(width,height,current_row_text,border=border,ln=1)
      

  def line(self,x_start,y_start,x_end,y_end):
    self.doc.line(x_start,y_start,x_end,y_end)

  def set_text_color(self,color_1,color_2=None,color_3=None):
    self.doc.setTextColor(color_1,color_2,color_3)

  def set_draw_color(self,color_1,color_2=None,color_3=None):
    if color_2 and color_3:
      self.doc.setDrawColor(color_1,color_2,color_3)
    else:
      self.doc.setDrawColor(color_1)

  def set_fill_color(self,color_1,color_2=None,color_3=None):
    self.doc.setFillColor(color_1,color_2,color_3)

  def set_line_width(self,line_width):
    self.doc.setLineWidth(line_width)

  def get_x(self):
    return self.current_x

  def get_y(self):
    return self.current_y

  def rotate(self,angle):
    self.doc.rotate(angle)
    
  def doc(self,width, height, text):
    self.doc.text(text,height,width)

  def add_image(self,image_data,x=0,y=0,w=0,h=0,alias='',compression='FAST',rotation=0):
    '''Takes an image in form of a blob and prints it on the pdf'''
    from . import utils
    b64_image = utils.media_obj_to_base64(image_data)
    self.doc.addImage(b64_image,'JPEG',x,y,w,h,alias,compression,rotation)

  def page_no(self):
    return self.page_number


def get_additional_height_dict():
  return {
    6 : 0.62, #check
    7 : 0.73,
    8 : 0.84, #check
    9 : 0.95,
    10 : 1.06, #check
    11 : 1.17,
    12 : 1.28, #check
    13 : 1.38,
    14 : 1.48, #check
    15 : 1.4,
    16 : 1.7, #check
    17 : 1.66,
    18 : 1.92, #check
    19 : 2,
    20 : 2.12, #check
    11 : 2.33,
    22 : 2.34, #check
    23 : 2.62,
    24 : 2.54, #check
    25 : 2.86,
    26 : 2.76, #check
    27 : 2.62,
    28 : 2.96, #check
    29 : 2.86,
    30 : 3.18, #check
    40 : 4.26, #check
  }