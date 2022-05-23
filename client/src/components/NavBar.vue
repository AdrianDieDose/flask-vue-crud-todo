<template>
  <div id="nav">
    <b-nav pills small>
      <b-nav-item class="item" active>Active</b-nav-item>
      <b-nav-item class="item">Link</b-nav-item>
      <b-nav-item class="item">Another Link</b-nav-item>
      <b-nav-item class="item" disabled>Disabled</b-nav-item>
    </b-nav>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
};
</script>
<style scoped>
#nav {
  padding: 20px 10%;
  background-color: white;
}
#nav-title {
  color: white;
  padding-left: 10px;
  height: 100%;
}

.item {
  color: white;
  background-color: rgb(108, 108, 233);
  margin: 1%;
  padding: 1%;
  border-radius: 5px;
}
</style>
