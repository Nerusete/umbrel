import os, sqlite3
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

BASE="/app/data"
UPLOADS=os.path.join(BASE,"uploads")
DB=os.path.join(BASE,"coleccion.db")
os.makedirs(UPLOADS, exist_ok=True)

app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=10*1024*1024

def db():
    c=sqlite3.connect(DB)
    c.row_factory=sqlite3.Row
    return c

def init():
    c=db()
    c.execute("""CREATE TABLE IF NOT EXISTS items(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      tipo TEXT NOT NULL,
      pais TEXT, valor TEXT, anio TEXT, ceca TEXT,
      material TEXT, conservacion TEXT, precio_compra REAL,
      valor_actual REAL, cantidad INTEGER DEFAULT 1,
      notas TEXT, anverso TEXT, reverso TEXT,
      creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    c.commit(); c.close()

@app.route("/")
def index():
    q=request.args.get("q","").strip()
    tipo=request.args.get("tipo","")
    sql="SELECT * FROM items WHERE 1=1"; args=[]
    if q:
        sql+=" AND (pais LIKE ? OR valor LIKE ? OR anio LIKE ? OR ceca LIKE ? OR notas LIKE ?)"
        args += [f"%{q}%"]*5
    if tipo:
        sql+=" AND tipo=?"; args.append(tipo)
    sql+=" ORDER BY creado DESC"
    c=db(); items=c.execute(sql,args).fetchall()
    stats=c.execute("SELECT COUNT(*) n, COALESCE(SUM(cantidad),0) unidades, COALESCE(SUM(valor_actual*cantidad),0) total FROM items").fetchone()
    c.close()
    return render_template("index.html",items=items,stats=stats,q=q,tipo=tipo)

@app.route("/nuevo",methods=["GET","POST"])
def nuevo():
    if request.method=="POST":
        f=request.files
        def save(name):
            x=f.get(name)
            if not x or not x.filename: return None
            safe=os.path.basename(x.filename).replace(" ","_")
            dest=os.path.join(UPLOADS,safe)
            i=1
            base,ext=os.path.splitext(safe)
            while os.path.exists(dest):
                dest=os.path.join(UPLOADS,f"{base}_{i}{ext}"); i+=1
            x.save(dest); return os.path.basename(dest)
        c=db()
        c.execute("""INSERT INTO items(tipo,pais,valor,anio,ceca,material,conservacion,precio_compra,valor_actual,cantidad,notas,anverso,reverso)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(
          request.form.get("tipo","Moneda"),request.form.get("pais"),request.form.get("valor"),
          request.form.get("anio"),request.form.get("ceca"),request.form.get("material"),
          request.form.get("conservacion"),request.form.get("precio_compra") or None,
          request.form.get("valor_actual") or None,request.form.get("cantidad") or 1,
          request.form.get("notas"),save("anverso"),save("reverso")))
        c.commit(); c.close()
        return redirect(url_for("index"))
    return render_template("nuevo.html")

@app.route("/item/<int:item_id>")
def detalle(item_id):
    c=db(); item=c.execute("SELECT * FROM items WHERE id=?",(item_id,)).fetchone(); c.close()
    if not item: return "No encontrado",404
    return render_template("detalle.html",item=item)

@app.route("/uploads/<path:name>")
def uploads(name): return send_from_directory(UPLOADS,name)

@app.route("/eliminar/<int:item_id>",methods=["POST"])
def eliminar(item_id):
    c=db(); item=c.execute("SELECT anverso,reverso FROM items WHERE id=?",(item_id,)).fetchone()
    if item:
        for n in (item["anverso"],item["reverso"]):
            if n:
                p=os.path.join(UPLOADS,n)
                if os.path.exists(p): os.remove(p)
        c.execute("DELETE FROM items WHERE id=?",(item_id,)); c.commit()
    c.close(); return redirect(url_for("index"))

init()
app.run(host="0.0.0.0",port=41100)
