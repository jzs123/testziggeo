import os
import time
import urlparse
import tornado.options

os.environ['COOKIE_SECRET'] = os.environ.get("SECRET_TOKEN", "placeholder")
os.environ['MONGODB_URL'] = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/apptrack")
os.environ['DB_NAME'] = urlparse.urlsplit(os.environ['MONGODB_URL']).path.replace("/","")
os.environ['ZIGGEO_TOKEN'] = urlparse.urlsplit(os.environ.get("ZIGGEO_URL", "https://token:privatekey@srvapi.ziggeo.com")).username
os.environ['FILE_PICKER_KEY'] = os.environ.get("FILEPICKER_API_KEY", "placeholder")
os.environ["ADMINS"] = "adminname:adminpassword"



os.environ['BASE_URL'] = "localhost"
os.environ['PATH'] = "/app/bin:/app/vendor/nginx/sbin:/app/vendor/php/bin:/app/vendor/php/sbin:/usr/local/bin:/usr/bin:/bin"
os.environ['TZ'] = "US/Eastern"
os.environ['PROJECT_ROOT'] = os.path.abspath(os.path.join(os.path.dirname(__file__)))

os.environ['SITE_TITLE'] = "Sitio de Postulacion"
os.environ['APPLY_TITLE'] = "Postular"   
os.environ['STRING_BOTTOM'] = "Esta es una prueba de un sistema de postulacion"
os.environ['STRING_CONFIRMATION'] = "Su solicitud sera revisada pronto, nos pondremos en contacto con usted."
os.environ["STRING_WELCOME"] = "Gracias por postular a nuestra vacante"
os.environ["STRING_INTRO"] = "En esta primera seccion debe escribir referencias"

global_data = {
    "VIDEOS": [{
        "question": "¿Por que esta interesado en esta Posicion y como puede aportar en la posicion?",
        "limit": 90,
        "required": True
    },
    {
        "question": "¿Cuales es su principal fortalez y su principal debilidad?",
        "limit": 50,
        "required": True
    },
        {
        "question": "¿Cual es su experiencia relevante en el Cargo?",
        "limit": 120,
        "required": True
    }
    
    ],
    "FIELDS": [{
        "label": "Su Nombre",
        "name": "nombre",
        "type": "text",
        "placeholder": "",
        "required": True
    }, {
        "label": "Email",
        "name": "email",
        "type": "text",
        "placeholder": "",
        "required": True
    }, {
        "label": "Ubicacion",
        "name": "Ubicacion",
        "type": "text",
        "placeholder": "¿Cual es su residencia actual?",
        "required": True
    }, {
        "label": "Referencias",
        "name": "referencias",
        "type": "textarea",
        "placeholder": "Por favor ingrese referencias con nombre, cargo y empresa , telefono y/o correo de la referencia",
        "required": False
    }, {
        "label": "CV",
        "name": "cv",
        "type": "file",
        "placeholder": "Su CV (PDF, DOC, TXT)",
        "required": False
    }]
}


try:
  import settings_local_environ
  if settings_local_environ.global_data :
      global_data = settings_local_environ.global_data
except:
  pass

  
time.tzset()

def get(key):
  return os.environ.get(key.upper())
