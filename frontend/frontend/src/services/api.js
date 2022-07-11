import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5001",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  // // GET
  getUser() {
    return apiClient.get("/user");
  },

  getLogOut() {
    return apiClient.get("/logout");
  },
  // function getCursos() {
  //   return apiClient.get("/cursos");
  // }

  // function getPosts() {
  //   return apiClient.get("/posts");
  // }

  // // POST
  loginUser(user) {
    return apiClient.post("/login", user);
  },

  registerUser(user) {
    return apiClient.post("/sign-up", user);
  },

  // function postCursos(obj) {
  //   return apiClient.post("/cursos", obj);
  // }

  // function postPosts(obj) {
  //   return apiClient.post("/posts", obj);
  // }

  // PATCH

  // DELETE

  //      TEST
  // async function testPosts() {
  //   // postPosts({

  //   // })

  //   getPosts()
  //     .then((response) => {
  //       console.log(response["data"]);
  //     })
  //     .catch((err) => console.log("ERROR\n", err));
  // }

  // async function testCursos() {}

  // testPosts();
};
