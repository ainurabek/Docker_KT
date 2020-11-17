<template>
  <v-container fluid>
    <line-chart-container></line-chart-container>
    <bar-chart-container></bar-chart-container>
  </v-container>
</template>

<script>
import LineChartContainer from "./LineChart/LineChartContainer";
import BarChartContainer from "./BarChart/BarChartContainer";


export default {
  name: "Home",
  components: { LineChartContainer, BarChartContainer },
  data: () => ({
    loaded: false,
    loadedBar: false,
  }),
};
</script>

<style scoped></style>