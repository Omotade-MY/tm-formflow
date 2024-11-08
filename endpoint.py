from flask import Flask, request 
from sqlalchemy import create_engine
import pandas as pd
import os
import io
import pickle
from datetime import datetime
from github import Github
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
username = os.environ['GITHUB_USERNAME']
token = os.environ['GITHUB_TOKEN']
g = Github(username, token)

GITHUB_REPO = "tm-formflow"

repo = g.get_user().get_repo(GITHUB_REPO)

app = Flask(__name__)
@app.route('/submit_form', methods=['POST'])
def submit_form():
    query = request.args
    first_name = query.get('first_name')
    last_name = query.get('last_name')
    data = {
        'first_name' : first_name,
        'last_name' : last_name
    }
    # dbname='your_dbname'
    # user='your_username'
    # password='your_password'
    # host='your_host'
    # port='your_port' 
    # conn_str = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"  
    # engine =  create_engine(conn_str)
    
    #conn = engine.connect()
    print(data)

    bytes_content = io.BytesIO()
    now = datetime.now().strftime("%y_%m_%d_%H_%M")
    try:
        print("HEEEEREREE")
        content = pd.DataFrame.from_dict([data])
        content.to_csv(bytes_content, index=False)
    # Upload to github
        git_file = f'data-{now}.csv'
        repo.create_file(git_file, "committing files", bytes_content.getvalue(), branch="exp")
    except:
        git_file = f'dump{now}.pkl'
        pickle.dump(data, bytes_content)

        repo.create_file(git_file, "committing files", bytes_content.getvalue(), branch="exp")
    print(git_file + ' CREATED')

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
    host = '0.0.0.0'
    # Use the environment variable 'PORT', defaulting to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host=host, port=port, debug=True)
