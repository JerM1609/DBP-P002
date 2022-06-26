<template>
  <div>
    <div class="datos">
      <p>{{ user.career }}</p>
      <p>{{ user.institute }}</p>
    </div>

    <div class="dat">
      <div class="interno2">
        <p class="dataname"><strong>Username</strong></p>
        <p class="data2">
          {{ user.username }}
        </p>
      </div>
      <hr width="100%" size="2px" />
      <div class="interno2">
        <p class="dataname"><strong>Email</strong></p>
        <p class="data2">
          {{ user.email }}
        </p>
      </div>
    </div>

    <div class="interno">
      <p class="dataname"><strong>Facebook</strong></p>
      <p class="data">
        <a href="#" target="_blank">{{ user.facebook }}</a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: {},
    };
  },
};
</script>
