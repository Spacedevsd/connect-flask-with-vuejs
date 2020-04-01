Vue.component("task-form", {
  template: `
  <div>
    <div class="form-group">
      <input type="text" v-model="name" class="form-control" placeholder="Insert a task name">
    </div>
    
    <div class="form-group">
      <button @click="setTask" class="btn btn-block btn-info btn-lg">
        <span v-if="isLoading" >
          <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
          Saving...
        </span>
        <span v-else> Save </span>
      </button>
    </div>

    <div class="mt-5">
      <ul class="list-group list-group-flush">
        <li class="list-group-item" v-for="task in tasksList">
          <span class="float-left">#{ task.id }</span>
          <span class="float-right">#{ task.name }</span>
        </li>
      </ul> 
    </div>
  </div>
  `,
  data: function() {
    return {
      tasksList: [],
      name: "",
      isLoading: false
    };
  },
  async mounted() {
    this.tasksList = await this.getTasks();
  },
  methods: {
    async getTasks() {
      const response = await axios.get("/tasks/list");
      return response.data;
    },
    async setTask() {
      this.isLoading = true;
      const response = await axios.post("/tasks/insert", { name: this.name });
      this.tasksList.push({ id: response.data.id, name: response.data.name });
      this.name = "";
      this.isLoading = false;
    }
  }
});

new Vue({
  el: "#app"
});

// Você não sabe quanto tempo isso daqui vai durar...1m, 1h, 23h
// Berg (Brasil) => Microsoft (USA) => Servidor (USA) => Banco De Dados (Japao)
