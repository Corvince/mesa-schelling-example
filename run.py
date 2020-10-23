from server import server
import os

port= int(os.getenv("PORT", 4200))

server.launch(port=port, open_browser=False)
