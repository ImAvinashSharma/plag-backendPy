import typesense
from fastapi import FastAPI
from pydantic import BaseModel
from pdfReader import *

app = FastAPI()

client = typesense.Client({
  'api_key': 'Hu52dwsas2AdxdE',
  'nodes': [{
    'host': '13.232.190.111',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 3
})

app = FastAPI()

class Item(BaseModel):
  titleId :str
  title :str
  createdOn :str
  url :str
  authors: str
  summary : str

"""
TODO: need to change the summary to abstract
{
  "titleId":"12",
  "title":"hey ",
  "createdOn":"2022",
  "authors":"sadfsdaf",
  "url":"https://sih-data.s3.ap-south-1.amazonaws.com/A+study+of+yoga%2C+its+benefits+and+true+self.pdf",
  "summary":""
}
"""

@app.post("/")
async def pdftotext(item: Item):
  a = {}
  a['id'] = item.titleId
  a['title'] = item.title
  a['createdOn'] = int(item.createdOn)
  a['authors'] = item.authors
  a['url'] = item.url
  a['summary'] = item.summary
  a['content'] = helper(item.url)
  # client.collections['test'].documents.create(a)
  return a