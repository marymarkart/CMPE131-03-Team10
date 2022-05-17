from flask_wtf import FlaskForm
from wtforms import FloatField,StringField, SubmitField, validators
from wtforms.validators import DataRequired

# Form class for posting a product
class PostProductForm(FlaskForm):
  productname= StringField('Product Name' ,validators= [DataRequired(), validators.Length(max=64)])
  productprice=  FloatField('Product Price' ,  [DataRequired()])
  productdescription= StringField('Product Description' ,validators= [DataRequired(),validators.Length(max=500)])
  productimage = StringField('Image Link',validators = [validators.Length(max=500)])
  submit = SubmitField('Post')
  home = SubmitField('Home')

# Form class for searching items in the database ( Mohammad )
class SearchForm(FlaskForm):
  search = SubmitField('Search')
  searchbox = StringField("searchbox",validators = [DataRequired()])

class CheckoutForm(FlaskForm):
  cardnumber= StringField("Card Number",validators= [DataRequired(), validators.Length(min=12,max=12)])
  expirationdate= StringField("Expiration Date",validators= [DataRequired(), validators.Length(min=5,max=5)])
  securitycode = StringField("Security Code",validators= [DataRequired(), validators.Length(min=3,max=3)])
  checkout = SubmitField('Place Order')

# Form class to add a product to the cart ( Mohammad )
class AddtoCartForm(FlaskForm):
   addtocart = SubmitField('Add to cart')
  
# Form class to manage Sign Up information ( Rafael )
class SignUpForm(FlaskForm):
  email = StringField('email' ,validators= [DataRequired(), validators.Length(max=64)])
  password = StringField('password' ,validators= [DataRequired(), validators.Length(max=64)])
  submit = SubmitField('Sign Up')

# Form class to manage Log In information ( Rafael )
class LoginForm(FlaskForm):
  email = StringField('email' ,validators= [DataRequired(), validators.Length(max=64)])
  password = StringField('password' ,validators= [DataRequired(), validators.Length(max=64)])
  submit = SubmitField('Log In')