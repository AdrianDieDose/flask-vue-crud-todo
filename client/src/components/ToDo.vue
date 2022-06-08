<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>CRUD - To Do App</h1>
        <hr />
        <br /><br />
        <b-row>
          <alert class="col" id="alert" :message="message" :showing="showMessage"></alert>
          <button
            id="cancel-button"
            v-show="showMessage"
            type="button"
            icon="chevron-bar-up"
            class="btn btn-danger btn-sm w-1"
            @click="changeShow()"
          >
            x
          </button>
        </b-row>

        <button type="button" class="btn btn-success btn-sm" v-b-modal.todo-modal>Add Task</button>
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
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    v-b-modal.todo-update-modal
                    @click="editTodo(todo)"
                  >
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="onDeleteTask(todo)">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal ref="addToDoModal" id="todo-modal" title="Add a new ToDo" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-task-group" label="Task:" label-for="form-task-input">
          <b-form-input
            id="form-task-input"
            type="text"
            v-model="addToDoForm.task"
            required
            placeholder="Enter task"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group" label="Author:" label-for="form-author-input">
          <b-form-input
            id="form-author-input"
            type="text"
            v-model="addToDoForm.author"
            required
            placeholder="Enter author"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-done-group">
          <b-form-checkbox-group v-model="addToDoForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editTodoModal" id="todo-update-modal" title="Update" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group" label="Task:" label-for="form-task-edit-input">
          <b-form-input
            id="form-task-edit-input"
            type="text"
            v-model="editForm.task"
            required
            placeholder="Enter task"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-author-edit-group"
          label="Author:"
          label-for="form-author-edit-input"
        >
          <b-form-input
            id="form-author-edit-input"
            type="text"
            v-model="editForm.author"
            required
            placeholder="Enter author"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-done-edit-group">
          <b-form-checkbox-group v-model="editForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'ToDo',
  data() {
    return {
      todo: [],
      addToDoForm: {
        task: '',
        author: '',
        done: [],
      },
      message: '',
      showMessage: false,

      editForm: {
        id: '',
        task: '',
        author: '',
        done: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getToDo() {
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
    addToDo(payload) {
      const path = 'http://localhost:5000/todo';
      axios
        .post(path, payload)
        .then(() => {
          this.getToDo();
          this.message = 'Task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getToDo();
        });
    },

    initForm() {
      this.addToDoForm.task = '';
      this.addToDoForm.author = '';
      this.addToDoForm.done = [];
      this.editForm.id = '';
      this.editForm.task = '';
      this.editForm.author = '';
      this.editForm.done = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addToDoModal.hide();
      let done = false;
      if (this.addToDoForm.done[0]) {
        done = true;
      }
      const payload = {
        task: this.addToDoForm.task,
        author: this.addToDoForm.author,
        done, // property shorthand
      };
      this.addToDo(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addToDoModal.hide();
      this.initForm();
    },
    changeShow() {
      this.showMessage = false;
    },
    editTodo(todo) {
      this.editForm = todo;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      let done = false;
      if (this.editForm.done[0]) done = true;
      const payload = {
        task: this.editForm.task,
        author: this.editForm.author,
        done,
      };
      this.updateTodo(payload, this.editForm.id);
    },

    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      this.initForm();
      this.getTodo(); // why?
    },
    updateTodo(payload, todoID) {
      const path = `http://localhost:5000/todo/${todoID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getToDo();
          this.message = 'Task updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getToDo();
        });
    },
    removeTask(todoID) {
      const path = `http://localhost:5000/todo/${todoID}`;
      axios
        .delete(path)
        .then(() => {
          this.getToDo();
          this.message = 'Task removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getToDo();
        });
    },
    onDeleteTask(task) {
      this.removeTask(task.id);
    },
  },
  created() {
    this.getToDo();
  },
};
</script>

<style scoped>
.container {
  padding-left: 0;
}

#alert {
  z-index: 1;
  padding-right: 0;
}

#cancel-button {
  z-index: 99;
  height: 50px;

  padding: 0.75rem 1.25rem;
}
</style>
