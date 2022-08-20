import pdftotext
from six.moves.urllib.request import urlopen
import io
import re

def helper(url):
  remote_file = urlopen(url).read()
  memory_file = io.BytesIO(remote_file)
  pdf = pdftotext.PDF(memory_file)
  content = ''
  for data in pdf:
    content = content + re.sub('\W+', ' ', "".join(data))
  return content
