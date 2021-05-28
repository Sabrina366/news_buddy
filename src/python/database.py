from databases import Database

db = Database('sqlite:C:/Users/sabri/Desktop/news_buddy/news-buddy.db')

async def get(query, values={}):
  rows = await db.fetch_all(query=query, values=values)
  dicts = []
  for row in rows:
    dicts.append(dict(row))
  return dicts


async def run(query, values={}):
  return await db.execute(query=query, values=values)

async def get_users():
  return await get('SELECT * FROM users')


async def create_user(user):
  query = 'INSERT INTO users(username, password) VALUES(:username, :password)'
  return await run(query, {"username": user['username'], "password": user['password']})


async def delete_user(id):
  return await run('DELETE FROM users WHERE id = :id', {"id": id})


async def get_articles():
  return await get('SELECT * FROM articles')


async def add_article(article):
  query = 'INSERT INTO articles(title, author, pub_date, text, timestamp, url) VALUES(:title, :author, :pub_date, :text, :timestamp, :url)'
  return await run(query, {"title": article['title'], "author": article['author'], "pub_date": article['pub_date'], "text": article['text'], "timestamp": article['timestamp'], "url": article['url']})

async def delete_article(id):
    return await run('DELETE FROM articles WHERE id = :id', {"id": id})
