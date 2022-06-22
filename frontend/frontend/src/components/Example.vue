<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Example",
  data() {
    return {
      msg: "coming soon",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/example-endpoint";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data["msg"];
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
