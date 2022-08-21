import pdftotext
from urllib.request import urlopen,Request
import io
import re

def helper(url):
  req = Request(
    url=url,
    headers={'User-Agent': 'Mozilla/5.0'}
  )
  remote_file = urlopen(req).read()
  memory_file = io.BytesIO(remote_file)
  pdf = pdftotext.PDF(memory_file)
  content = ''
  for data in pdf:
    content = content + re.sub('\W+', ' ', "".join(data))
  return content
