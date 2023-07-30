from flask import Flask,render_template,request,url_for,flash,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key='roi'

#Connection sa Database
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='crudpython'

mysql=MySQL(app)

@app.route('/')
def Home():
    #pang call nang or view nang mga data
    cru=mysql.connection.cursor()
    #pang execute nang database
    cru.execute("SELECT * FROM tbl_user")
    data=cru.fetchall()
    cru.close()
    
    return render_template('index.html',users=data)
#ADD
@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        flash("AYUN PUMASOK")
        email=request.form['email']
        name=request.form['name']
        password=request.form['password']
   # pang connect sa database at yung cursor is pang trigger
    sql=mysql.connection.cursor()
    sql.execute("INSERT INTO tbl_user(email,name,password) VALUES(%s,%s,%s)",(email,name,password))
    mysql.connection.commit()
    return redirect(url_for("Home"))
#DELETE
@app.route('/delete/<string:id_data>', methods= ['GET','POST'])
# def delete(id_data):
#     flash("AYUN TINANGGAL")
#     sql=mysql.connection.cursor()
#     sql.execute("DELETE FROM tbl_user WHERE id=%s", [id_data])
#     mysql.connection.commit()
#     return redirect(url_for("Home"))
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    sql = mysql.connection.cursor()
    sql.execute("DELETE FROM tbl_user WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Home'))



@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=='POST':
     
         id_data=request.form['id']
         email=request.form['email']
         name=request.form['name']
         password=request.form['password']
         sql=mysql.connection.cursor()
         sql.execute("UPDATE tbl_user SET email=%s, name=%s, password=%s WHERE id=%s", (email, name, password, id_data))
         mysql.connection.commit()
         
         flash("NA UPDATE ANG IYONG INFO")
         return redirect(url_for("Home"))
    
    
if __name__=='__main__':
    app.run(debug=True)
 