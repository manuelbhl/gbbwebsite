


class Inhouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resvno = db.Column(db.String(50), nullable=False)
    room = db.Column(db.String(10), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    chkindate = db.Column(db.String(100))
    chkoutdate = db.Column(db.String(100))
    phonenum = db.Column(db.String(100))
    note = db.Column(db.String(100))
    misc = db.Column(db.String(100))
    guestnum = db.Column(db.Integer)
    daynum = db.Column(db.Integer)
    unitnum = db.Column(db.Integer)
    deposit = db.Column(db.Integer)
    totpay = db.Column(db.Integer)
    miscpay = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    pay_date = db.Column(db.Date)
    chkinsw = db.Column(db.Boolean, default=False)
    chkoutsw = db.Column(db.Boolean, default=False)
    cancelsw = db.Column(db.Boolean, default=False) 
    paysw = db.Column(db.Boolean, default=False) 
    filler1sw = db.Column(db.Boolean, default=False)     

    def __repr__(self):
        return f'<Inhouse {self.firstname}>'


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resvno = db.Column(db.String(50))
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    arrvdate = db.Column(db.String(100))
    chkoutdate = db.Column(db.String(100))
    phonenum = db.Column(db.String(100))
    guestnum = db.Column(db.Integer)
    daynum = db.Column(db.Integer)
    unitnum = db.Column(db.Integer)   
    cancelsw = db.Column(db.Boolean, default=False)
    deposit = db.Column(db.Integer)
    filler1sw = db.Column(db.Boolean, default=False) 
    filler2sw = db.Column(db.Boolean, default=False) 
    msg = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    

    def __repr__(self):
        return f'<Guest {self.firstname}>'


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    msg = db.Column(db.String(100), nullable=False)
    maildate = db.Column(db.Date)
    contsw = db.Column(db.Boolean, default=False, nullable=False) 
    investsw = db.Column(db.Boolean, default=False,nullable=False ) 
    mailsw = db.Column(db.Boolean, default=False) 
    filler1sw = db.Column(db.Boolean, default=False) 
    filler2sw = db.Column(db.Boolean, default=False) 
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    

    def __repr__(self):
        return f'<Contact {self.contname}>'

class Invest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investno = db.Column(db.String(50))
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    msg = db.Column(db.String(100), nullable=False)
    maildate = db.Column(db.Date)
    deposit = db.Column(db.Integer)
    totpay = db.Column(db.Integer)
    miscpay = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    pay_date = db.Column(db.Date)
    contsw = db.Column(db.Boolean, default=False, nullable=False) 
    investsw = db.Column(db.Boolean, default=False,nullable=False ) 
    mailsw = db.Column(db.Boolean, default=False) 
    filler1sw = db.Column(db.Boolean, default=False) 
    filler2sw = db.Column(db.Boolean, default=False) 
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    

 

@app.route('/formmail', methods=["POST"])
def formmail():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    message = "You have been subscribed to my email newsletter "    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("johne4196@gmail.com", "PASSWORD")     
    server.sendmail("johne4196@gmail.com", email, message)
    if not first_name or not last_name or not email:         
        error_statement = "All Form Fields Required..."         
        return render_template("subscribe.html",             
            error_statement = error_statement,
            first_name = first_name,
            Last_name=last_name, 
            email=email)




if __name__ == "__main__":
    app.run(debug=True)
    
