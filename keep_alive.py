from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def main():
  return '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>Discord Keep Alive</title>
      </head>
      <body>
        I'm alive!
      </body>
    </html>
  '''

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()