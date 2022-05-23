<template>
  <div id="app">
    <nav-bar />
    <router-view id="route" />
  </div>
</template>
<script>
import NavBar from './components/NavBar.vue';

export default {
  components: {
    NavBar,
  },
};
</script>
<style>
#route {
  margin: 5% 10%;
}
</style>
