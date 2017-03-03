from wtforms import Form
from wtforms.fields import SelectField, StringField, BooleaField, SubmitField,\
                           DecimalField

class Infos(Form):
    veiculo_tipo = SelectField("como você se locomove?", 
                   choices=[(i,i) for i in ["carro", "onibus", "moto",
                   "bicicleta"]])
    veiculo_distancia = DecimalField("quantos km você percorre diariamente?")

