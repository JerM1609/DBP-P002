<template>
  <section>
    <div class="cuerpo">
      <div class="head">
        <div class="titulo-fecha">
          <header class="titulo">{{ post.titulo }}</header>
          <button type="button" class="btn btn-day">
            {{ post.fecha.date() }}
          </button>
        </div>
        <div class="Line">
          <div>
            <a href="../../dashboard"
              ><button type="button" class="btn btn-label">Blog</button></a
            >
            <button type="button" class="btn btn-label">Like</button>
            <button type="button" class="btn btn-label2">
              {{ rTime }} min read
            </button>
            <button type="button" class="btn btn-label2">
              by {{ post.autor.username }}
            </button>
          </div>
        </div>
      </div>
      <h2>{{ post.subtitulo }}</h2>
      <div class="contenido">
        <img
          src="{{ url_for('static', filename= '/img/portada/' + ph_photo)  }}"
          alt=""
          height="100%"
        />
      </div>
      <div class="final">
        {{ post.contenido }}
      </div>
    </div>
  </section>
</template>
<script></script>
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
.btn-label2,
.btn-day {
  font-size: 0.8rem;
}
.btn-label2:focus,
.btn-day:focus {
  box-shadow: none;
}
.btn-label {
  color: #212529;
  font-size: 0.8rem !important;
  background-color: #e9ecef;
  border-color: #e9ecef;
}
.btn-label:hover {
  color: #212529;
  background-color: #b5c4d3;
  border-color: #a7b5c2;
}

.btn-label:focus {
  box-shadow: 0 0 0 0.2rem #b5c4d3;
}

.btn-label:disabled {
  color: #212529;
  background-color: #e9ecef;
  border-color: #e9ecef;
}
.btn-outline-primary {
  color: #007bff;
  border-color: #007bff;
}
.btn-outline-primary:hover {
  color: #212529;
  background-color: #007bff;
  border-color: #007bff;
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
.head {
  width: 100%;
}
.Line {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
}
.titulo-fecha {
  display: grid;
  grid-template-columns: 10fr 1fr;
}
.titulo {
  grid-column-start: 1;
}
.btn-day {
  background-color: #212529;
  color: #fff;
  border: 2px solid #212529;
  grid-column-start: 2;
}
.btn-day:hover {
  color: #fff;
}
.contenido {
  width: 100%;

  justify-content: center;
  display: flex;
}

.texto {
  padding-left: 3%;
  padding-right: 3%;
  padding-top: 1%;
}
.btn-icon {
  background-color: #e9ecef;
  border-radius: 0px;
  width: 30px;
  height: 30px;
  padding: 0px;
  margin-left: 0.5%;
  margin-right: 0.5%;
}
.buttons {
  text-align: right;
}
.head {
  height: 20%;
}
.contenido {
  height: 40%;
}
.final {
  margin-top: 2%;
  height: 40%;
  width: 100%;
  background-color: #e9ecef;
  overflow-wrap: break-word;
}
.head {
  font-size: 37px;
}
</style>
