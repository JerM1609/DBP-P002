<template>
  <div>
    <form @submit.prevent="onLogin">
      <label>Username :</label>
      <input type="username" v-model.trim="profile.username" required />

      <label>Password :</label>
      <input type="password" v-model.trim="profile.password" required />

      <div class="button">
        <button type="submit">Log in</button>
      </div>
    </form>

    <p>UsernameA: {{ profile.username }}</p>
    <p>Password: {{ profile.password }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      userData: Object(),
      profile: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
  },
  methods: {
    ...mapActions({
      loginUser: "auth/loginUser",
    }),
    async login() {
      await this.loginUser(this.user).then(() => {
        if (this.authUser.authenticated) {
          this.$router.push("/profile");
        } else {
          // Handle error
          this.user = {
            username: null,
            password: null,
          };
        }
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
