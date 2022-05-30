<template>
  <div>
    <b-alert variant="success" :show="showing">{{ message }}</b-alert>
  </div>
</template>

<script>
export default {
  props: ['message', 'showing'],
  data() {
    return {};
  },
};
</script>
