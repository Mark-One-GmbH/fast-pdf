from .. import fast_pdf
from datetime import datetime
import anvil.server
import anvil.media


def run():
  from .basic_pdf import create
  client_pdf = create()
  anvil.media.download(client_pdf)
  
  server_pdf = anvil.server.call('get_basic_pdf')
  anvil.media.download(server_pdf)

  
  
