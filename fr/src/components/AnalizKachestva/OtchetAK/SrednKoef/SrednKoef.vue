<template>
  <v-container>
    <v-card>
      <v-card-title>
        <span class="headline-2">Создать таблицу среднего коэффициента: {{id57.name}}</span>

      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12" sm="6" md="3">
            <v-text-field
              label="Начало, дата и время"
              type="date"
              v-model="datetime"
              outlined
              dense
              min="1990-06-01"
              max="2099-06-30"
            ></v-text-field>
          </v-col>
          <v-col  cols="12" sm="6" md="3">
            <v-text-field
              label="Конец, дата и время"
              type="date"
              v-model="datetime2"
              outlined
              dense
              min="1990-06-01"
              max="2099-06-30"
            ></v-text-field>
          </v-col>
          <v-col  cols="12" sm="6" md="2">
            <v-autocomplete
              label="Предприятие"
              v-model="editOutfitSrK"
              :items="outfit"
              item-text="outfit"
              item-value="id"
              dense
            >
            </v-autocomplete>
          </v-col>
          <v-col  cols="12" sm="6" md="2">
            <v-autocomplete
              label="Пункт 7"
              v-model="editPunkt7"
              :items="punkt7"
              item-text="name"
              item-value="id"
              dense
            >
            </v-autocomplete>
          </v-col>
          <v-col  cols="12" sm="6" md="2">
            <v-btn class="ml-4" color="green darken-1" dark @click="createSrK">
              Создать
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
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
    <DataTableSrK></DataTableSrK>
  </v-container>
</template>

<script>
import DataTableSrK from "./DataTableSrK"
import { bus } from "../../../../main"
import router from "../../../../router";

export default {
  components: { DataTableSrK },
  data: () => ({
    errored: false,
    loading: false,
    datetime: null,
    datetime2: null,
    editOutfitSrK: null,
    editPunkt7: null,
    idForSrk: "",
    outfit: [],
    punkt7: [],
    id57: {},
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  mounted() {
    this.getOutfit()
    this.getIdForSrK()
    this.getPunkt7()
  },
  methods: {
    getPunkt7() {
      this.$http
        .get(`${this.url.baseUrl}/apps/analysis/form/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          if (response.status == 200) {
            this.punkt7 = response.data
          }
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    punkt5link() {
      localStorage.setItem("idPunkt5", JSON.stringify(this.id57))
      router.push({ name: "otchetp5" });
    },
    punkt7link() {
      localStorage.setItem("idPunkt7", JSON.stringify(this.id57))
      router.push({ name: "otchetp7" });
    },
    getIdForSrK() {
      this.id57 = JSON.parse(localStorage.getItem("idSrK"))
      this.idForSrk = JSON.parse(localStorage.getItem("idSrK")).id
      this.datetime = this.id57.date_from
      this.datetime2 = this.id57.date_to
      console.log(this.id57)
    },
    getOutfit() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.outfit = response.data;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    createSrK() {
      this.$http
        .post(
          `${this.url.baseUrl}/apps/analysis/form/create/${this.idForSrk}/`,
          {
            date_from: this.datetime,
            date_to: this.datetime2,
            outfit: this.editOutfitSrK,
            form_analysis: this.editPunkt7
          },
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            bus.$emit("updateOtchetSrK");
          }
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>

<style scoped>
.centerBtn {
  margin-left: auto;
  margin-right: auto;
}
</style>
