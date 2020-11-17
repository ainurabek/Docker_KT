<template>
  <div>
    <v-card class="mx-auto backCardIP pl-4 pr-4 pt-3 pb-3">
      <v-toolbar-title>Список ИП</v-toolbar-title>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-autocomplete
            label="ИП"
            v-model="point_id"
            :items="ip"
            item-value="point"
            item-text="point"
          >
          </v-autocomplete>
        </v-col>
        <v-col cols="12" sm="6" md="4">
          <v-autocomplete
            label="Название"
            v-model="object_id"
            :items="ip"
            item-value="name"
            item-text="name"
          >
          </v-autocomplete>
        </v-col>
      </v-row>
      <!-- <v-btn color="primary" class="mr-12 mb-2" @click="initialize"
      >Обновить</v-btn
    > -->
      <v-btn color="primary" class="mr-12 mb-2" @click="clearAll"
        >Очистить</v-btn
      >
    </v-card>
  </div>
</template>

<script>
import { bus } from "../../../main";
export default {
  data: () => ({
    obj: [],
    ip: [],
    object_id: "",
    point_id: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  watch: {
    object_id() {
      this.sendPropsIPObj();
    },
    point_id() {
      this.sendPropsIPPoint();
    },
  },
  mounted() {
    this.initialize();
    this.objGet();
  },
  methods: {
    sendPropsIPObj() {
      bus.$emit("object_idIP", this.object_id);
      console.log(this.object_id);
    },
    sendPropsIPPoint() {
      bus.$emit("point_idIP", this.point_id);
      console.log(this.point_id);
    },
    clearAll() {
      this.point_id = "";
      this.object_id = "";
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/point/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.ip = response.data;
          console.log(this.ip);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    objGet() {
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

<style scoped>
.backCardIP {
  background-color: white;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}
</style>
