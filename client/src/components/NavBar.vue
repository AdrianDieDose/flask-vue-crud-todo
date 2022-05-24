<template>
  <div>
    <b-navbar id="nav" toggleable type="dark" variant="primary">
      <b-navbar-brand href="./">Flask + Vue</b-navbar-brand>

      <b-navbar-toggle target="navbar-toggle-collapse">
        <template #default="{ expanded }">
          <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
          <b-icon v-else icon="arrow-bar-down"></b-icon>
        </template>
      </b-navbar-toggle>

      <b-collapse id="navbar-toggle-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="/ToDo">ToDo</b-nav-item>
          <b-nav-item href="/Ping">Ping</b-nav-item>
          <b-nav-item href="#" disabled>Disabled</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
};
</script>
<style>
#nav {
  padding: 15px 10%;
}
</style>
