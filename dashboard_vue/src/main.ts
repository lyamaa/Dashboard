import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import axios from "axios";

axios.defaults.baseURL = "https://superdash8848.herokuapp.com/api/";
axios.defaults.withCredentials = true;

createApp(App)
  .use(store)
  .use(router)
  .mount("#app");
