"""
Utility functions for pdf interactions
"""

def media_obj_to_base64(media_obj):
  '''returns a base 64 representation of the pdf media obj'''
  import base64
  return base64.b64encode(media_obj.get_bytes()).decode('utf-8')
    
def print_pdf(blob_media,new_tab=False):
  '''prints an anvil blob media of type pdf'''
  if new_tab:
    import anvil.media
    anvil.media.print_media(blob_media)
  else:
    from anvil.js.window import printJS
    printJS({'printable':media_obj_to_base64(blob_media), 'type': 'pdf', 'base64': True})


def download_pdf(blob_media):
  import anvil.media
  anvil.media.download(blob_media)

def pdf_to_component(blob_media):
  from ..components.preview import preview
  comp = preview()
  comp.pdf_media = blob_media
  return comp

def media_obj_to_pil(blob_media):
  try:
    from PIL import Image
    from io import BytesIO
    return Image.open(BytesIO(blob_media.get_bytes()))
  except Exception as e:
    print('WARNING: image could not be converted')
        
