from app import models, db, flaskObj, forms
from flask import render_template
from flask import  flash, request, redirect

# Create the database to manage the data
db.create_all()

# Home page (Rafael)
@flaskObj.route('/')
def home():
    return render_template("Home.html")

# Log in (Rafael)
@flaskObj.route('/login')
def login():
    return render_template("Login.html")

# Sign up (Rafael)
@flaskObj.route('/signup')
def signup():
    return render_template("Signup.html")

# Profile (Rafael)
@flaskObj.route('/profile')
def profile():
    return render_template("Profile.html")

# Deleted account (Rafael)
@flaskObj.route('/deleteaccount')
def deleteaccount():
    models.User.query.delete()
    return 'Account succesfully deleted'

# Cart (Mohammad)
@flaskObj.route('/cart')
def cart():
    # Adds whatever is pressed on to the Cart database
    product_id = request.form.get('product_id')
    product= Product.query.filter_by(id=product_id).first()
    if request.method =="POST":
        u = Cart(productname= product.productname, productprice = product.productprice, productimage=product.productimage)
        db.session.add(u)
        db.session.commit()
    return render_template('cart.html')
 
# Post product success (Mohammad)
@flaskObj.route('/postProductSuccess',methods=['GET','POST'])
def postProductSuccess():
    #Confirms to customer that their product has been posted then allows them to go to home
    form = forms.PostProductForm()
    if request.method == 'GET':
        submit = forms.SubmitField('Home')
        return render_template('PostedProductSuccess.html', home=submit,form=form)
    if request.method == 'POST':
        return redirect('/')

# Item gallery (Mohammad)
@flaskObj.route('/itemgallery',methods=['GET','POST'])
def Home():
  form = forms.SearchForm()
  if request.method == 'GET':
      return render_template('ItemGallery.html', form=form)
  if request.method == 'POST':
      return redirect('/search')

# Item Search (Mohammad)
@flaskObj.route('/search',methods=['GET','POST'])
def searchresult():
    #When search is clicked, the searched phrase is compared to the products database to display all matches
    form = forms.SearchForm()
    cart = forms.AddtoCartForm()
    productList = []
    searchedphrase = models.ProductModel.query.all()

    if form.validate_on_submit():
        result = request.form['searchbox']
        product = models.ProductModel.query.filter(models.ProductModel.productname == result).first()

    for i in searchedphrase:
        if (i.productname == result):
            productList.append(i.productname)

        return render_template('Search.html', result=result,form=form, searchedphrase=searchedphrase, product=product, productList=productList, cart=cart)

    return render_template('Search.html', form = form)

# Post product page (Mohammad)
@flaskObj.route('/PostProduct', methods=['GET','POST'])
def Product():
  #Saves whatever is inputed into the products databse
  form = forms.PostProductForm()
  if request.method == 'GET':
      return render_template('ListItemForSelling.html', form=form)
  if request.method == 'POST':
      product = models.ProductModel(productname=form.productname.data, productprice = form.productprice.data, productdescription = form.productdescription.data, productimage = form.productimage.data)
      db.session.add(product)
      db.session.commit()
      return redirect('/postProductSuccess')

# Item seller (Umesh)
@flaskObj.route('/seller')
def seller():
    return 'seller'

# Item rating (Umesh)
@flaskObj.route('/rating')
def rating():
    return render_template('RateItem.html')

