from flask import Flask,render_template,request,flash,Response,g
from flask_wtf.csrf import CSRFProtect
from flask import redirect
import forms
from models import db


from config import DevelopmentConfig
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()



@app.route("/index",methods=["GET","POST"])
def index():
    alum_form=forms.UsarForm2(request.form)
    if request.method=='POST':
         alum=Alumnos(nombre=alum_form.nombre.data,
                      apaterno=alum_form.apaterno.data,
                      email=alum_form.email.data)
         #para mandar los datos seran por seciones 
         db.session.add(alum)
         db.session.commit()

    return render_template("index.html",form=alum_form)


@app.route("/ABC_Completo",methods=["GET","POST"])
def ABC_Completo():
    alum_form=forms.UsarForm2(request.form)
    #para hacer una consulta
    alumno=Alumnos.query.all()
    return render_template("ABC_Completo.html",alumnos=alumno)

@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
    alum_form=forms.UsarForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #aqui pasamos la condicion que queremos buscar 
        alumno1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum_form.id.data=request.args.get('id')
        alum_form.nombre.data=alumno1.nombre
        alum_form.apaterno.data=alumno1.apaterno
        alum_form.email.data=alumno1.email
    if request.method=='POST':
        id=alum_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template('eliminar.html',form=alum_form)

@app.route("/modificar",methods=["GET","POST"])
def modificar():
    alum_form=forms.UsarForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #aqui pasamos la condicion que queremos buscar 
        alumno1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum_form.id.data=request.args.get('id')
        alum_form.nombre.data=alumno1.nombre
        alum_form.apaterno.data=alumno1.apaterno
        alum_form.email.data=alumno1.email
    if request.method=='POST':
        id=alum_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=alum_form.nombre.data
        alum1.apaterno=alum_form.apaterno.data
        alum1.email=alum_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template('modificar.html',form=alum_form)

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    
    alum_form=forms.UsarForm(request.form)
    nom=''
    apa=''
    ama=''
    mensaje=''
    #para validar que los campos no tengan un error se agrega el validate 
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("Apellido Paterno: {}".format(apa))
        print("Apellido Materno: {}".format(ama))
    return render_template("alumnos.html",form=alum_form,nom=nom,apa=apa,ama=ama)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



#especificar el metodo que va a arrancar la aplicacion 
if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()    


    