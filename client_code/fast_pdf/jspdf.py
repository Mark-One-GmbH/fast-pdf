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

    #JS PDF Proxy Object
    from anvil.js.window import jspdf
    self.doc = jspdf.jsPDF('p', 'mm','a4')
    
    #Cursor position
    self.current_x = 0
    self.current_y = 0

  def _header_callback(self):
    print('js header callback')
    self.doc.text('HEADER',10,10)

    
  def add_page(self):
    self._header_callback()
    self.doc.addPage()


  def set_font(self,font_name,size=10):
    self.doc.setFont(font_name,'','normal')
    self.doc.setFontSize(size)

  def _check_new_page(self,offset):
    if self.current_y + offset + self.margin_bottom >= self.page_height: 
      self.add_page()
      self._reset_x()
      self._reset_y()

  def _reset_x(self):
    self.current_x = self.margin_left

  def _reset_y(self):
    self.current_y = self.margin_top
    
  def cell(self,width,height,text,border = 0, ln = 1):
    #check if new page must be added
    self._check_new_page(height)
      
    self.doc.text(text,self.current_x,self.current_y)
    self.current_x += width
    if ln==1: 
      self.current_y += height
      self._reset_x()
    
  def doc(self,width, height, text):
    self.doc.text(text,height,width)

    

