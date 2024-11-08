from flask import Flask, request 
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json  
    # dbname='your_dbname'
    # user='your_username'
    # password='your_password'
    # host='your_host'
    # port='your_port' 
    # conn_str = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"  
    # engine =  create_engine(conn_str)
    
    #conn = engine.connect()
    print(data)
    df = pd.DataFrame.from_dict([data])

    #df.to_csv("data.csv")
    # cur.execute(
    #     "INSERT INTO your_table_name (column1, column2, ...) VALUES (%s, %s, ...)",
    #     (data['field1'], data['field2'], ...)
    # )
    # conn.commit()
    # cur.close()
    # conn.close()
    return 'Success', 200


if __name__ == '__main__':
    app.run(debug=True)
