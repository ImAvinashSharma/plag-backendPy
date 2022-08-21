import typesense
from fastapi import FastAPI
from pydantic import BaseModel
from pdfReader import *

app = FastAPI()

client = typesense.Client({
  'api_key': 'Hu52dwsas2AdxdE',
  'nodes': [{
    'host': '13.232.14.234',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 3
})

app = FastAPI()


# {
#   "titleId":"bbhhaa",
#   "title":"TCS",
#   "ResearcherName":"Avinash Sharma",
#   "GuideName":"Avinash Sharma",
#   "Keywords":"Avinash Sharma",
#   "Category":"Avinash Sharma",
#   "createdOn":"2022",
#   "url":"https://sih-data.s3.ap-south-1.amazonaws.com/DT20206890800_OL.pdf",
#   "abstract":"ntitlement You and your enrolled dependants will be entitled for 12 00 000 as a family floater coverage towards hospitalisation expenses over and above the individual basic coverage ii Premium For Higher Hospitalisation a part of the premium will be recovered from your salary and the differential"
# }

class Item(BaseModel):
  titleId :str
  title :str
  researcherName : str
  guideName :str
  keywords: str
  category : str
  createdOn :str
  url :str
  abstract :str

@app.post("/")
async def pdftotext(item: Item):
  a = {}
  a['titleId'] = item.titleId
  a['title'] = item.title
  a['researcherName'] = item.researcherName
  a['guideName'] = item.guideName
  a['keywords'] = item.keywords
  a['category'] = item.category
  a['createdOn'] = int(item.createdOn[:4])
  a['url'] = item.url
  a['abstract'] = item.abstract
  a['content'] = helper(item.url)
  client.collections['test'].documents.create(a)
  return a