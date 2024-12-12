from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

#needs filled out with current database info
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}
#post test
@app.route('/save-player-data', methods={'POST'})
def save_player_data():
    print("made it to flask")
    connection = None
    cursor = None
    try:
        #connect to database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        print("connected")

        data = request.get_json()
        id = data.get("id")
        name = data.get("name")
        randnum = data.get("randnum")


        # Insert data into the table
        insert_query = "INSERT INTO gdtest (id, name, randnum) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (id, name, randnum))

        # Commit the transaction
        connection.commit()

        # Return a success response
        return jsonify({"status": "Data added successfully"}), 201

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Failed to add to gdtest"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
#get test
@app.route('/get-data', methods=['GET'])
def get_data():
    connection = None
    cursor = None
    try:
        #connect to database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        #execute a query
        cursor.execute("select * from countries")
        results = cursor.fetchall()

        #return data as JSON
        return jsonify(results)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "Database connection failed"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#actual get/post funcs
@app.route('/get-cbtt-session-start-data', methods=['GET'])
def get_cbtt_session_start_data():
    connection = None
    cursor = None
    parid_in = request.args.get('id')
    try:
        #connect to database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.curso(dictionary=True)

        #organize and execute a query
        cursor.execute("select * from sessionstartdata where parid = " + parid_in + ";")
        results = cursor.fetchall()

        #return data as JSON
        return jsonify(results)

    except mysql.connector.Error as err:
        print(f"Effor: {err}")
        return jsonify({"error": "Database connection failed"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/post-cbtt-session-progress-update', methods=['POST'])
def post_cbtt_session_progress_update():
    connection = None
    cursor = None
    try:
        #connect to database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        data = request.get_json()
        id = data.get("parid")
        level = data.get("level")
        sessioncount = data.get("sessioncount")
        completedoflevel = data.get("completedoflevel")

        #insert session progress into CBTTprogress
        insert_query = "INSERT INTO cbttprogress (sessioncount, parid, currentlevel, completedoflevel, updated) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (sessioncount, id, level, completedoflevel, "default"))

        #commit the transaction
        connection.commit()

        #return a success response
        return jsonify({"status": "CBTT session progress data added successfully"}), 201

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "failed to add to CBTTprogress"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route("/post-cbtt-session-stats", methods=['POST'])
def post_cbtt_session_stats():
    connection = None
    cursor = None
    try:
        #connect to database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        data = request.get_json()
        id = data.get("parid")
        sessionnum = data.get("sessionnum")
        length = data.get("length")
        score = data.get("score")
        longest_sequence = data.get("longest_sequence")
        level = data.get("level")

        # insert session progress into CBTTsessions
        insert_query = "INSERT INTO cbttsessions (sessionnum, parid, sessionlength, correctcount, longestsequence, currentlevel, updated) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (sessionnum, id, length, score, longest_sequence, level, "default"))

        # commit the transaction
        connection.commit()

        # return a success response
        return jsonify({"status": "CBTT session stats data added successfully"}), 201

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "failed to add to CBTTprogress"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


@app.route("/post-cbtt-trials-stats", methods=['POST'])
def post_cbtt_trials_stats():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        data = request.get_json()
        #prepare values for bulk insertion
        values_list = []

        for trial in data:
            cursor.execute("SELECT id FROM sequencetypes where name = %s;", (trial['sequencetype']))
            result = cursor.fetchone()
            if result:
                stid = result[0]
            else:
                raise ValueError("sequence type id not found")

            trial_values = (trial['trialnum'], trial['sessionnum'], trial['parid'], stid, trial['length'], trial['score'], "default")
            values_list.append(trial_values)

        if values_list:
            insert_query = """
            INSERT INTO cbtttrials (trialnum, sessionnum, parid, stid, sequencelength, score, whencompleted)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.executemany(insert_query, values_list)
            connection.commit()


    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": "failed to add to CBTTtrials"}), 500


    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route('/get-cbtt-sequence-types', methods=['GET'])
def get_cbtt_session_start_data():
    connection = None
    cursor = None
    parid_in = request.args.get('id')
    try:
        #connect to database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.curso(dictionary=True)

        #organize and execute a query
        cursor.execute("select * from sessionstartdata where parid = " + parid_in + ";")
        results = cursor.fetchall()

        #return data as JSON
        return jsonify(results)

    except mysql.connector.Error as err:
        print(f"Effor: {err}")
        return jsonify({"error": "Database connection failed"}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
