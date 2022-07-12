<template>
  <section>
    <div v-if="slug === 'profile'">
      <form @submit.prevent="handleSubmit">
        <label>Country :</label>
        <input type="text" v-model="profile.country" />

        <label>Instituto :</label>
        <input type="text" v-model="profile.institute" />

        <label>Carrera :</label>
        <input type="text" v-model="profile.career" />

        <label>Website :</label>
        <input type="url" v-model="profile.website" />

        <label>GitHub :</label>
        <input type="url" v-model="profile.github" />

        <label>Twitter :</label>
        <input type="url" v-model="profile.twitter" />

        <label>Instagram :</label>
        <input type="url" v-model="profile.instagram" />

        <label>facebook :</label>
        <input type="url" v-model="profile.facebook" />

        <div class="button">
          <button @click="update" class="submit" type="submit">Edit</button>
        </div>
      </form>
    </div>
    <div v-if="slug === 'course'">
      <form @submit.prevent="handleSubmit">
        <!-- <label>Portada :</label>
        <input type="file" /> -->

        <label>Titulo :</label>
        <input type="text" v-model="course.titulo" />

        <label>Subtitulo :</label>
        <input type="text" v-model="course.subtitulo" />

        <label>Contenido :</label>
        <textarea v-model="course.contenido"></textarea>

        <div class="button">
          <button @click="createC" class="submit" type="submit">Create</button>
        </div>
      </form>
    </div>
    <div v-if="slug === 'post'">
      <form @submit.prevent="handleSubmit">
        <label>Portada :</label>
        <input type="file" />

        <label>Titulo :</label>
        <input type="text" v-model="post.titulo" />

        <label>Subtitulo :</label>
        <input type="text" v-model="post.subtitulo" />

        <label>Clase :</label>
        <input type="text" v-model="post.clase" />

        <label>Contenido :</label>
        <textarea v-model="post.contenido"></textarea>

        <div class="button">
          <button @click="createP" class="submit" type="submit">Create</button>
        </div>
      </form>
    </div>
  </section>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      profile: {
        country: null,
        website: null,
        institution: null,
        career: null,
        github: null,
        twitter: null,
        facebook: null,
        instagram: null,
        Id: this.Id,
      },
      course: {
        portada: null,
        titulo: null,
        subtitulo: null,
        contenido: null,
        Id: this.Id,
      },
      post: {
        wallpaper: null,
        titulo: null,
        subtitulo: null,
        clase: null,
        contenido: null,
        Id: this.Id,
      },
    };
  },
  props: ["slug", "Id", "datas"],
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
  },
  methods: {
    ...mapActions({
      updateUser: "auth/updateUser",
      createCourse: "auth/createCourse",
      createPost: "auth/createPost",
    }),
    async update() {
      console.log(this.profile.Id);
      await this.updateUser(this.profile).then(() => {
        console.log("a", this.authUser);
        if (this.authUser) {
          this.$router.push({
            name: "Profile",
            params: {
              idUser: this.authUser["username"],
            },
          });
        } else {
          // Handle error
          this.profile = {
            username: null,
            password: null,
          };
        }
      });
    },
    async createC() {
      await this.createCourse(this.course).then(() => {
        console.log("done");
        // console.log("a", this.authUser);
        if (this.authUser) {
          this.$router.push({
            name: "Course",
            params: {
              slug: "mycourse",
            },
          });
        } else {
          // Handle error
          this.profile = {
            username: null,
            password: null,
          };
        }
      });
    },
    async createP() {
      await this.createPost(this.post).then(() => {
        console.log("done");
      });
    },
  },
};
</script>
<style scoped>
form {
  max-width: 600px;
  margin: 30px auto;
  background: #fff;
  text-align: left;
  padding: 20px;
  border-radius: 10px;
}
label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  text-transform: uppercase;
}
input,
textarea,
select {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: bordre-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}
input[type="checkbox"] {
  display: inline-block;
  width: 16px;
  margin: 0 10px 0;
  position: relative;
  top: 2px;
}
.pill {
  display: inline-block;
  margin: 20px 10px 0 0;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  cursor: pointer;
  background: #eee;
}
button {
  background: rgb(7, 24, 7);
  border: 0;
  padding: 10px 20px;
  color: white;
  border-radius: 20px;
}
.submit {
  text-align: center;
}
.error {
  color: #ff0000;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
</style>
