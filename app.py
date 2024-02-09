from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

db_params = {
    'host' :"db",
    'port': 5432,
    'dbname': 'deneme',
    'user': 'admin1',
    'password': 'admin'
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/enternew")
def enternew():
    return render_template("student.html")

@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    cur = None  # cur değişkenini tanımla
    msg = "hejka" 
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            zip = request.form['zip']

            with psycopg2.connect(**db_params) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (nm, addr, city, zip) VALUES (%s, %s, %s, %s)", (nm, addr, city, zip))
                con.commit()
                msg = "Record successfully added to the database"

        except Exception as e:
            print(e)
            con.rollback()
            msg = "Error in the INSERT: {}".format(str(e))
        finally:
            cur.close()
            return render_template('result.html', msg=msg)

def create_table():
    with psycopg2.connect(**db_params) as con:
        con.autocommit = True
        cur = con.cursor()
        
        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'students')")
        table_exists = cur.fetchone()[0]

        if not table_exists:
            cur.execute("""
                CREATE TABLE students (
                    id SERIAL PRIMARY KEY,
                    nm VARCHAR(100),
                    addr VARCHAR(255),
                    city VARCHAR(100),
                    zip VARCHAR(20)
                )
            """)
            print("Table 'students' created.")

@app.route('/list')
def list():

    create_table()

    with psycopg2.connect(**db_params) as con:
        con.autocommit = True
        cur = con.cursor()

        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
    print(rows)
    return render_template("list.html", rows=rows)


    return render_template("list.html", rows=rows)

 
@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        try:
            
            id = request.form['id']
      
            with psycopg2.connect(**db_params) as con:
                con.autocommit = True
                cur = con.cursor()
                cur.execute("SELECT * FROM students WHERE id = %s", (id,))

                rows = cur.fetchall()
        except Exception as e:
            print(e)
            id = None
        finally:
            cur.close()
 
            return render_template("edit.html", rows=rows)


@app.route("/editrec", methods=['POST', 'GET'])
def editrec():
 
    if request.method == 'POST':
        try:
      
            rowid = request.form['id']
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            zip = request.form['zip']

           
            with psycopg2.connect(**db_params) as con:
                con.autocommit = True
                cur = con.cursor()
                cur.execute("UPDATE students SET nm=%s, addr=%s, city=%s, zip=%s WHERE id=%s", (nm, addr, city, zip, rowid))

                con.commit()
                msg = "Record successfully edited in the database"
        except Exception as e:
            print(e)
            con.rollback()
            msg = "Error in the Edit: UPDATE students SET nm=%s, addr=%s, city=%s, zip=%s WHERE id=%s" % (nm, addr, city, zip, rowid)

        finally:
            if cur and not cur.closed:
                cur.close()
         
            return render_template('result.html', msg=msg)

# Route used to DELETE a specific record in the database    
@app.route("/delete", methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        try:
            
            rowid = request.form['id']
          
            with psycopg2.connect(**db_params) as con:
                con.autocommit = True
                cur = con.cursor()
                cur.execute("DELETE FROM students WHERE id=%s", (rowid,))

                con.commit()
                msg = "Record successfully deleted from the database"
        except Exception as e:
            print(e)
            con.rollback()
            msg = e

        finally:
            cur.close()
            
            return render_template('result.html', msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
