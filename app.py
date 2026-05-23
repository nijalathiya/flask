from flask import Flask,render_template,request,redirect

app = Flask(__name__)
setData =[]
@app.route("/")

def viewpage():
    return render_template("index.html",setData = setData)

@app.route("/addData")
def addData():
    name = request.args.get("name")
    age = request.args.get("age")
    

    dict = {"name": name,"age":age}
    # print(dict)
    setData.append(dict)
    print(setData)

    return redirect('/')

@app.route('/deleteData')
def deleteFun():

    deleteId = request.args.get('delete')

    setData.pop(int(deleteId))

    return redirect('/')


@app.route('/editData')
def editData():
    editId = request.args.get('edit')
    editData = setData[int(editId)]
    print(editData)

    return render_template("index.html" , editData = editData , setData = setData , editId = editId)