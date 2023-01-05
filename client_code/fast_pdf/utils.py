"""
Utility functions for pdf interactions
"""

def media_obj_to_base64(media_obj):
  '''returns a base 64 representation of the pdf media obj'''
  import base64
  return base64.b64encode(self.to_blob().get_bytes()).decode('utf-8')
    
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

def preview_pdf(blob_media):
  from ..components.preview import preview
  return preview(blob_media)
  