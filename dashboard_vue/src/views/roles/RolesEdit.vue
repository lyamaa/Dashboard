<template>
    <form class="box" @submit.prevent="submit">
    <div class="field">
      <label class="label">Name</label>
      <div class="control">
        <input
          class="input is-medium"
          name="name"
          type="text"
         
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
            :checked="checked(permission.id)"
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
import axios from 'axios';

import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Role } from '@/classes/role';

export default {
    name: "RolesEdit",

    setup() {
    const name = ref("");
    const permissions = ref([]);
    const selected = ref([] as number[]);
    const router = useRouter()
    const {params} = useRoute( )

    onMounted(async () => {
      const res = await axios.get("permissions");

      permissions.value = res.data.data;

      const roleCall = await axios.get(`roles/${params.id}`)
      const role: Role = roleCall.data.data
      name.value = role.name

      selected.value = role.permissions.map(p => p.id)
    });

    const select = (id: number, checked: boolean) => {
      if (checked) {
        selected.value = [...selected.value, id];

        return;
      }

      selected.value = selected.value.filter((s) => s !== id);
    };

    const submit = async () => {
      await axios.put(`roles/${params.id}`, {
        name: name.value,
        permissions: selected.value,
      });

      await router.push("/roles");
    };

    const checked =  (id: number) => selected.value.some(s => s === id)
    
        

    return {
      name,
      permissions,
      select,
      selected,
      submit,
      checked,
    };
  },
}
</script>