<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>To Do App</h1>
        <hr />
        <br /><br />
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Task</th>
              <th scope="col">From</th>
              <th scope="col">Done?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>foo</td>
              <td>bar</td>
              <td>foobar</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ToDo',
  data() {
    return {};
  },
};
</script>

<style scoped>
.container {
  padding-left: 0;
}
</style>
