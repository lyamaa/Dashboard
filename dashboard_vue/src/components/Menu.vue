<template>
  <div class="column col is-2  rox" >
    <aside class="menu is-hidden-mobile">
      <p class="menu-label">General</p>
      <ul class="menu-list">
        <li>
          <router-link to="/dashboard" active-class="active"
            >Dashboard</router-link
          >
        </li>
        <li v-if="user.canView('users')">
          <router-link to="/users" active-class="active">Users</router-link>
        </li>
        <li v-if="user.canView('roles')">
          <router-link to="/roles" active-class="active">Roles</router-link>
        </li>
        <li v-if="user.canView('products')">
          <router-link to="/products" active-class="active"
            >Products</router-link
          >
        </li>
        <li v-if="user.canView('orders')">

          <router-link to="/orders" active-class="active">Orders</router-link>
        </li>
      </ul>
    </aside>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
export default {
  name: "Menu",
  setup() {
    const store = useStore();
    const user = computed(() => store.state.User.user);

    return {
      user,
    };
  },
};
</script>

<style src="../_main.scss" lang="scss">


</style>