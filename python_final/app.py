from flask import Flask,request,flash
from flask import render_template

app = Flask(__name__)
app.secret_key="djskhhujas2"
username_list=["小明","李华","xuzhichao","youge"]
password_list=["123456","123789","456789","000123"]

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/third')
def third():
    return render_template("index_first.html")

@app.route('/forth')
def forth():
    return render_template("index_second.html")

@app.route('/index1',methods=['POST','GET'])
def index1():
    return render_template("index_first.html")

@app.route('/index2',methods=['POST','GET'])
def index2():
    return render_template("index_second.html")

@app.route('/result1',methods=['POST'])
def result1():
    py_firstname = request.form['firstname']
    py_lastname = request.form['lastname']
    py_fullname = py_firstname.title() + " " + py_lastname.title()
    return render_template("result_first.html",fullname = py_fullname)

@app.route('/result2',methods=['POST'])
def result2():
    py_serch4letters = set(request.form['phrase']) & set(request.form['vowels'])
    word = request.form['phrase']
    py_vowels = request.form['vowels']
    found={}
    for i in word:
        if i in py_vowels:
            found.setdefault(i,0)
            found[i] += 1
    for k,v in found.items():
        jieguo = found
        return render_template("result_second.html",search4letters=jieguo,search=py_serch4letters)

@app.route('/index3',methods=['POST','GET'])
def index3():
    return render_template("homepage.html")

@app.route('/contact',methods=['get','post'])
def contact():
    return render_template("contact.html")


@app.route('/first',methods=['GET','POST'])
def first():
    return render_template('index.html')
# 此处用来返回到首页

@app.route('/second',methods=['GET','POST'])
def second():
    return render_template('login.html')

# 此处为改进后的登录，即只有在数据库中的用户才可以登录成功（目前只有列表中指定的用户）
@app.route('/login',methods=['get','post'])
def index():
    if request.method == "POST":
        user_name = request.form.get("username")
        user_pwd = request.form.get("password")
        if user_name in username_list and user_pwd in password_list:
            return render_template("index.html",username=user_name)
        else:
            flash("密码或账号有误，请重新输入！")
            return render_template("login.html")
    return render_template("login.html")

# 以下几行的注释代码为尚未实现用户登录和注册管理，即不用登录即可进入后台首页
    # @app.route('/index',methods=['get','post'])
    # def index():
    #   user = request.form['username']
    #   psw = request.form['password']
    #   return render_template("index.html",username=user , password=psw)

    # @app.route('/login',methods=['POST','GET'])
    # def login():
    #     return render_template("login.html")

@app.route('/register',methods=['get','post'])
def register():
    return render_template("register.html")
# 本项目尚未实现用户注册管理

@app.route('/result',methods=['get','post'])
def result():
    shopping_cart=request.form.getlist('dagou')
    list_shopping=" |  ".join(shopping_cart)
    return  render_template("result.html",list=list_shopping)



if __name__ == '__main__':
    app.run()
