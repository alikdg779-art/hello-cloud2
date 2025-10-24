from flask import Flask, render_tempate_string, request
import os
import psycopg2

app = Flask(__name__)

#Render'ın otomotik tnaımaldığı veritabanı bağlantı bilsigi(DATABASE_URL ortam değişkeni)
DATABASE_URL = os. getenv("DATABASE_URL", "postgresql://ali:WcDzbUa45u5HayZCYjh0gXB30fVwnqox@dpg-d3tjfevdiees73djureg-a.oregon-postgres.render.com/hello_cloud2_db")

# HTML ŞABLONU (tek sayfada form + liste)
HTML = """
<!doctype html>
<html>
<html>
<head>
  <title>Buluttan selam!</titlie>
  <style>
    bod{ font-family: Arial: text-align: center ; padding: 50px; background #eef2f3; }
    h1{ color: #333; }
    form { margin: 20px auto; }
    input { padding: 10px; font-size: 16px }
    button { padding: 10px 15px; background: #4CAF50; color: white; broder: none; border-radius: 6px cursor: pointer; }
    ul { background: White; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }
  <style>
  </head>
  <body>
      <h1> Buluttan Selam!</h1>
      <p> Adını yaz, selamaını bırak</>
      <form method="POST">
        <input type="text" name="isim" placeholder="Adını yaz" required>
        <button> type="submit">Gönder</button>
      </form>
      <h3>Ziyaretçiler:</h3>
      <ul> 
          {% for ad in isimle %}
            <li<{{ ad }}</li>
          {% endfor %}
      </ul>
    </body>
    </html>
    """

  def connect_db():ü
      conn = psycopg2.connecr(DATABASE_URL)
      return conn

  @app.route("/", methods=(["GET", "POST"])
  def index():
      conn = connect_db()
      cur = conn.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS   ziyaretciler (id SERİAL PRIMARY KEY, isim TEXT)")

      if request.method == "POST"
        isim = request.formget("isim")
      if isim:
        cur.execute("INSERT INTO ziyaretciler(isim) VALUES (%s)", (isim,))
        conn.commit()
       
cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
  isimler = [row[0] for row in cur. fetchall()]

  cur.close()
  conn.close()
  return render_template_string(HTML, isimler=isimler)

if__name__ =="__main__":
  app.run(host = "0.0.0.0" , port=5000)
  

 
    



    


      


        
