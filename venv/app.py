from flask import Flask, render_template
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

from project import db
    class item(db.Model):
     
    __tablename__ = "item"
 
    id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_description = db.Column(db.String, nullable=False)
 
    def __init__(self, title, description):
        self.recipe_title = title
        self.recipe_description = description
 
    def __repr__(self):
        return '<title {}'.format(self.name)



posts = [
    {
        'author': 'Herbet',
        'title': 'book',
        'content': 'first post',
        'date_posted': 'august 18, 2019'
    },
      {
        'author': 'Jane Doe',
        'title': 'book 2',
        'content': 'second post',
        'date_posted': 'august 20, 2019'
    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')


# creates a command prompt using python instead of flask run
if __name__ == '__main__':
    app.run(debug=True)    