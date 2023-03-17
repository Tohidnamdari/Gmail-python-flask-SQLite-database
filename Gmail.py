from flask import Flask,render_template,request,redirect,make_response,flash

from database import db
db.create_all()
from database import Users,send_m
from database import app


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        in_email = request.form.get('in_email')
        in_pass = request.form.get('in_pass')
        found=False
        for u in range(len(Users.query.all())):
            if in_email==Users.query.all()[u].email and in_pass==Users.query.all()[u].password:
                flash("کاربر وارد شد", "success")
                response=make_response(redirect('/'))
                response.set_cookie("user",in_email)
                found = True
                return response
        if found==False:
                flash("ایمیل یا رمز عبور اشتباه است", "danger")
                return render_template('login.html',user=request.cookies.get("in_email"))
    return render_template('login.html',user=request.cookies.get("user"))
@app.route('/register',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        re_name = request.form.get('re_name')
        re_email = request.form.get('re_email')
        re_password = request.form.get('re_password')
        flash("کاربر ثبت نام شد", "success")
        admin=Users(name=re_name,password=re_password,email=re_email)
        print(admin)
        db.session.add(admin)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('Register.html',user=request.cookies.get("in_email"))
@app.route('/',methods=['POST','GET'])
def index():

    return render_template('index.html', user=request.cookies.get("user"),Users=Users.query.all())
@app.route("/logout")
def logout():
    flash("کاربر خارج شد", "danger")
    response = make_response(redirect('/login'))
    response.delete_cookie("user")
    return response
@app.route('/send',methods=['POST','GET'])
def send():
    if request.cookies.get("user"):
        if request.method == 'POST':
            message1 = request.form.get('message')
            email_mag1 = request.form.get('email_mag')
            email_mab1 = request.form.get('email_mab')
            flash("پیغام ارسال شد", "success")
            admin2 = send_m(email_mab=email_mab1, email_mag=email_mag1, message=message1)
            db.session.add(admin2)
            db.session.commit()
            return redirect('/')
        return render_template('send.html', user=request.cookies.get("user"))
    else:
        return redirect('/login')

@app.route('/inbox', methods=['POST', 'GET'])
def inbox():
    if request.cookies.get("user"):
        message_in=send_m.query.filter_by(email_mag=request.cookies.get("user"))
        print(message_in)
        return render_template('inbox.html', user=request.cookies.get("user"),message_in=message_in)
    else:
        return redirect('/login')
@app.errorhandler(404)
def showerror(error):
    return render_template("error.html"),404

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80)
