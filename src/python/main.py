from sanic import Sanic, response as res

app = Sanic('app')






if __name__ == '__main__':
    app.run(port=5000)