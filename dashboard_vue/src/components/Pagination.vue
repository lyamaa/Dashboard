<template>
  <footer class="card-footer" style="margin-top: 4rem">
    <nav class="pagination" role="navigation" aria-label="pagination">
      <a href="javascript:void(0)" class="pagination-previous" @click="prev">Previous</a>
      <a href="javascript:void(0)" class="pagination-next" @click="next">Next page</a>
      <ul class="pagination-list"></ul>
    </nav>
  </footer>
</template>

<script>
import { ref } from "vue";
export default {
  name: "Pagination",
  emits: ['page-changed'],
  props: {
    lastPage: Number
  },

  setup(props, {emit}) {
    const page = ref(1);
    const lastPage = ref(0)
   
   
    const next = async () => {
      if (page.value === props.lastPage) return;
      page.value++
      emit('page-changed', page.value)
    };

    const prev = async () => {
      if (page.value === 1) return;
      page.value--;
      emit('page-changed', page.value)
    };

    return {
      page,
      lastPage,
      next,
      prev,
    };
  },
};
</script>