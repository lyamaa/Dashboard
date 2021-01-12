<template>
  <div class="columns dash">
    <div class="column is-12">
      <div class="card events-card">
        <div class="buttons" style="">
          <router-link
            to="/"
            class="button is-primary mt-2"
            style="margin-left: 1rem"
            >Export CSV</router-link
          >
        </div>
        <header class="card-header">
          <p class="card-header-title">Order Items</p>
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
                  <th><abbr title="Position"> #</abbr></th>
                  <th><abbr title="Played">Product Title</abbr></th>
                  <th><abbr title="Won">Price</abbr></th>
                  <th><abbr title="Drawn">Quantity</abbr></th>
                </tr>
              </thead>

              <tfoot>
                <tr>
                  <th><abbr title="Position"> #</abbr></th>
                  <th><abbr title="Played">Product Title</abbr></th>
                  <th><abbr title="Won">Price</abbr></th>
                  <th><abbr title="Drawn">Quantity</abbr></th>
                </tr>
              </tfoot>
              <tbody>
                <tr v-for="item in orderItems" :key="item.id">
                  <td>{{ item.id }}</td>
                  <td>{{ item.product_title }}</td>
                  <td>{{ item.price }}</td>
                  <td>{{ item.quantity }}</td>
                
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <Pagination :last-page="lastPage" @page-changed="load($event)" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
export default {
  name: "OrderItems",
  setup() {
      const orderItems = ref([])
      const {params} = useRoute()

      onMounted( async () => {
          const res = await axios.get(`orders/${params.id}`)

          orderItems.value = res.data.data.order_items
          console.log(res)
      })

      return {
          orderItems,

      }
  }
};
</script>