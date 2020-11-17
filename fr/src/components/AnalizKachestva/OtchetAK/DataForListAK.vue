<template>
  <v-container>
    <v-card>
      <v-card-title>
        <span class="headline">Наименование отчета:</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <div>
            <span class="fontsiz">{{ this.itemOtch.name }}</span>
          </div>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <div class="centerBtn">
          <v-btn color="green darken-1" dark @click="srKlink">
            Средний коэф.
          </v-btn>
        </div>
        <div class="centerBtn">
          <v-btn color="orange darken-1" dark @click="punkt5link">
            Пункт 5
          </v-btn>
        </div>
        <div class="centerBtn">
          <v-btn color="blue darken-1" dark @click="punkt7link">
            Пункт 7
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>

import router from "../../../router";
export default {
  props: {
    itemOtch: {
      type: Object,
      default: function() {
        return {};
      },
    },
  },
  data: () => ({
    errored: false,
    loading: false,
    datetime: null,
    datetime2: null,
    editNameAF: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  methods: {
    srKlink() {
      localStorage.setItem("idSrK", JSON.stringify(this.itemOtch))
      router.push({ name: "otchetsrk" });
    },
    punkt5link() {
      localStorage.setItem("idPunkt5", JSON.stringify(this.itemOtch))
      router.push({ name: "otchetp5" });
    },
    punkt7link() {
      localStorage.setItem("idPunkt7", JSON.stringify(this.itemOtch))
      router.push({ name: "otchetp7" });
    },
  },
};
</script>

<style scoped>
.fontsiz {
  font-size: 16px;
  margin-right: 8px;
  color: black;
}
.centerBtn {
  margin-left: auto;
  margin-right: auto;
}
</style>
