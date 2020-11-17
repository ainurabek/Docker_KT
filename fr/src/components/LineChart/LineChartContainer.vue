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
      <line-chart
        v-if="loaded"
        :chart-data="datacollection"
        :options="chartOptions"
        :styles="myStyles"
      ></line-chart>
    </v-col>
  </v-row>
</template>

<script>
import LineChart from "./LineChart";

export default {
  name: "LineChartContainer",
  components: { LineChart },
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
    urlStatsLine: "http://0.0.0.0:8000/apps/dispatching/api/event/today/",

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
        let response = await this.$http.get(this.urlStatsLine);
        if (
          this.urlStatsLine ===
          "http://0.0.0.0:8000/apps/dispatching/api/event/today/"
        ) {
          this.dataLabels = response.data.dates.map((t) => {
            return t.time;
          });
          this.dataCount = response.data.dates.map((t) => {
            return t.counts;
          });
          this.fillData({ id: 1 });
          this.loaded = true;
          console.log(this.dataLabels, this.dataCount);
        } else if (
          this.urlStatsLine ===
          "http://0.0.0.0:8000/apps/dispatching/api/event/week/"
        ) {
          this.dataLabels = response.data.dates.map((t) => {
            return t.date;
          });
          this.dataCount = response.data.dates.map((t) => {
            return t.counts;
          });
          this.fillData({ id: 2 });
          this.loaded = true;
          console.log(this.dataLabels);
        } else if (
          this.urlStatsLine ===
          "http://0.0.0.0:8000/apps/dispatching/api/event/month/"
        ) {
          this.dataLabels = response.data.dates.map((t) => {
            return t.date;
          });
          this.dataCount = response.data.dates.map((t) => {
            return t.counts;
          });
          this.fillData({ id: 3 });
          this.loaded = true;
          console.log(this.dataLabels);
        }
      } catch (err) {
        console.log(err);
      }
    },
    fillData(item) {
      if (item != undefined) {
        console.log(item.id);
        if (item.id == 1) {
          (this.minTime =
            new Date().toISOString().substring(0, 11) + "00:00:00"),
            (this.maxTime =
              new Date().toISOString().substring(0, 11) + "23:59:59");
          this.unitChange = "hour";
          this.unitStepSizeChange = 1;
          this.tooltipFormatChange = "L HH:mm";
          this.urlStatsLine =
            "http://0.0.0.0:8000/apps/dispatching/api/event/today/";
        } else if (item.id == 2) {
          let minWeek = new Date().setDate(this.today.getDate() - 7);
          let minTimeWeek =
            new Date(minWeek).toISOString().substring(0, 11) + "00:00:00";
          let maxTimeWeek =
            new Date().toISOString().substring(0, 11) + "23:59:59";
          console.log(minTimeWeek, maxTimeWeek);
          this.minTime = minTimeWeek;
          this.maxTime = maxTimeWeek;
          this.unitChange = "day";
          this.unitStepSizeChange = 1;
          this.tooltipFormatChange = "L";
          this.urlStatsLine =
            "http://0.0.0.0:8000/apps/dispatching/api/event/week/";
        } else if (item.id == 3) {
          let minMonth = new Date().setDate(this.today.getDate() - 30);
          let minTimeMonth =
            new Date(minMonth).toISOString().substring(0, 11) + "00:00:00";
          let maxTimeMonth =
            new Date().toISOString().substring(0, 11) + "23:59:59";
          console.log(minTimeMonth, maxTimeMonth);
          this.minTime = minTimeMonth;
          this.maxTime = maxTimeMonth;
          this.unitChange = "day";
          this.unitStepSizeChange = 3;
          this.tooltipFormatChange = "L";
          this.urlStatsLine =
            "http://0.0.0.0:8000/apps/dispatching/api/event/month/";
        }
      } else {
        (this.minTime = new Date().toISOString().substring(0, 11) + "00:00:00"),
          (this.maxTime =
            new Date().toISOString().substring(0, 11) + "23:59:59");
        this.unitChange = "hour";
        this.unitStepSizeChange = 1;
        this.tooltipFormatChange = "L HH:mm";
      }
      this.datacollection = {
        labels: this.dataLabels.map((t) => {
          return new Date(t);
        }),
        datasets: [
          {
            label: "Кол-во событий событий",
            data: this.dataCount,
            lineTension: 0.25,
            fill: false,
            borderColor: "orange",
            backgroundColor: "transparent",
            pointBorderColor: "orange",
            pointBackgroundColor: "rgba(255,150,0,0.5)",
            borderDash: [5, 5],
            pointRadius: 5,
            pointHoverRadius: 10,
            pointHitRadius: 30,
            pointBorderWidth: 2,
            pointStyle: "rectRounded",
          },
        ],
        grid: {
          show: true,
          aboveData: true,
          color: "#3f3f3f",
          labelMargin: 10,
          axisMargin: 0,
          borderWidth: 0,
          borderColor: null,
          minBorderMargin: 5,
          clickable: true,
          hoverable: true,
          autoHighlight: true,
          mouseActiveRadius: 100,
        },
      };
      this.chartOptions = {
        legend: {
          display: true,
          position: "top",
          labels: {
            boxWidth: 80,
            fontColor: "black",
          },
        },
        scales: {
          xAxes: [
            {
              type: "time",
              time: {
                unit: this.unitChange,
                unitStepSize: this.unitStepSizeChange,
                round: "hour",
                tooltipFormat: this.tooltipFormatChange,
                displayFormats: {
                  hour: "HH:mm",
                  day: "MMM D",
                },
              },
              ticks: {
                min: this.minTime,
                max: this.maxTime,
              },
              distribution: "linear",
            },
          ],
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
              gridLines: {
                color: "black",
                borderDash: [2, 2],
              },
              // scaleLabel: {
              //   display: true,
              //   labelString: "Количество событий",
              //   fontColor: "green",
              // },
            },
          ],
        },
        responsive: true,
        maintainAspectRatio: false,
      };
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
