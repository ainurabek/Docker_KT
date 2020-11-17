import { Bar, mixins } from "vue-chartjs";
export default {
  extends: Bar,
  props: ["options", "chartData"],
  mixins: [mixins.reactiveProp],
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
  watch: {
    options() {
      this.renderChart(this.chartData, this.options);
    },
  },
};
//  urlStatsBar: "http://0.0.0.0:8000/apps/dispatching/api/event/out-week/",
