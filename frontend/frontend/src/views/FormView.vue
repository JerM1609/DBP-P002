<template>
  <section>
    <h1>{{ slug }}</h1>
    <fieldset v-if="datas">
      <form v-for="data in datas" :key="data.id">
        <div class="sep">
          <label :for="data.id">{{ data.name }}</label>
          <textarea
            :id="data.id"
            :type="data.type"
            v-if="data.required == true && data.class == 'textarea'"
            required
          />
          <textarea
            :id="data.id"
            :type="data.type"
            v-else-if="data.class == 'textarea'"
            required
          />
          <input
            :id="data.id"
            :type="data.type"
            v-if="data.required == true && data.class == 'input'"
            required
          />
          <input
            :id="data.id"
            :type="data.type"
            v-else-if="data.class == 'input'"
          />
        </div>
      </form>
    </fieldset>
    <fieldset v-if="Id">
      <form v-for="data in datos" :key="data.id">
        <div v-if="data.completed" class="sep">
          <p>{{ data.name }}</p>
          <p>{{ data.info }}</p>
        </div>
        <div v-else class="sep">
          <label :for="data.id">{{ data.name }}</label>
          <textarea
            :id="data.id"
            :type="data.type"
            v-if="data.required == true && data.class == 'textarea'"
            required
          />
          <textarea
            :id="data.id"
            :type="data.type"
            v-else-if="data.class == 'textarea'"
            required
          />
          <input
            :id="data.id"
            :type="data.type"
            v-if="data.required == true && data.class == 'input'"
            required
          />
          <input
            :id="data.id"
            :type="data.type"
            v-else-if="data.class == 'input'"
          />
        </div>
      </form>
    </fieldset>
  </section>
</template>
<script>
export default {
  props: ["slug", "Id", "datas"],
};
</script>
<style scoped>
.sep{
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    font-size: larger;
    margin-top: 3%;
    margin-bottom: 3%;
    padding: 5px 10px 5px 10px;
}
</style>