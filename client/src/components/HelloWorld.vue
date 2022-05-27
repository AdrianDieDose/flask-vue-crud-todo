<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <img v-for="index in 20" :key="index" :src="url + randomRes()" alt="" />
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to my page!',
      url: 'https://placekitten.com/g/',
    };
  },
  methods: {
    randomRes() {
      const max = 400;
      const min = 50;
      return `${String(Math.floor(Math.random() * (max - min + 1) + min))}/${String(
        Math.floor(Math.random() * (max - min + 1) + min),
      )}`;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0;
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
img {
  margin: 3%;
  border-radius: 50%;
}
</style>
