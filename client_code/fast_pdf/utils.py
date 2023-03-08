"""
Utility functions for pdf interactions
"""

def media_obj_to_base64(media_obj):
  '''returns a base 64 representation of the pdf media obj'''
  import base64
  return base64.b64encode(media_obj.get_bytes()).decode('utf-8')
    
def print_pdf(blob_media):
  '''prints an anvil blob media of type pdf'''
  try:
    from anvil.js.window import printJS
    printJS({'printable':media_obj_to_base64(blob_media), 'type': 'pdf', 'base64': True})
  except Exception as e:
    print('Warning could not print document',e)

def download_pdf(blob_media):
  import anvil.media
  anvil.media.download(blob_media)

def pdf_to_component(blob_media):
  from ..components.preview import preview
  comp =  preview()
  comp.pdf_media = blob_media
  return comp

def media_obj_to_pil(blob_media):
  try:
    from PIL import Image
    from io import BytesIO
    return Image.open(BytesIO(blob_media.get_bytes()))
  except Exception as e:
    print('WARNING: image could not be converted')
        
