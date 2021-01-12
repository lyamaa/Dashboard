<template>
      <div class="columns dash">
      <div class="column is-12">
        <div class="card events-card">
          <div class="buttons" v-if="authUser.canEdit('users')">
            <router-link to="/roles/create" class="button is-info mt-2" style="margin-left: 1rem">New Role</router-link>
            
          </div>
          <header class="card-header">
            <p class="card-header-title">Events</p>
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
                    <th><abbr title="Lost">Action</abbr></th>
                  </tr>
                </thead>

                <tfoot>
                  <tr>
                    <th><abbr title="Position"> #</abbr></th>
                    <th><abbr title="Played">Name</abbr></th>
                    <th><abbr title="Lost">Action</abbr></th>
                  </tr>
                </tfoot>
                <tbody>
                  <tr v-for="role in roles" :key="role.id">
                    <td>{{role.id}}</td>
                    <td>{{role.name}}</td>
                    
                    <td>
                      <div v-if="authUser.canEdit('users')">
                        <router-link
                        :to="`/roles/${role.id}/edit`"
                        class="button is-small is-primary"
                        >Edit</router-link
                      >
                      &nbsp;
                      <a
                        href="javascript:void(0)"
                        class="button is-small is-danger"
                        @click="del(role.id)"
                        >Delete</a
                      >
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          
        </div>
      </div>
    </div>
</template>
<script lang="ts">
import axios from "axios"
import { computed, onMounted, ref } from 'vue'
import { Entity } from '../../interfaces/entity';
import { useStore } from 'vuex';

    export default {
        name: "Roles",
    
        setup(){
            const roles = ref([]);
            const store = useStore()

            const authUser = computed(() => store.state.User.user)

            onMounted(async () => {
                const response = await axios.get('roles')

                roles.value = response.data.data
            })

            const del = async (id: number) => {
                if(confirm("Are you sure to delete this record?")){
                    await axios.delete(`roles/${id}`)

                    roles.value = roles.value.filter((e:Entity) => e.id !== id)
                }
            }

            return{
                roles,
                del,
                authUser,
            }
        }
    }
</script>