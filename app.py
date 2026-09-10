from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("registration.html")
@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    email=request.form['email']
    Rollno=request.form['Rollno']
    year=request.form['year']
    return render_template('successful.html',name=name,year=year)
if __name__=="__main__":
    app.run(debug=True)
    