<template>
  <form class="box" @submit.prevent="submit">
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input
          class="input is-medium"
          name="name"
          type="text"
          placeholder="Username"
          required
          v-model="name"
        />
      </div>
    </div>

    <label class="label">Permission</label>
    <div class="field">
      <div
        class="control"
        v-for="permission in permissions"
        :key="permission.id"
      >
        <label class="checkbox">
          <input
            type="checkbox"
            :value="permission.id"
            @change="select(permission.id, $event.target.checked)"
          />
          &nbsp;<strong>{{ permission.name }}</strong>
        </label>
      </div>
    </div>
    <button class="button is-block is-primary is-fullwidth is-medium">
      Submit
    </button>
  </form>
</template>

<script lang="ts">
import { onMounted, ref } from "vue";
import axios from "axios";
import router from "@/router";
export default {
  name: "RolesCreate",
  setup() {
    const name = ref("");
    const permissions = ref([]);
    const selected = ref([] as number[]);

    onMounted(async () => {
      const res = await axios.get("permissions");

      permissions.value = res.data.data;
    });

    const select = (id: number, checked: boolean) => {
      if (checked) {
        selected.value = [...selected.value, id];

        return;
      }

      selected.value = selected.value.filter((s) => s !== id);
    };

    const submit = async () => {
      await axios.post("roles", {
        name: name.value,
        permissions: selected.value,
      });

      await router.push("/roles");
    };

    return {
      name,
      permissions,
      select,
      selected,
      submit,
    };
  },
};
</script>