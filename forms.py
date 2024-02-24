from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField
from wtforms import validators


class UsarForm(Form):
    #para validar se genra una lista de validaciones, para que sea un dato requerido
    
    nombre=StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa nombre valido')
    ])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa nombre valido')
    ])
    amaterno=StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa nombre valido')
    ])
    edad=IntegerField('edad',[
        validators.DataRequired(message='el campo es requerido'),
        validators.number_range(min=1,max=20,message='valor no valido')
    ])
    correo=EmailField('email',[validators.Email(message='Ingresa un correo valido')])