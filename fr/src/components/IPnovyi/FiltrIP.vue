<template>
  <v-container>
    <v-toolbar-title>Список ИП</v-toolbar-title>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-select
          label="ТПО, Индекс"
          v-model="editedItemTpo"
          :items="tpo"
          item-value="id"
          item-text="index"
        >
        </v-select>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-autocomplete
          label="ИП"
          v-model="editedItemPoint"
          :items="point"
          item-value="id"
          item-text="point"
        >
        </v-autocomplete> </v-col
      ><v-col cols="12" sm="6" md="4">
        <v-select
          label="Объект"
          v-model="editedItemObject"
          :items="obj"
          item-value="id"
          item-text="name"
        >
        </v-select>
      </v-col>
    </v-row>
    <v-btn color="primary" class="mr-12" @click="initialize, tpoGet, outfitGet"
      >Обновить</v-btn
    >

    <v-btn color="primary" @click="clearAll">Очистить</v-btn>

    <IP
      :editedItemTpoProps="editedItemTpo"
      :editedItemPointProps="editedItemPoint"
      :editedItemObjectProps="editedItemObject"
    ></IP>
  </v-container>
</template>

<script>
import IP from "./IP";
export default {
  components: { IP },
  data: () => ({
    tpo: [],
    point: [],
    obj: [],
    editedItemTpo: "",
    editedItemPoint: "",
    editedItemObject: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  mounted() {
    this.initialize();
    this.tpoGet();
    this.pointGet();
  },
  methods: {
    clearAll() {
      (this.editedItemTpo = ""),
        (this.editedItemPoint = ""),
        (this.editedItemObject = "");
    },
    pointGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/point/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.point = response.data;
          console.log(this.point);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    tpoGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/tpo/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.tpo = response.data;
          console.log(this.tpo);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/objects/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.obj = response.data;
          console.log(this.obj);
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
