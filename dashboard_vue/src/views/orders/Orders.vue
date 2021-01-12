<template>

    <div class="columns dash">
      <div class="column is-12">
        <div class="card events-card">
          <div class="buttons" v-if="authUser.canEdit('users')">
            <a  class="button is-primary mt-2" style="margin-left: 1rem" @click="exportCSV">Export CSV</a>
            
          </div>
          <header class="card-header">
            <p class="card-header-title">Order</p>
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
                    <th><abbr title="Drawn">Total</abbr></th>
                    <th><abbr title="Lost">Action</abbr></th>
                  </tr>
                </thead>

                <tfoot>
                  <tr>
                    <th><abbr title="Position"> #</abbr></th>
                    <th><abbr title="Played">Name</abbr></th>
                    <th><abbr title="Won">Email</abbr></th>
                    <th><abbr title="Drawn">Total</abbr></th>
                    <th><abbr title="Lost">Action</abbr></th>
                  </tr>
                </tfoot>
                <tbody>
                  <tr v-for="order in orders" :key="order.id">
                    <td>{{ order.id }}</td>
                    <td>{{ order.first_name }} | {{ order.last_name }}</td>
                    <td>{{ order.email }}</td>
                    <td>{{ order.total }}</td>
                    <td>
                      <router-link
                        :to="`/orders/${order.id}`"
                        class="button is-small is-primary"
                        >View</router-link
                      >
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

<script>
import { computed, onMounted, ref } from 'vue'
import Pagination from "../../components/Pagination.vue"
import axios from 'axios';
import { useStore } from 'vuex';
    export default {
        name: "Orders",
        components: {Pagination},

        setup() {
            const orders = ref([]);
            const lastPage= ref(0)
             const store = useStore()

             const authUser = computed(() => store.state.User.user)

            const load = async(page = 1) => {
                const res = await axios.get(`orders?page=${page}`)

                orders.value = res.data.data
                lastPage.value = res.data.meta.last_page;
            }

            onMounted(load)

            const exportCSV = async () => {
              const res = await axios.get('export', {responseType: 'blob'});
              const blob = new Blob([res.data], {type: 'text/csv'})
              const download = window.URL.createObjectURL(res.data)
              const link = document.createElement('a')
              link.href = download
              link.download = 'orders.csv'
              link.click()

              console.log(res)
            }

            return {
                orders,
                lastPage,
                load,
                exportCSV,
                authUser,
            }
        }


    }
</script>