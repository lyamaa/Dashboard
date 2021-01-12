<template>
  <div class="column is-9">
    <div class="columns dash">
      <div class="column is-6">
        <!-- here -->
        <div class="card events-card">
          <header class="card-header">
            <p class="card-header-title">Profile</p>
          </header>

          <div class="content">
            <form class="mt-5 box" @submit.prevent="submitProfile">
              <div class="field">
                <label class="label">Username</label>
                <div class="control">
                  <input
                    class="input is-medium"
                    name="username"
                    type="text"
                    placeholder="Username"
                    required
                    v-model="username"
                  />
                </div>
              </div>

              <div class="field">
                <label class="label">Email</label>
                <div class="control">
                  <input
                    class="input is-medium"
                    type="email"
                    name="email"
                    placeholder="Email"
                    required
                    v-model="email"
                  />
                </div>
              </div>
              <button class="button is-info">Submit</button>
            </form>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <div class="card events-card">
          <header class="card-header">
            <p class="card-header-title">Password Change</p>
          
          </header>

          <div class="content">
            <form class="mt-5 box" @submit.prevent="submitPassword">
              <div class="field">
                <label class="label">Password</label>
                <div class="control">
                  <input
                    class="input is-medium"
                    name="password"
                    type="password"
                    
                    required
                    v-model="password"
                  />
                </div>
              </div>

              <div class="field">
                <label class="label">Password Confirm</label>
                <div class="control">
                  <input
                    class="input is-medium"
                    type="password"
                    name="password_confirm"
                    
                    required
                    v-model="password_confirm"
                  />
                </div>
              </div>
              <button class="button is-info" type="submit">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, onMounted, ref } from "vue";
import axios from "axios";
import { User } from "@/classes/user";
import { useStore } from 'vuex';
export default {
  name: "Profile",
  setup() {
    const username = ref("");
    const email = ref("");
    const password = ref("");
    const password_confirm = ref("");
    const store = useStore()

    onMounted(async () => {
        const user = computed(() => store.state.User.user)
     

      
      username.value = user.value.username; 
      email.value = user.value.email;
    });

    const submitProfile = async() => {
        const res = await axios.put('user/info', {
            username: username.value,
            email: email.value
        })
        const  u : User = res.data.data
        await store.dispatch('User/setUser', new User(
          u.id,
          u.username,
          u.email,
          u.role,
          u.permissions
        ))
    }

    const submitPassword = async () => {
        await axios.put('user/password', {
            password: password.value,
            password_confirm: password_confirm.value
        })

        password.value = ''
        password_confirm.value = ''
    }

    return {
      username,
      email,
      password,
      password_confirm,
      submitProfile,
      submitPassword
    };
  },
};
</script>