from flask import Flask, render_template, request
from message import get_posts, create_post
app= Flask(__name__)



@app.route("/", methods=['POST', 'GET'])
def home():

    if request.method =='GET':
    	pass
    if request.method =='POST':
    	name=request.form.get('name')
    	content=request.form.get('message')
    	create_post(name, content)

    posts=get_posts()

    return render_template('home.html', posts=posts)

if __name__=='__main__':
	app.run(debug=True)