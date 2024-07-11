from flask import Flask,render_template,request
import data


app=Flask(__name__)

@app.route("/")
def index():
    content="daily news around Taiwan and present the perspectives of Taiwan and Asia."

    selected_area=request.args.get('area')
    areas=[tup[0] for tup in data.get_areas()]

    selected_area='士林區' if selected_area is None else selected_area
    
    return render_template("index.html.jinja",left=content,areas=areas,show_area=selected_area)

    
    
    