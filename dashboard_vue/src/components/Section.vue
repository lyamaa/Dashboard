<template>
  <section class="hero is-info welcome is-small">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          Hello, Mr/Mrs. <strong><router-link to="/profile">{{ user.username }}</router-link></strong>
        </h1>
        <h2 class="subtitle">Welcome to dashboard!</h2>
      </div>
    </div>
  </section>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
export default {
  name: "Section",
   
  setup() {
    const store = useStore()
    const user = computed(() => store.state.User.user)


    return{
      user
    }
  }
  
};
</script>