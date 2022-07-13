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
    - flask_jwt_extended (intento de uso)
- VueJS
- VueX

## DISEÑO CONCEPTUAL DE BASE DE DATOS

Se presenta a continuación los requerimientos de `<APP>`

- Un usuario se identifica a través de su e-mail. Además, cuenta con un nombre, username, contraseña, datos personales y de redes sociales, los cuales se muestran en su perfil.

- Un usuario, si es verificado puede crear y publicar un curso.

- Un curso se identifica con un id de curso, tiene también título, fecha de creación y una reseña. 

- Un usuario puede inscribirse a uno o más cursos, pero no puede inscribirse al curso que el mismo dicta.

- Un usuario puede realizar publicaciones, verlas e interactuar con ellas.

- Un post se identifica con su propio id y el de su creador. Tiene un título, subtítulo, contenido y fecha de creación.

## CONSIDERACIONES
- No puede existir más de 1 curso con el mismo nombre, entre usuarios.
    - Hash: `md5(user.id + curso.nombre)`
- Verificación: Curriculum + validación manual.

## TASKS

- Diego
    - API, Axios y su comunicacion con el backend
- Jeremy
    - API, Axios y su comunicacion con el backend
- Luis
    - Frontend completo (VueJS, VueX, SessionStorage)
- Marcos
    - API, UnitTesting 

## AUTENTICACIÓN

Desde un inicio, sabíamos que queríamos implementar un método de autenticación a nuestro proyecto, debido a que le daría un toque realista de lo que se implementa en la industria. Por esa razón, decidimos intentar implementar el OAuth; sin embargo, después de unos días nos empezó a tomar más tiempo de lo que pensamos por lo que decidimos cambiar a JSON Web Tokens (JWT), lo que nos resultó mucho más fácil y sencillo de entender a comparación del OAuth, en gran parte debido a la documentación de la librería de flask_jwt_extended. 

Una vez con todo seteado(los access tokens, los refresh tokens, los responses enviados en cada endpoint, y cada endpoint que lo necesite resguardado con el decorator @jwt_required(), configuración del CORS, etc.), empezamos a setear la comunicación de Axios con el backend. Después de investigar, vimos que para acceder a los endpoints de @jwt_required() debíamos enviar headers de tipo Authorization que contengan un token de seguridad (del JWT). Fue ahí donde tuvimos problemas con el paso de los headers por medio de Axios, a pesar de estar buscando diferentes maneras y formatos de pasar los headers no pudimos solucionarlo: al tratar de acceder al endpoint no se nos otorgaba acceso a pesar de enviarle el token.

Por eso, decidimos retirar los tokens del método JWT, y solo quedarnos con el id del user y sus datos en el sessionStorage de VueX, a lo largo de todos los endpoints. **Como prueba de nuestros intentos de arreglar los problemas, se puede ver en los commits como pasamos de agregar configuraciones para el OAuth y para los JWT.**

## TESTING

#Explicar tests mas importantes, que se lograron, que no se lograron

## DESPLIEGUE

0. Set `.env` file in `backend/api/config` folder and upload credentials.
1. Restore venv
2. Launch **Flask API server** 
3. Restore Nodejs project in folder where `package.json` file exists.
4. Launch **Vue.js server**    
5. Enjoy it!

## REFERENCES

- [Full Stack Project with Vue.js and Flask](https://www.youtube.com/watch?v=lenV5aVOMp8)
