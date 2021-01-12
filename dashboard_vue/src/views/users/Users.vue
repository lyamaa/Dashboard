<template>
  
    <div class="columns dash">
      <div class="column is-12">
        <div class="card events-card">
          <div class="buttons" v-if="authUser.canEdit('users')">
            <router-link to="/user/create" class="button is-primary mt-2" style="margin-left: 1rem" >Create User</router-link>
            
          </div>
          <header class="card-header">
            <p class="card-header-title">Users</p>
            <a href="#" class="card-header-icon" aria-label="more options">
              <span class="icon">
                <i class="fa fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>
          <div class="card-table">
            <div class="content">
              <table class="table is-fullwidth is-striped">
                <thead>
                  <tr>
                    <th><abbr title="Position">#</abbr></th>
                    <th><abbr title="Played">Name</abbr></th>
                    <th><abbr title="Won">Email</abbr></th>
                    <th><abbr title="Drawn">Roles</abbr></th>
                    <th><abbr title="Lost">Action</abbr></th>
                  </tr>
                </thead>

                <tfoot>
                  <tr>
                    <th><abbr title="Position"> #</abbr></th>
                    <th><abbr title="Played">Name</abbr></th>
                    <th><abbr title="Won">Email</abbr></th>
                    <th><abbr title="Drawn">Roles</abbr></th>
                    <th><abbr title="Lost">Action</abbr></th>
                  </tr>
                </tfoot>
                <tbody>
                  <tr v-for="user in users" :key="user.id">
                    <td>{{ user.id }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.email }}</td>
                    <td>{{ user.role.name }}</td>
                    <td>
                     <div v-if="authUser.canEdit('users')">
                        <router-link
                        :to="`/users/${user.id}/edit`"
                        class="button is-small is-primary"
                        >Edit</router-link
                      >
                      &nbsp;
                      <a
                        href="javascript:void(0)"
                        class="button is-small is-danger"
                        @click="del(user.id)"
                        >Delete</a
                      >
                     </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
           <Pagination :last-page="lastPage" @page-changed="load($event)"/>
        </div>
      </div>
    </div>
</template>
<script lang="ts">
import { ref, onMounted, computed } from "vue";
import { Entity } from "../../interfaces/entity";
import axios from "axios";
import Pagination from '../../components/Pagination.vue';
import { useStore } from 'vuex';

export default {
  name: "Users",
  components: { Pagination },
  setup() {
    const users = ref([]);
    const lastPage = ref(0)
    const store = useStore()

    const authUser = computed(() => store.state.User.user)

    const load = async (page = 1) => {
      const res = await axios.get(`users?page=${page}`);

      users.value = res.data.data;
      lastPage.value = res.data.meta.last_page;
    };

    
    onMounted(load);

    const del = async (id: number) => {
      if (confirm("Are you sure to delete.!!")) {
        const res = await axios.delete(`user/${id}`);

        users.value = users.value.filter((e: Entity) => e.id !== id);
      }
    };

    const edit = () => {};

    return {
      users,
      authUser,
      load,
      lastPage,
      del,
    };
  },
};
</script>