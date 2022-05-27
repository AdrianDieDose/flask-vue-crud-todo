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
            <tr v-for="(todo, index) in todo" :key="index">
              <td>{{ todo.task }}</td>
              <td>{{ todo.author }}</td>
              <td>
                <span v-if="todo.done">Yes</span>
                <span v-else>No</span>
              </td>
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
import axios from 'axios';

export default {
  name: 'ToDo',
  data() {
    return {
      todo: [],
    };
  },
  methods: {
    getTodo() {
      const path = 'http://localhost:5000/todo';
      axios
        .get(path)
        .then((res) => {
          this.todo = res.data.todo;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTodo();
  },
};
</script>

<style scoped>
.container {
  padding-left: 0;
}
</style>
