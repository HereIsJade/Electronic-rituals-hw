from flask import Flask, request,render_template
import songAnalyzer


app=Flask(__name__)

@app.route('/')
def home():
    # name=request.args.get('name','no one')
    return render_template("home.html")
    # return render_template("home.html",name=name,age=age)
    # return "heyyy "+name #http://127.0.0.1:5000/?name=ada

@app.route('/create')
def create():
    artist=request.args.get('artist','')
    song=request.args.get('song','')
    advice=songAnalyzer.getAdvice(artist,song)
    return render_template('home.html',advice=advice)

if __name__ =='__main__':
    app.run(debug=True)
