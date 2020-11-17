<template>
  <v-row>
    <v-col cols="12" sm="4" md="2">
      <v-list class="mt-5">
        <v-list-item-group v-model="radioGroup" mandatory color="indigo">
          <v-list-item
            v-for="(item, id) in radioArray"
            :key="id"
            @click="fillData(item)"
          >
            <v-list-item-content>
              <v-list-item-title v-text="item.name"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-col>
    <v-divider vertical></v-divider>
    <v-col cols="12" sm="4" md="9">
      <bar-chart
        v-if="loaded"
        :chart-data="datacollection"
        :options="chartOptions"
        :styles="myStyles"
      ></bar-chart>
    </v-col>
  </v-row>
</template>

<script>
import BarChart from "./BarChart";

export default {
  name: "BarChartContainer",
  components: { BarChart },
  data: () => ({
    loaded: false,
    dataLabels: [],
    dataCount: [],
    datacollection: {},
    today: new Date(),
    minTime: "",
    maxTime: "",
    unitChange: "",
    tooltipFormatChange: "",
    unitStepSizeChange: 1,
    urlStatsBar:
      "http://0.0.0.0:8000/apps/dispatching/api/event/out-week/",
    chartOptions: null,
    radioGroup: 0,
    radioArray: [
      {
        id: 1,
        name: "День",
      },
      {
        id: 2,
        name: "Неделя",
      },
      {
        id: 3,
        name: "Месяц",
      },
    ],
  }),
  watch: {
    radioGroup() {
      this.init();
    },
  },
  methods: {
    async init() {
      this.loaded = false;
      try {
        let response = await this.$http.get(this.urlStatsBar);
        if (
          this.urlStatsBar ===
          "http://0.0.0.0:8000/apps/dispatching/api/event/out-today/"
        ) {
          this.dataLabels = response.data.map((t) => {
            return t.outfit
          })
          this.dataCount = response.data.map((t) => {
            return t.counts
          })
          this.fillData({ id: 1 });
          this.loaded = true;
          console.log(response.data, this.dataLabels, this.dataCount);
        } else if (
          this.urlStatsBar ===
          "http://0.0.0.0:8000/apps/dispatching/api/event/out-week/"
        ) {
          this.dataLabels = response.data.map((t) => {
            return t.outfit
          })
          this.dataCount = response.data.map((t) => {
            return t.counts
          })
          this.fillData({ id: 2 });
          this.loaded = true;
          console.log(response.data, this.dataLabels);
        } else if (
          this.urlStatsBar ===
          "http://0.0.0.0:8000/apps/dispatching/api/event/out-month/"
        ) {
          this.dataLabels = response.data.map((t) => {
            return t.outfit
          })
          this.dataCount = response.data.map((t) => {
            return t.counts
          })
          this.fillData({ id: 3 });
          this.loaded = true;
          console.log(response.data, this.dataLabels);
        }
      } catch (err) {
        console.log(err);
      }
    },
    fillData(item) {
      if (item != undefined) {
        console.log(item.id);
        if (item.id == 1) {
          this.urlStatsBar =
            "http://0.0.0.0:8000/apps/dispatching/api/event/out-today/";
        } else if (item.id == 2) {
          this.urlStatsBar =
            "http://0.0.0.0:8000/apps/dispatching/api/event/out-week/";
        } else if (item.id == 3) {
          this.urlStatsBar =
            "http://0.0.0.0:8000/apps/dispatching/api/event/out-month/";
        }
      } else {
        this.urlStatsBar =
          "http://0.0.0.0:8000/apps/dispatching/api/event/out-today/";
      }
      (this.datacollection = {
        labels: this.dataLabels,
        datasets: [
          {
            label: "Предприятия и количество событий",
            data: this.dataCount,
            backgroundColor: 
              // "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              // "rgba(255, 206, 86, 0.2)",
              // "rgba(75, 192, 192, 0.2)",
              // "rgba(153, 102, 255, 0.2)",
              // "rgba(255, 159, 64, 0.2)",
          // ],
            borderColor: 
              // "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              // "rgba(255, 206, 86, 1)",
              // "rgba(75, 192, 192, 1)",
              // "rgba(153, 102, 255, 1)",
              // "rgba(255, 159, 64, 1)",
            // ],
            borderWidth: 1,
          },
        ],
      }),
        (this.chartOptions = {
          scales: {
           yAxes: [
            {
              ticks: {
                beginAtZero: true,
                suggestedMin: 10,
                suggestedMax: 15
              },
            },
          ],
        },
        responsive: true,
        maintainAspectRatio: false,
        });
    },
  },
  computed: {
    myStyles() {
      return {
        height: `40vh`,
        position: "relative",
      };
    },
  },
  mounted() {
    this.init();
  },
};
</script>

<style scoped></style>
