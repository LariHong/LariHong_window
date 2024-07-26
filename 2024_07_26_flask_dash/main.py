from flask import Flask,render_template,request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import data
from dashboard.board1 import app1
from dashboard.board2 import app2

app=Flask(__name__)

areas=[tup[0] for tup in data.get_areas()]
@app.route("/")
def index():
    return render_template("index.html.jinja")

@app.route("/index1")
def index1():
    content="daily news around Taiwan and present the perspectives of Taiwan and Asia."

    selected_area=request.args.get('area')

    selected_area='士林區' if selected_area is None else selected_area
    detail_snaes=data.get_snaOfArea(area=selected_area)

    return render_template("index1.html.jinja",left=content,areas=areas,show_area=selected_area,show_detail=detail_snaes)

#這裡要和board1 對應 但最後不需要+/
application = DispatcherMiddleware(app, {
    '/dashboard/app1': app1.server,
    '/dashboard/app2': app2.server
})

if __name__ == "__main__":
    run_simple("localhost",8081,application,use_debugger=True,reloader_type=True)
     
    
    