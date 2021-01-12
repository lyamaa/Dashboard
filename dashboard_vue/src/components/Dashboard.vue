<template>
  <div class="column is-9">
    <Section />
    <section class="info-tiles">
      <div class="tile is-ancestor has-text-centered">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title">439k</p>
            <p class="subtitle">Users</p>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title">59k</p>
            <p class="subtitle">Products</p>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title">3.4k</p>
            <p class="subtitle">Open Orders</p>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title">19</p>
            <p class="subtitle">Exceptions</p>
          </article>
        </div>
      </div>
    </section>
    <div class="columns dash">
      <div class="column is-12">
        <div class="card events-card mt-5">
          <header class="card-header">
            <p class="card-header-title">Bar Chart</p>
            <a href="#" class="card-header-icon" aria-label="more options">
              <span class="icon">
                <i class="fa fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>

          <div class="content mt-5 mb-2">
            <div id="chart" class="mt-5"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="columns dash">
      <!-- here -->
      <div class="column is-12">
        <!-- here -->
        <div class="card events-card">
          <header class="card-header">
            <p class="card-header-title">Area Chart</p>
            <a href="#" class="card-header-icon" aria-label="more options">
              <span class="icon">
                <i class="fa fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>

          <div class="content">
            <div id="chart1" class="mt-5"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- here -->
    <div class="columns dash">
      <div class="column is-12">
        <div class="card events-card">
          <header class="card-header">
            <p class="card-header-title">Pie Chart</p>
            <a href="#" class="card-header-icon" aria-label="more options">
              <span class="icon">
                <i class="fa fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>

          <div class="content">
            <div id="chart2" class="mt-5"></div>
          </div>
        </div>
      </div>
      <!-- here -->
    </div>
    <!-- END -->
  </div>
</template>

<script lang="ts">
import { onMounted } from "vue";
import * as c3 from "c3";
import Section from "./Section.vue";
import axios from "axios";
export default {
  name: "Dashboard",
  components: {
    Section,
  },

  setup() {
    onMounted(async () => {
      const chart = c3.generate({
        bindto: "#chart",
        data: {
          x: "x",
          columns: [["x"], ["Sales"]],
          types: {
            Sales: "bar",
          },
        },
        axis: {
          x: {
            type: "timeseries",
            tick: {
              format: "%Y-%m-%d",
            },
          },
        },
      });

      const chart1 = c3.generate({
        bindto: "#chart1",

        data: {
          x: "x",
          columns: [["x"], ["Sales"]],
          types: {
            Sales: "area",
            x: "area-spline",
          },
        },
        axis: {
          x: {
            type: "timeseries",
            tick: {
              format: "%Y-%m-%d",
            },
          },
        },
      });

      const chart2 = c3.generate({
        bindto: "#chart2",

        data: {
          x: "x",
          columns: [["x"], ["Sales"]],
          type: 'spline',
        },
        axis: {
          x: {
            type: "timeseries",
            tick: {
              format: "%Y-%m-%d",
               fit: true
            },
          },
        },
      });

      const res = await axios.get("chart");

      const records = res.data.data;

      chart.load({
        columns: [
          ["x", ...records.map((r: any) => r.date)],
          ["Sales", ...records.map((r: any) => r.sum)],
        ],
      });
      chart1.load({
        columns: [
          ["x", ...records.map((r: any) => r.date)],
          ["Sales", ...records.map((r: any) => r.sum)],
        ],
      });
      chart2.load({
        columns: [
          ["x", ...records.map((r: any) => r.date)],
          ["Sales", ...records.map((r: any) => r.sum)],
        ],
      });
    });
  },
};
</script>

