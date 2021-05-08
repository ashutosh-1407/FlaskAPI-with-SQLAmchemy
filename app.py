from flask import Flask, json, request
from flask.wrappers import Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/MyDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description) -> None:
        super().__init__()
        self.name = name
        self.description = description 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

class Review(db.Model):
    __table_args__ = (
        db.UniqueConstraint('user_id', 'product_id', name='unique_user_product'),
    )
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, review, rating, user_id, product_id) -> None:
        super().__init__()
        self.review = review
        self.rating = rating
        self.user_id = user_id
        self.product_id = product_id

@app.route('/')
def index():
    return 'Flask API + SQLAlchemy + postgresql'

@app.route('/review/<product_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def search_review(product_id):
    response = []
    json_response = {}
    cnt = 1
    if request.method in ('GET'):
        outputs = Review.query.filter_by(product_id=product_id)
        for output in outputs:
            response.append({'User ID': output.user_id,
                            'Product ID': product_id,
                            'Review': output.review})
            cnt+=1
        json_response['results'] = response
    if request.method == 'POST':
        u_id = request.form.get('userid')
        review = request.form.get('review', 'This is the default review')
        rating = request.form.get('id', 0.0)
        output = Review.query.filter_by(product_id=product_id, user_id=u_id, rating=rating, review=review).first()
        if output:
            db.session.delete(output)
            db.session.commit()
            json_response['result'] = 'success'
        else:
            json_response['result'] = 'failure'
    if request.method == 'DELETE':
        print(request.form.get('userid'))
        output = Review.query.filter_by(product_id=product_id, user_id=request.form.get('user_id')).first()
        if output:
            db.session.delete(output)
            db.session.commit()
            json_response['result'] = 'success'
        else:
            json_response['result'] = 'failure'
    if request.method == 'PUT':
        u_id = request.form.get('userid')
        review = request.form.get('review', 'This is the default review')
        rating = request.form.get('id', 0.0)
        review_to_insert = Review(review=review, rating=rating, user_id=u_id, product_id=product_id)
        db.session.add(review_to_insert)
        db.session.commit()
        json_response['result'] = 'success'

    return json_response

@app.route('/product/<product_id>', methods=['GET'])
def search_product(product_id):
    json_response = {}
    outputs = Product.query.filter_by(id=product_id)
    for output in outputs:
        json_response['Product ID'] = product_id
        json_response['Product Name'] = output.name
        json_response['Product Description'] = output.description
    return json_response

@app.route('/user/<user_id>', methods=['GET'])
def search_user(user_id):
    json_response = {}
    outputs = User.query.filter_by(id=user_id)
    for output in outputs:
        json_response['User ID'] = user_id
        json_response['User Name'] = output.name
    return json_response

if __name__ == '__  main__':
    app.run()