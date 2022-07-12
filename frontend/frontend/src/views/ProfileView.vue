<template>
  <section>
    <div class="cuerpo">
      <div class="segmento izq">
        <div class="prof">
          <figure class="ContenedorFoto">
            <img
              class="imagen"
              src="../assets/logo.png"
              alt=""
              height="220px"
              width="220px"
            />
            <!--- --->
            <figcaption class="Nombre">
              <!--<h2>{{ user.username }}</h2>-->
              <!--{{ this.userData }}-->
            </figcaption>
          </figure>
          <div class="datos">
            <p>
              <!--{% if user.career is not none %}
            {{ user.career }}
            {% else %} - {% endif %}-->
              {{ datas }}
            </p>
            <p>
              <!--{% if user.institute is not none %}
            {{ user.institute }}
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
          <div class="botones">
            <!--<a href="/editar-perfil/"
            ><button type="button" class="btn btn-primary">
              Editar datos
            </button></a
          >-->
            <button type="button" class="btn btn-primary">Editar datos</button>
            <!--<a href="../logout"
            ><button type="button" class="btn btn-outline-primary">
              Logout
            </button>
          </a>-->
            <button
              type="button"
              class="btn btn-outline-primary"
              @click="logout"
            >
              Logout
            </button>
          </div>
        </div>
        <div class="links">
          <div class="interno">
            <p class="dataname"><strong>Website</strong></p>
            <p class="data">
              <!--{% if user.website is not none %}
            <a href="{{user.website}}">{{ user.website }}</a>
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno">
            <p class="dataname"><strong>GitHub</strong></p>
            <p class="data">
              <!--{% if user.github is not none %} {% set idGithub =
            user.github.replace("https://github.com/", "")%}
            <a href="https://github.com/{{idGithub}}" target="_blank">{{
              idGithub
            }}</a>
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno">
            <p class="dataname"><strong>Twitter</strong></p>
            <p class="data">
              <!--{% if user.twitter is not none %} {% set idTwitter =
            user.twitter.replace("https://twitter.com/", "")%}
            <a href="https://twitter.com/{{idTwitter}}" target="_blank">{{
              idTwitter
            }}</a>
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno">
            <p class="dataname"><strong>Instagram</strong></p>
            <p class="data">
              <!--{% if user.instagram is not none %} {% set idInstagram =
            user.instagram.replace("https://instagram.com/", "")%}
            <a href="https://instagram.com/{{idInstagram}}" target="_blank">{{
              idInstagram
            }}</a>
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno">
            <p class="dataname"><strong>Facebook</strong></p>
            <p class="data">
              <!--{% if user.facebook is not none %} {% set idFB =
            user.facebook.replace("https://facebook.com/", "")%}
            <a href="https://facebook.com/{{idFB}}" target="_blank">{{
              idFB
            }}</a>
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
        </div>
      </div>
      <div class="segmento der">
        <div class="dat">
          <div class="interno2">
            <p class="dataname"><strong>Username</strong></p>
            <p class="data2">
              <!--{{ user.username }}--->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno2">
            <p class="dataname"><strong>Email</strong></p>
            <p class="data2">
              <!--{{ user.email }}-->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno2">
            <p class="dataname"><strong>Country</strong></p>
            <p class="data2">
              <!--{% if user.country is not none %}
            {{ user.country }}
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
          <hr width="100%" size="2px" />
          <div class="interno2">
            <p class="dataname"><strong>Institute</strong></p>
            <p class="data2">
              <!--{% if user.institute is not none %}
            {{ user.institute }}
            {% else %} - {% endif %}-->
              a
            </p>
          </div>
        </div>

        <div class="cont">
          <div class="llevando">
            <div class="header">
              <h2>Cursos</h2>
            </div>
            <!--{% if courses|length > 0 %} {% for c in courses %}
          <div class="curso">
            <a href="/curso_post/{{c.id}}"
              ><p>{{ c.titulo }}</p></a
            >
          </div>
          {% endfor %}
          <div class="curso">
            <p><a href="#">Mas</a></p>
          </div>
          {% else %}-->
            <div class="curso">
              <p>Nothing for now</p>
            </div>
            <!--{% endif %}-->
          </div>
          <div class="asesor">
            <div class="header">
              <h2>Asesorar</h2>
            </div>
            <!--{% if my_courses|length > 0 %} {% for c in my_courses %}
          <div class="curso">
            <a href="/curso_post/{{c.id}}"
              ><p>{{ c.titulo }}</p></a
            >
          </div>
          {% endfor %}
          <div class="curso">
            <p><a href="#">Mas</a></p>
          </div>
          {% else %}-->
            <div class="curso">
              <p>Nothing for now</p>
            </div>
            <!--{% endif %}-->
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Profile",
  data() {
    return {
      datas: null,
    };
  },
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
  },
  created() {
    this.datas = JSON.parse(sessionStorage.getItem(this.idUser));
    console.log(typeof this.datas);
  },
  methods: {
    ...mapActions({
      logoutUser: "auth/logoutUser",
    }),
    async logout() {
      await this.logoutUser().then(() => {
        this.$router.push("/");
      });
    },
  },
  props: {
    idUser: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
a {
  color: #007bff;
  text-decoration: none;
  background-color: transparent;
}
a:hover {
  color: #0056b3;
  text-decoration: underline;
}
.btn {
  display: inline-block;
  font-weight: 400;
  color: #212529;
  text-align: center;
  vertical-align: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  background-color: transparent;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.btn:hover {
  color: #212529;
  text-decoration: none;
}

.btn:focus {
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}
.btn-primary {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}
.btn-primary:hover {
  color: #fff;
  background-color: #0069d9;
  border-color: #0062cc;
}

.btn-primary:focus {
  box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
}

.btn-primary:disabled {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}
.btn-outline-primary {
  color: #007bff;
  border-color: #007bff;
}
.btn-outline-primary:hover {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}
.btn-outline-primary:hover > a {
  color: #fff;
  text-decoration: none;
}
.btn-outline-primary:focus {
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.5);
}
nav {
  margin-left: 5%;
  margin-right: 5%;
}
.breadcrumb {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 0.05rem 1rem;
  margin-bottom: 1rem;
  list-style: none;
  background-color: #e9ecef;
  border-radius: 0.25rem;
}
.breadcrumb-item + .breadcrumb-item {
  padding-left: 0.5rem;
}
.breadcrumb-item + .breadcrumb-item::before {
  display: inline-block;
  padding-right: 0.5rem;
  color: #6c757d;
  content: "|";
}
.breadcrumb-item.active {
  color: #6c757d;
}
body {
  background-color: #c2c2fe;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
.cuerpo {
  margin: 2% 5% 2% 5%;
  display: flex;
  flex-wrap: wrap;
  height: 800px;
}

.segmento {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.izq {
  flex-direction: column;
  width: 34%;
  height: 100%;
  margin-right: 1%;
}
.prof {
  text-align: center;
  width: 100%;
  background-color: #ffffff;
  height: 59%;
  margin-bottom: 1%;
}
.ContenedorFoto {
  margin-bottom: 6%;
  height: 55%;
}
.imagen {
  border-radius: 50%;
  border: 2px solid #6c757d;
}
figcaption {
  height: 20%;
}
.datos {
  height: 20%;
}

.links {
  margin-top: 1%;
  width: 96%;
  height: 39%;
  display: flex;
  flex-wrap: wrap;
  padding-left: 2%;
  padding-right: 2%;
  background-color: #ffffff;
}
hr {
  margin: 0%;
  padding: 0%;
}
.interno {
  display: grid;
  grid-template-columns: 6fr 2fr;
  height: calc(20% - 8px);
  width: 100%;
}
.data {
  text-align: right;
  grid-column-start: 2;
}
.dataname {
  grid-column-start: 1;
}
.der {
  flex-direction: column;
  width: 64%;
  margin-left: 1%;
  height: 100%;
}
.interno2 {
  display: grid;
  grid-template-columns: 3fr 4fr;
  width: 100%;
}
.dat {
  padding-left: 2%;
  padding-right: 2%;
  background-color: #ffffff;
  display: flex;
  flex-wrap: wrap;
  width: 96%;
  height: 44%;
  margin-bottom: 1%;
}
.cont {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 54%;
  margin-top: 1%;
}
.data2 {
  text-align: left;
  grid-column-start: 2;
}
.llevando,
.asesor {
  background-color: #ffffff;
  height: 100%;
  padding-left: 2%;
  padding-right: 2%;
  width: 44%;
}
.llevando {
  margin-right: 2%;
}
.asesor {
  margin-left: 2%;
}
.curso {
  height: 9%;
}

.centrado {
  height: 100vh;
  margin: 0;
  position: relative;
}

.box {
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  height: 100%;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
}
.box-content:hover {
  filter: drop-shadow(0 0 1rem rgb(147, 26, 196));
}

.box-content {
  text-align: center;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  flex-direction: column;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  height: 60%;
  width: 30%;
  background: #333;
  color: #fff;
}
.centrado {
  position: relative;
}

.centrado:hover::before {
  opacity: 0.4;
}
</style>
