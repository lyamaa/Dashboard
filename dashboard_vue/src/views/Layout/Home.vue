<template>
  <div>
    <Navbar />
    <div class="container">
      <div class="columns">
        <Menu />

        <router-view  v-if="!loggedIn"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { onMounted, ref } from "vue";
import { defineComponent } from "vue";
import Menu from "../../components/Menu.vue";
import Navbar from "../../components/Navbar.vue";
import Dashboard from "../../components/Dashboard.vue";

import axios from "axios";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { User } from "../../classes/user";
import {authComputed} from "../../store/helper"

export default defineComponent({
  name: "Layout",
  computed: {
    ...authComputed
  },
  components: {
    Navbar,
    Menu,
    Dashboard,
  },
  setup() {
    const router = useRouter();
    const user = ref(null);
    const store = useStore();
    onMounted(async () => {
      try {
        const res = await axios.get("user");
        const u : User = res.data.data
        store.dispatch("User/setUser", new User(
          u.id,
          u.username,
          u.email,
          u.role,
          u.permissions
        ));
        user.value = res.data.data;
        console.log(res);
      } catch (err) {
        await router.push("/login");
      }
    });

    return {
      user,
    };
  },
});
</script>

<style src="../../_main.scss" lang="scss">
</style>
