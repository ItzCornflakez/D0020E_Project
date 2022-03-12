from __init__ import create_app
import webbrowser
from threading import Timer

app = create_app()

Timer(1, webbrowser.open_new('http://127.0.0.1:5000/')).start();
app.run(debug=True)



