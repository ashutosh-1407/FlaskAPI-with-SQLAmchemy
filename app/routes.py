from flask import request
from flask.wrappers import Response
from models import Product, User, Review

def configure_routes(app, db):
    @app.route('/')
    def index():
        return 'Flask API + SQLAlchemy + postgresql'

    @app.route('/review/<product_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def search_review(product_id):
        response = []
        json_response = {}
        if request.method in ('GET'):
            outputs = Review.query.filter_by(product_id=product_id)
            for output in outputs:
                response.append({'User ID': output.user_id,
                                'Product ID': product_id,
                                'Review': output.review,
                                'Rating': output.rating})
            json_response['results'] = response
        if request.method == 'POST':
            u_id = request.form.get('userid')
            review = request.form.get('review', 'This is the default review')
            rating = request.form.get('rating', 0.0)
            output = Review.query.filter_by(product_id=product_id, user_id=u_id).first()
            if output:
                output.review = review
                output.rating = rating
                db.session.commit()
                json_response['result'] = 'success: record updated'
            else:
                review_to_insert = Review(id=str(u_id)+str(product_id), review=review, rating=rating, user_id=u_id, product_id=product_id)
                db.session.add(review_to_insert)
                db.session.commit()
                json_response['result'] = 'success: record inserted'
        if request.method == 'DELETE':
            output = Review.query.filter_by(product_id=product_id, user_id=request.form.get('userid')).first()
            if output:
                db.session.delete(output)
                db.session.commit()
                json_response['result'] = 'success: record deleted'
            else:
                json_response['result'] = 'failure: record doesn"t exist'
        if request.method == 'PUT':
            u_id = request.form.get('userid')
            review = request.form.get('review', 'This is the default review')
            rating = request.form.get('rating', 0.0)
            check_insert = Review.query.filter_by(product_id=product_id, user_id=u_id).first()
            if check_insert:
                json_response['result'] = 'failure: record already exist'
            else:
                review_to_insert = Review(id=str(u_id)+str(product_id), review=review, rating=rating, user_id=u_id, product_id=product_id)
                db.session.add(review_to_insert)
                db.session.commit()
                json_response['result'] = 'success: record inserted'

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
