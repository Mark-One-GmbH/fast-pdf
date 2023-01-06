import anvil.js

class jsPdf:
  def __init__(self):
    from anvil.js.window import jspdf
    self.doc = jspdf.jsPDF('p', 'mm','a4')

    self.top_margin = 20
    self.bottom_margin = 10
    self.left_margin = 10
    self.right_margin = 5
    
    self.page_height = 297
    self.page_width = 210
    
    self.current_x = self.left_margin
    self.current_y = self.top_margin

    
  def add_page(self):
    pass

  def set_font(self,font_name,size=10):
    self.doc.setFont(font_name,'','normal')
    self.doc.setFontSize(size)

  def _check_new_page(self,offset):
    if self.current_y + offset + self.bottom_margin >= self.page_height: 
      self.doc.addPage()
      self._reset_x()
      self._reset_y()

  def _reset_x(self):
    self.current_x = self.left_margin

  def _reset_y(self):
    self.current_y = self.top_margin
    
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

    

