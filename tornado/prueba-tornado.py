# Tornado is a Python web framework and asynchronous networking library,

# https://www.tornadoweb.org/en/stable/

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    port = 8888
    url = "http://localhost:" + str(port)
    print("Open your broser at ", url)
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
