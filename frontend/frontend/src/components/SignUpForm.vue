<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <label>Email :</label>
      <input type="email" v-model="email" required />
      <div v-if="emailError" class="error">{{ emailError }}</div>

      <label>Username :</label>
      <input type="username" v-model="username" required />

      <label>Password :</label>
      <input type="password" v-model="password" required />
      <div v-if="passwordError" class="error">{{ passwordError }}</div>

      <div>
        <input type="checkbox" v-model="terms" required />
        <label>Please accept terms and conditions</label>
      </div>

      <div class="button">
        <button @click="signUp" class="submit" type="submit">
          Sign up here
        </button>
      </div>
    </form>

    <p>Email: {{ email }}</p>
    <p>Username: {{ username }}</p>
    <p>Password: {{ password }}</p>
    <p>Terms : {{ terms }}</p>
    <p>Send : {{ send }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      username: "",
      password: "",
      terms: false,
      send: false,
      passwordError: "",
      emailError: "",
    };
  },
  methods: {
    handleSubmit() {
      // Validate password field length
      // this.passwordError =
      //   this.password.length > 6
      //     ? ""
      //     : "Password should be more than 6 characters long!";
      //   if (!this.passwordError) {
      //     console.log(this.email);
      //     console.log(this.password);
      //     console.log(this.terms);
      //   }
    },
    async signUp() {
      this.send = true;
      const path = "http://localhost:5000/user";

      let item = {
        email: this.email,
        username: this.username,
        password: this.password,
      };
      let form_data = new FormData();
      for (let key in item) {
        form_data.append(key, item[key]);
      }

      // const response = await fetch(path, {
      //   method: "POST",
      //   body: form_data,
      // });
      // const responseText = await response.text();
      // let responseJSON = JSON.parse(responseText);
      // if (responseJSON["code"] === 200) this.$router.push("/log-in");
      this.emailError = "";
      this.passwordError = "";

      fetch(path, {
        method: "POST",
        body: form_data,
      })
        .then(async (response) => {
          const responseText = await response.text();
          return JSON.parse(responseText);
        })
        .then((responseJSON) => {
          console.log(responseJSON);
          if (responseJSON["code"] === 200) {
            this.$router.push("/log-in");
          } else {
            this.email = "";
            this.username = "";
            this.password = "";
            this.emailError = "Email is already used";
          }
        })
        .catch((err) => console.log(err));
    },
  },
};

/**
 * https://dmitripavlutin.com/fetch-with-json/
 * https://stackoverflow.com/questions/22783108/convert-js-object-to-form-data
 * https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData
 * https://learningwithmanjeet.com/create-a-signup-form-with-vue-js/
 */
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
