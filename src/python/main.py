from sanic import Sanic, response as res
from sanic_cors import CORS, cross_origin #pip install Sanic-Cors
import sys
sys.path.append('../')
from python.nlp import sim_res_search, GetSummary, readingTime




app = Sanic(__name__)

@app.get('/sanic/api/users')
async def get_users(req):
  from python.database import get_users
  return res.json(await get_users())


@app.post('/sanic/api/users')
async def post_user(req):
  from python.database import create_user
  user = req.json

  user['id'] = await create_user(user)
  return res.json(user)


@app.delete('/sanic/api/users/<user_id:int>')
async def delete_user_by_id(req, user_id):
  from python.database import delete_user
  await delete_user(user_id)
  return res.text('OK')



@app.get('/sanic/api/articles')
async def get_articles(req):
  from python.database import get_articles
  return res.json(await get_articles())




@app.post('/sanic/api/articles')
async def post_article(req):
    from python.database import add_article
    article = req.json
    
    article['id'] = await add_article(article)
    return res.json(article)



@app.delete('/sanic/api/articles/<article_id:int>')
async def delete_article_by_id(req, article_id):
    from python.database import delete_article
    await delete_article(article_id)
    return res.text('OK')



@app.route('/sanic/api/search', methods=['POST', 'OPTIONS'])
@cross_origin(app)
async def post_search(req):
    from python.database import get_articles
    search = req.json
    print(search)
  
    data_frame = await get_articles()
  
    for article in data_frame:
      doc = article['text']
      score_result = sim_res_search(search, doc)
      summary_result = GetSummary(doc)
      fullText = readingTime(doc)
      sumText = readingTime(summary_result)
      #print(score_result)
      article['score'] = score_result
      article['summary'] = summary_result
      article['Full-RedingTime'] = fullText
      article['Summery-RedingTime'] = sumText
      
      
    return res.json(data_frame)

""" @app.get('/sanic/api/articles/result')
async def post_proccesed(req):
  from database import get_articles
  
  data_frame = await get_articles()
  
  for article in data_frame:
    doc = article['text']
    score_result = sim_res_search(, doc)
    summary_result = GetSummary(doc)
  for article in data_frame:
    article['score'] = score_result
    article['summary'] = summary_result
  
  return res.json(data_frame) """

if __name__ == "__main__":
  app.run(port=8000)