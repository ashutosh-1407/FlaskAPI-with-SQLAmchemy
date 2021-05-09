from app import db, Product, User, Review

def insert():
    user1 = User(name='ashutosh')
    db.session.add(user1)

    user2 = User(name='nitin')
    db.session.add(user2)

    user3 = User(name='abhishek')
    db.session.add(user3)

    user4 = User(name='sachin')
    db.session.add(user4)

    user5 = User(name='arnab')
    db.session.add(user5)

    product1 = Product(name='Laptop', description='Dell inspiron 15R')
    db.session.add(product1)

    product2 = Product(name='Mobile', description='iPhone SE 2020')
    db.session.add(product2)

    product3 = Product(name='Playstation', description='PS5')
    db.session.add(product3)

    product4 = Product(name='Guitar', description='Gibson guitar')
    db.session.add(product4)

    product5 = Product(name='Piano', description='58 keys Casio keyboard')
    db.session.add(product5)

    review1 = Review(review="Exellent quality", rating=5.0, user_id=8, product_id=9)
    db.session.add(review1)

    review2 = Review(review="Good quality", rating=3.5, user_id=9, product_id=9)
    db.session.add(review2)

    db.session.commit()