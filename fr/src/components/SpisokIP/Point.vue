<template>
  <v-container>
    <v-toolbar-title>Фильтр объектов</v-toolbar-title>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-select
          label="ТПО, Индекс"
          v-model="editedItemTpo"
          :items="tpo"
          item-value="index"
          item-text="name"
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.name }} - {{ item.index }}
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.name }} - {{ item.index }}
          </template>
        </v-select>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-select
          label="Название"
          v-model="editedItemPoint"
          :items="point"
          item-value="point"
          item-text="point"
        >
        </v-select> </v-col
      ><v-col cols="12" sm="6" md="4">
        <v-select
          label="Предприятие"
          v-model="editedItemOutfit"
          :items="id_outfit"
          item-value="outfit"
          item-text="outfit"
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
      :editedItemOutfitProps="editedItemOutfit"
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
    name: [],
    id_outfit: [],
    tpoEdited: {},
    editedItemTpo: "",
    editedItemPoint: "",
    editedItemName: "",
    editedItemOutfit: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  mounted() {
    this.initialize();
    this.tpoGet();
    this.outfitGet();
    this.pointIp();
  },
  methods: {
    clearAll() {
      (this.editedItemTpo = ""),
        (this.editedItemPoint = ""),
        (this.editedItemName = ""),
        (this.editedItemOutfit = "");
    },
    outfitGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.id_outfit = response.data;
          console.log(this.id_outfit);
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
    pointIp() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/ip/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.name = response.data;
          console.log(this.name);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/point-list/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.point = response.data;
          console.log(response.status);
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
