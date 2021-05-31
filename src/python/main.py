from sanic import Sanic, response as res
from nlp import sim_res_search

app = Sanic(__name__)

@app.get('/sanic/api/users')
async def get_users(req):
  from database import get_users
  return res.json(await get_users())


@app.post('/sanic/api/users')
async def post_user(req):
  from database import create_user
  user = req.json

  user['id'] = await create_user(user)
  return res.json(user)


@app.delete('/sanic/api/users/<user_id:int>')
async def delete_user_by_id(req, user_id):
  from database import delete_user
  await delete_user(user_id)
  return res.text('OK')



@app.get('/sanic/api/articles')
async def get_articles(req):
  from database import get_articles
  return res.json(await get_articles())

@app.get('/sanic/api/articles/result')
async def post_proccesed(req):
  from database import get_articles
  
  data_frame = await get_articles()
  
  for article in data_frame:
    doc = article['text']
    result = sim_res_search("hey i am a string" , doc)
    
  for article in data_frame:  
    article['score'] = result
    
  return res.json(data_frame)  
   


@app.post('/sanic/api/articles')
async def post_article(req):
    from database import add_article
    article = req.json
    
    article['id'] = await add_article(article)
    return res.json(article)



@app.delete('/sanic/api/articles/<article_id:int>')
async def delete_article_by_id(req, article_id):
    from database import delete_article
    await delete_article(article_id)
    return res.text('OK')






if __name__ == "__main__":
  app.run(port=8000)