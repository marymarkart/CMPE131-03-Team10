from app import models, db, flaskObj, forms
from flask import  flash, request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required

# Create the database to manage the data
db.create_all()

# Search page (Rafael)
@flaskObj.route('/')
def Home():
    return render_template("Home.html")

# Log in (Rafael)
@flaskObj.route('/login', methods = ['GET', 'POST'])
def login():
    loginForm = forms.LoginForm()
    email = loginForm.email.data
    password = loginForm.password.data
    if loginForm.validate():
        # We try to find a matching email and password in the database
        user = models.UserModel.query.filter_by(email = str(email)).first()
        if not user or not models.UserModel.check_password(user, password):
            flash('Your password was incorrect, or the account does not exist. Please try again.')
            return redirect('/login')
        login_user(user)
        return 'Logged in successfully, you may return to the home page'
    return render_template("Login.html", form = loginForm)

# Sign up (Rafael)
@flaskObj.route('/signup', methods = ['GET', 'POST'])
def signup():
    signupForm = forms.SignUpForm()
    if request.method == 'POST' and signupForm.validate():
        email = signupForm.email.data
        password = signupForm.password.data
        user = models.UserModel(email = email, password_hash = password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'Created account succesfully! Please log in :)'
    return render_template("Signup.html", form = signupForm)

# Profile (Rafael)
@flaskObj.route('/profile')
@login_required
def profile():
    loggedUser = models.UserModel.query.filter_by(id = current_user.get_id()).first() 
    return render_template("Profile.html", form = loggedUser)

# Logout (Rafael)
@flaskObj.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Succesfully logged out, you may return to the home page'

# Delete account (Rafael)
@flaskObj.route('/deleteaccount')
@login_required
def deleteaccount():
    if current_user.is_authenticated : 
        loggedUser = models.UserModel.query.filter_by(id = current_user.get_id()).first() 
        print('DELETING USER! : ' + str(loggedUser))
        db.session.delete(loggedUser)
        db.session.commit()
        logout_user()
    return 'Succesfully deleted account, you may return to the home page'

# Cart (Mohammad)
@flaskObj.route('/cart',methods=['GET','POST'])
@login_required
def cart():
    cart =forms.AddtoCartForm()
    # Adds whatever is pressed on to the Cart database
    if cart.validate_on_submit():
        userid = request.form.get('userid2')
        itemid = request.form.get('itemid2')
        itemname = request.form.get('itemname2')
        itemprice = request.form.get('itemprice2')
        itemdescription = request.form.get('itemdescription2')
        itemimage = request.form.get('itemimage2')
        
        cartitem = models.CartModel(userid=userid, productname=itemname,productprice=itemprice,productdescription=itemdescription,productimage=itemimage )
        #cartitem = models.CartModel(userid=userid2,itemid=itemid2)
        db.session.add(cartitem)
       
        db.session.commit()
        print('Item added')

    return redirect('/')

@flaskObj.route('/usercart',methods=['GET','POST'])
def usercart():
    total =0
    current=models.CartModel.query.all()
    currentid=current_user.get_id()
    if request.method == 'POST':
        return redirect('/checkout')
    
    return render_template('usercart.html',current=current,currentid=currentid)

@flaskObj.route('/checkout',methods=['GET','POST'])
def checkout():
    form = forms.CheckoutForm()
    if form.validate_on_submit():
        return redirect('/Placed')
    return render_template('checkout.html',form=form)

@flaskObj.route('/Placed',methods=['GET','POST'])
@login_required
def Placed():
    #Confirms to customer that their product has been posted then allows them to go to Search
    form = forms.PostProductForm()
    if request.method == 'GET':
        submit = forms.SubmitField('Home')
        return render_template('Placed.html', home = submit,form = form)
    if request.method == 'POST':
        return redirect('/')
 
# Post product success (Mohammad)
@flaskObj.route('/postProductSuccess',methods=['GET','POST'])
@login_required
def postProductSuccess():
    #Confirms to customer that their product has been posted then allows them to go to Search
    form = forms.PostProductForm()
    if request.method == 'GET':
        submit = forms.SubmitField('Home')
        return render_template('PostedProductSuccess.html', home = submit,form = form)
    if request.method == 'POST':
        return redirect('/')

# Item gallery (Mohammad)
@flaskObj.route('/itemgallery',methods=['GET','POST'])
def Gallery():
  form = forms.SearchForm()
  if request.method == 'GET':
      return render_template('ItemGallery.html', form=form)
  if request.method == 'POST':
      return redirect('/search')

# Item Search (Mohammad)
@flaskObj.route('/search',methods=['POST'])
def SearchItem():
    #When search is clicked, the searched phrase is compared to the products database to display all matches
    form = forms.SearchForm()
    cart = forms.AddtoCartForm()
    productList = []
    searchedphrase = models.ProductModel.query.all()

    #if request.method == 'POST':

    if form.validate_on_submit():
        result = request.form['searchbox']
        product = models.ProductModel.query.filter(models.ProductModel.productname == result).first()

    for i in searchedphrase:
        if (i.productname == result):
            productList.append(i.productname)

    
    return render_template('Search.html', result=result,form=form, searchedphrase=searchedphrase, product=product, productList=productList, cart=cart)


# Post product page (Mohammad)
@flaskObj.route('/PostProduct', methods=['GET','POST'])
@login_required
def Product():
  #Saves whatever is inputed into the products databse
  form = forms.PostProductForm()
  if request.method == 'GET':
      return render_template('ListItemForSelling.html', form=form)
  if request.method == 'POST':
      product = models.ProductModel(productname = form.productname.data, productprice = form.productprice.data, productdescription = form.productdescription.data, productimage = form.productimage.data)
      db.session.add(product)
      db.session.commit()
      return redirect('/postProductSuccess')

# Item seller (Umesh)
@login_required
@flaskObj.route('/seller')
def seller():
    return 'seller'

# Item rating (Umesh)
@login_required
@flaskObj.route('/rating')
def rating():
    return render_template('RateItem.html')

