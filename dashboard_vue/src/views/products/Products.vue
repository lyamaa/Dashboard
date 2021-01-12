<template>
  <div class="columns dash">
    <div class="column is-12">
      <div class="card events-card">
        <div class="buttons" style="">
          <router-link
            to="/product/create"
            class="button is-info mt-2"
            style="margin-left: 1rem"
            >New Product</router-link
          >
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
                  <th><abbr title="Played">Image</abbr></th>
                  <th><abbr title="Lost">Title</abbr></th>
                  <th><abbr title="Lost">Description</abbr></th>
                  <th><abbr title="Lost">Price</abbr></th>
                  <th><abbr title="Lost">Actions</abbr></th>
                </tr>
              </thead>

              <tfoot>
                <tr>
                  <th><abbr title="Position">#</abbr></th>
                  <th><abbr title="Played">Image</abbr></th>
                  <th><abbr title="Lost">Title</abbr></th>
                  <th><abbr title="Lost">Description</abbr></th>
                  <th><abbr title="Lost">Price</abbr></th>
                  <th><abbr title="Lost">Actions</abbr></th>
                </tr>
              </tfoot>
              <tbody>
                <tr v-for="product in products" :key="product.id">
                  <td>{{ product.id }}</td>
                  <td><img :src="product.image" height="20" /></td>
                  <td>{{ product.title }}</td>
                  <td>{{ product.description }}</td>
                  <td>{{ product.price }}</td>

                  <td>
                    <router-link :to="`/product/${product.id}/edit`" class="button is-small is-primary"
                      >Edit</router-link
                    >
                    &nbsp;
                    <a
                      href="javascript:void(0)"
                      class="button is-small is-danger"
                      @click="del(product.id)"
                      >Delete</a
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

<script lang="ts">
import { onMounted, ref } from "vue";
import axios from "axios";
import {Entity} from "@/interfaces/entity"
import Pagination from '@/components/Pagination.vue';
export default {
   name: "Products",
  components: { Pagination },
  setup() {
    const products = ref([]);
    const lastPage = ref(0)
    

    const load = async (page = 1 ) => {
       const res = await axios.get(`products?page=${page}`);

      products.value = res.data.data;
      lastPage.value = res.data.meta.last_page
    }  

   onMounted(load)
  
    const del = async (id: number) => {
        if(confirm('Are You sure want to delete this user?')){
            await axios.delete(`products/${id}`)
            products.value = products.value.filter((e: Entity) => e.id !== id)
        }
    }
    
    return {
      products,
      del,
      lastPage,
      load,
    };
  },

  
};
</script>