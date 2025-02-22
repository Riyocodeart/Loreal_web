from flask import Flask ,render_template,request, url_for

from flask_mysqldb import MySQL

from flask import send_from_directory


app = Flask(__name__, static_folder="static")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1324abc@2908"
app.config['MYSQL_DB'] = "users_db"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)





@app.route('/Login', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users (name,email) VALUES (%s,%s)",(username,email))
         
        mysql.connection.commit()

        cur.close()

        return "Success" 


    return render_template('login.html')

@app.route('/')
def home():
    return render_template('homepage.html')



@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    usersDetails = cur.fetchall()
    cur.close()

    print("Fetched Users:", usersDetails)

    if usersDetails:
        return render_template('users.html',usersDetails=usersDetails)
    else:
        return "No users found"    

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)          

@app.route('/profile')
def profile():
    return render_template('profile.html')

   
@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True, port=7000)
