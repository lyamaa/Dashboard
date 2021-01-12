<template>
  <form class="box" @submit.prevent="submit">
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

    <div class="field">
      <label class="label">Role</label>
      <div class="control">
        <div class="select">
          <select name="role" v-model="role_id">
            <option value="0">Select Roles</option>
            <option v-for="role in roles" :key="role.id" :value="role.id">
              {{ role.name }}
            </option>
          </select>
        </div>
      </div>
    </div>

    <button class="button is-block is-primary is-fullwidth is-medium">
      Submit
    </button>
    <br />
    <small><em>Lorem ipsum dolor sit amet consectetur.</em></small>
  </form>
</template>


<script lang="ts">
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
export default {
  name: "UserCreate",

  setup() {
    const username = ref("");
    const email = ref("");
    const role_id = ref(0);
    const roles = ref([]);
    const router = useRouter();

    onMounted(async () => {
      const res = await axios.get("roles");

      roles.value = res.data.data;
    });

    const submit = async () => {
      await axios.post("users", {
        username: username.value,
        email: email.value,
        role_id: role_id.value,
      });

      await router.push("/users");
    };

    return {
      username,
      email,
      role_id,
      roles,
      submit,
    };
  },
};
</script>