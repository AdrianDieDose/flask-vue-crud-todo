<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <img src="https://placekitten.com/g/500/500" alt="" />
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to my page!',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
  margin: 5px;
}
</style>
