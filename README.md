# **DBP-P002**

Red social que une estudiantes de todo el mundo en búsqueda de enriquecer su experiencia académica

## INTEGRANTES 🙋‍♂️

- Jeremy Matos Cangalaya [JerM1609]
- Marcos Ayala Pineda [Marcos-1001]
- Diego Guerra Chevarria [DiegoGCh]
- Luis Gutierrez [Luis-ntonio]

## REQUERIMIENTOS
```
node -v
npm -v
git --version
npm install -g @vue/cli
``` 

## MISIÓN

- Facilitar el contacto entre asesores y estudiantes, respecto a un curso.
- Brindar tutoriales y experiencias por medio de publicaciones
- Brindar cursos hechos por estudiantes para estudiantes.

## VISIÓN

Ser la plataforma virtual de comunicación interestudiantil por excelencia.

## LIBRERÍAS, FRAMEWORKS Y PLUGINS

- werkezug
- Flask
    - flask_login
    - flask_wtf
    - flask_mail
- VueJS

## DISEÑO CONCEPTUAL DE BASE DE DATOS

Se presenta a continuación los requerimientos de `<APP>`

- Un usuario se identifica a través de su e-mail. Además, cuenta con un nombre, username, contraseña, datos personales y de redes sociales.

- Un usuario, si es verificado puede crear y publicar un curso.

- Un curso se identifica con un id de curso, tiene también título, fecha de creación y una reseña. 

- Un usuario puede inscribirse a uno o más cursos, pero no puede inscribirse al curso que el mismo dicta.

- Un usuario puede realizar publicaciones, verlas e interactuar con ellas.

- Un post se identifica con su propio id y el de su creador. Tiene un título, subtítulo, contenido y fecha de creación.

## TASKS

- Diego
    - API
- Jeremy
    - consumo de API en Vue
- Luis
    - frontend
- Marcos
    - OAuth 

## AUTENTICACIÓN

## TESTING

## DESPLIEGUE

0. Set `.env` file in `backend/api/config` folder and upload credentials.
1. Restore venv
2. Launch **Flask API server** 
3. Restore Nodejs project in folder where `package.json` file exists.
4. Launch **Vue.js server**    
5. Enjoy it!

## REFERENCES

- [Full Stack Project with Vue.js and Flask](https://www.youtube.com/watch?v=lenV5aVOMp8)
