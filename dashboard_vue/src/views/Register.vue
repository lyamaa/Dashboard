<template>
  
    <div class="columns is-multiline reg">
      <div class="column box is-8 is-offset-2 register">
        <div class="columns">
          <div class="column left">
            <h1 class="title is-1">DJ DASH</h1>
            <h2 class="subtitle colored is-2">नम्स्ते दाजु</h2>
            
             <figure class="image is-128X128 mt-5">
              <img :src="mySvg" />
            </figure>
            
          </div>
          <div class="column right has-text-centered">
            <h1 class="title is-4">Sign up today</h1>
            <p class="description">
              Welcome to our site....
            </p>
            
            <form @submit.prevent="submit">
              <div class="field">
                <div class="control">
                  <input
                    class="input is-medium"
                    type="text"
                    placeholder="Username"
                    required
                    v-model="username"
                  />
                </div>
              </div>

              <div class="field">
                <div class="control">
                  <input
                    class="input is-medium"
                    type="email"
                    placeholder="Email"
                    required
                    v-model="email"
                  />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <input
                    class="input is-medium"
                    type="password"
                    placeholder="Password"
                    required
                    v-model="password"
                  />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <input
                    class="input is-medium"
                    type="password"
                    placeholder="Confirm Password"
                    required
                    v-model="password_confirm"
                  />
                </div>
              </div>
              <button class="button is-block is-primary is-fullwidth is-medium">
                Submit
              </button>
              <br />
               <p class="subtitle">Have an account? <router-link to="/login">Sign In</router-link> &nbsp;·&nbsp;</p>
               <small> <p v-if="error" class="help is-danger box">{{error}}</p></small>
            
            </form>
          </div>
        </div>
      </div>
      <div class="column is-8 is-offset-2">
        <br />
        <nav class="level">
          <div class="level-left">
            <div class="level-item">
              <span class="icon">
                <i class="fab fa-twitter"></i>
              </span>
              &emsp;
              <span class="icon">
                <i class="fab fa-facebook"></i>
              </span>
              &emsp;
              <span class="icon">
                <i class="fab fa-instagram"></i>
              </span>
              &emsp;
              <span class="icon">
                <i class="fab fa-github"></i>
              </span>
              &emsp;
              <span class="icon">
                <i class="fas fa-envelope"></i>
              </span>
            </div>
          </div>
          <div class="level-right">
            <small class="level-item" style="color: white">
              &copy; Dj Dash. All Rights Reserved.
            </small>
          </div>
        </nav>
      </div>
    </div>
 
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { ref } from "vue";

import axios from "axios";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "Register",

  setup() {
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const password_confirm = ref("");
    const router = useRouter();
    const error = ref(null)

    const submit = async () => {
      const res = await axios.post("register", {
        username: username.value,
        email: email.value,
        password: password.value,
        password_confirm: password_confirm.value,
      }).then(async () => {
         await router.push("/login");
      })
      .catch(err => {
          console.log(err)
          error.value = err.response.data.detail
          error.value = err.response.data.username
        })
      console.log(res);

     
    };

    return {
      username,
      email,
      password,
      password_confirm,
      submit,
      error,
      mySvg: require('../assets/img/profile.svg'),
    };
  },
});
</script>



<style src="../assets/scss/register.scss" lang="scss">
</style>