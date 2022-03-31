from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import cast, type_coerce, String
from sqlalchemy.dialects.postgresql import JSON
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@postgres:5432/testdb'
db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)

db.create_all()

@app.route('/api/test_db')
def test_db():
    # dbtest = Card.query.all()
    # for i in dbtest:
    #     dbjson = json.loads(i.data)
    #     for x in dbjson['model_details']['citations']:
    #         if x['citation'] == 'SVM':
    #             print(dbjson['model_details'])
            # if dbjson['model_details']['citations'][x]['citation'] == 'SVM':
            #     print(dbjson['model_details'])
        # print(dbjson['model_details']['citations'][0]['citation'])
    # dbjson = json.loads(dbtest)
    # print(dbtest)
    dbtest = None
    dbtest = [json.loads(i.data) for i in Card.query.all()]
    # for i in dbtest:
    #     dbjson = json.loads(i.data)
    return jsonify(dbtest)

def fill_db():
    check = Card.query.first()
    if check is not None:
        print('Database already populated')
        return
    with open('/app/model_cards_json/Davidson.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Waseem.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Tulkens.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Koeffer.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Niemann.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Jorgensen.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Badjatiya.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Gamback.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    with open('/app/model_cards_json/Zhang.json', 'r') as f:
        json_file = f.read()
    dat = Card(data = json_file)
    db.session.add(dat)
    db.session.commit()
    print('Database populated!')
    
fill_db()

@app.route('/api/test', methods=['POST'])
def on_Search():
    return 'Hallo Welt!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')