from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"TASK {self.id}"

with app.app_context():
    db.create_all()

#homepage
@app.route("/",methods=["POST","GET"])
def index():
    
    if request.method == 'POST':
        curr_task = request.form['content']
        new_task = Task(content=curr_task)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        
        except Exception as e:
            print(f"Error{e}")
            return f'error {eval}'
    else:
        tasks = Task.query.order_by(Task.created).all()
        return render_template('index.html',tasks=tasks)

#delete
@app.route('/delete/<int:id>')
def delete(id:int):
    del_task = Task.query.get_or_404(id)
    try:
        db.session.delete(del_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"Error{e}")
        return f'error {eval}'
    
#edit
@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id:int):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"Error{e}")
            return f'error {eval}'
    else:
        return render_template('edit.html',task=task)
    



if __name__ == "__main__":
    app.run(debug=True)
