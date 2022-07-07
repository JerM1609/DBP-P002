<template>
  <h1>{{ form.name }}</h1>
</template>
<script>
import form from "@/forms";

export default {
  name: "Forms",
  data() {
    return {
      form: this.$route.params.name,
    };
  },
  props: {
    name: {
      type: String,
      require: true,
    },
  },
  computed: {
    Form() {
      return form.form.find((t) => t.name === this.name);
    },
  },
};
</script>
