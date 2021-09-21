from flask import Flask,render_template,request,url_for,redirect,flash
import mysql
import mysql.connector as mysql
from flask_mysqldb import MySQL
import base64
import os
import os.path
from werkzeug import secure_filename



app=Flask(__name__)



app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="users"
app.config['MYSQL_PASSWORD']="hydax"
app.config['MYSQL_DB']="flap"

mysql=MySQL(app)

@app.route('/')
def main():
    return render_template("main.html")
    


@app.route('/users',methods=['GET'])


def user():
    
        cur=mysql.connection.cursor()
        users=cur.execute("SELECT*FROM catgg")
        if users>0:
            userDetails=cur.fetchall()
            return render_template('users.html',userDetails=userDetails)


@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/test')
def student():
    return render_template('test.html')

@app.route('/result',methods=['POST','GET'])
def result():
    
    if request.method=='POST':
        result=request.form
        Product_Name=result['Product_Name']
        cur=mysql.connection.cursor()
        cur.execute("delete from catgg where Product_Name='"+Product_Name+"'")
        mysql.connection.commit()
        cur.close()
        return " Records deleted Successfully"

@app.route('/resultt',methods=['POST','GET'])
def resultt():
    
    if request.method=='POST':
        result=request.form
        Product_Name=result['Product_Name']
        Details=result['Details']
        Image=result['Image']
        Video=result['Video']
        cur=mysql.connection.cursor()
        cur.execute("UPDATE catgg SET  Product_Name=%s,Details=%s,Image=%s,Video=%s,where Product_Name=%s",(Product_Name,Details,Image,Video))
        mysql.connection.commit()
        cur.close()
        return " Records Updated Successfully"






   

@app.route('/',methods=['POST'])
def aa():
    if request.method=='POST':
        Product_Name=request.form['Product_Name']
        Details=request.form['Details']
        image=request.form['image']
        video=request.form['video']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO catgg(Product_Name,Details,image,video)VALUES(%s,%s,%s,%s)",(Product_Name,Details,image,video))
        mysql.connection.commit()
        cur.close()
        return "data inserted successfully into a database"
    return render_template('aa.html')









    
@app.route("/aa.html")    
def second():
    templateData={
        'title':'SETTINGS PAGE'
        }
    return render_template('aa.html',**templateData)


@app.route('/userr',methods=['GET'])


def userr():
    
        cur=mysql.connection.cursor()
        userr=cur.execute("SELECT*FROM catgg")
        if userr>0:
            userrDetails=cur.fetchall()
            return render_template('userr.html',userrDetails=userrDetails)
        
        
        




    

   



@app.route('/upload_file',methods=['POST'])
def upload_file():
	if request.method=='POST':
		f=request.files['file']
		f.save(secure_filename(f.filename))
		url=f.filename
		return 'image uploaded successfully'
    

    
    

if __name__=="__main__":
    app.run(debug=True)




