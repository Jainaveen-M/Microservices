from flask import Flask, jsonify
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello():
    return "Hello This is Login service"

@app.route('/demo',methods=['GET'])
def demo():
    try:
        result = requests.get('http://172.19.0.3:5055/')
        return jsonify({"data":str(result.content)})
    except Exception as e:
        print(str(e))
        
@app.route('/getdb',methods=['GET'])
def getDb():
    try:
        db_session = scoped_session(session_maker)
        result = db_session.query(TEST).all()
        l = []
        for i in result:
            l.append({"id":i.id,"name":i.name})
        return jsonify({"status":"success","data":l})
    except Exception as e:
        print(str(e))

session_maker = None
engine = None

def init_db(
    db_str,
    pool_size=10,
    pool_recycle=3600,
    isolation_level="READ COMMITTED",
    convert_unicode=True,
):
    global session_maker, engine
    SQL_ALCHEMY_DATABASE_URI = db_str
    engine = create_engine(
        SQL_ALCHEMY_DATABASE_URI,
        pool_size=pool_size,
        pool_recycle=pool_recycle,
        isolation_level=isolation_level,
        convert_unicode=convert_unicode,
    )
    session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

class TEST(Base):
    __tablename__ = 'test'
    __table_args__ = {'schema': 'demo'}

    id = Column(INTEGER, primary_key=True)
    name = Column(String(45))
    
    
if __name__ == "__main__":
    db_str = "mysql+pymysql://root:root@172.19.0.4:3306/demo"
    init_db(db_str=db_str)
    app.run(host="0.0.0.0",port="5056",debug=True)

    
    