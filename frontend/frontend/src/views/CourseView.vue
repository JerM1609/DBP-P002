<template>
  <section>
    <div>
      <h1 v-if="slug === 'mycourse'">My courses</h1>
      <h1 v-else-if="slug === 'course'">courses of the comunity</h1>
      <div v-if="slug === 'mycourse'" class="posts">
        <div class="publication">
          <div class="content">
            <h2><a href="#">as</a></h2>
            <p>
              Lorem ipsum dolor sit, amet consectetur adipisicing elit.
              Excepturi nemo impedit animi suscipit. Obcaecati asperiores atque
              perspiciatis culpa fugiat? Nulla porro rerum ducimus quisquam!
              Accusantium asperiores fugit quod explicabo nobis.
            </p>
          </div>
          <div class="edition">
            <button class="btn btn-primary" v-on:click="delete courses.id">
              Unsubscribe
            </button>
          </div>
        </div>
        <!--
      <div v-for="courses in datas" :key="courses.id" class="posts">
        <div class="publication">
          <div class="content">
            <router-link
              :to="{ name: 'Publication', params: { PostId: courses.id } }"
              >{{ courses.name }}</router-link
            >
            <p>{{ courses.brief }}</p>
          </div>
          <button class="btn btn-primary" v-on:click="delete(courses.id)">Unsubscribe</button>
        </div>
      </div>
      --></div>
      <div v-else-if="slug === 'course'" class="posts">
        <div class="publication">
          <div>
            <h2><a href="#">as</a></h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi
              similique quisquam necessitatibus quod quae ratione incidunt!
              Dolore dolor, beatae, tempora quis similique perferendis labore
              natus eum corrupti qui, nihil sunt.
            </p>
          </div>
        </div>
        <!--
      <div v-for="course in datas" :key="course.id" class="posts">
        <div class="publication">
          <router-link
            :to="{ name: 'Publication', params: { PostId: posts.id } }"
            >{{ posts.name }}</router-link
          >
          <p>{{ posts.brief }}</p>
        </div>
      </div>-->
      </div>
      <div v-else>
        <h2>Page not found</h2>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  props: ["slug", "datas"],
  //falta el fetch delete()
};
</script>
<style scoped>
.posts {
  display: flex;
  justify-content: center;
  width: 100%;
}
.publication {
  flex-shrink: 0;
  flex-direction: row;
  background-color: aliceblue;
  height: 120px;
  display: flex;
  padding: 1%;
  width: 80%;
  text-align: left;
  border-radius: 20px;
}
.edition {
  text-align: right;
}
.content {
  width: 97%;
}
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
</style>
