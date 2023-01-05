import anvil.js

class jsPdf:
  def __init__(self):
    from anvil.js.window import jspdf
    self.doc = jspdf.jsPDF('p', 'mm')
    self.doc.setFont('helvetica','','normal')
    self.doc.setFontSize(10)
    
  def add_page(self):
    pass

  def set_font(self,font_name,size=10):
    pass

  def cell(self,width,height,text,border = 0, ln = 1):
    self.doc.text(text,10,10)
    
  def doc(self,width, height, text):
    self.doc.text(text,height,width)

    

