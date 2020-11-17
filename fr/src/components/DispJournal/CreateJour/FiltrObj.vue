<template>
  <div>
    <v-card class="mx-auto backCardCirc pl-4 pr-4 pt-3 pb-3">
      <v-toolbar-title>Список КО</v-toolbar-title>
      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Название"
            v-model="id_object"
            :items="obj"
            item-value="name"
            item-text="name"
          >
          </v-autocomplete>
          <!-- <span>{{editedItemCirc}}</span> -->
        </v-col>
        <v-col cols="12" sm="6" md="2">
          <v-autocomplete
            label="ИП от"
            v-model="point_id"
            :items="ip"
            item-value="id"
            item-text="point"
          >
          </v-autocomplete>
          <!-- <span>{{editedItemCirc}}</span> -->
        </v-col>
        <v-col cols="12" sm="6" md="2">
          <v-autocomplete
            label="ИП до"
            v-model="point_id2"
            :items="ip"
            item-value="id"
            item-text="point"
          >
          </v-autocomplete> </v-col
        ><v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Предприятие"
            v-model="outfit"
            :items="outfitArr"
            item-value="id"
            item-text="outfit"
          >
          </v-autocomplete> </v-col
        ><v-col cols="12" sm="6" md="2">
          <v-autocomplete
            label="Арендатор"
            v-model="customer"
            :items="customerArr"
            item-value="id"
            item-text="abr"
          >
          </v-autocomplete>
        </v-col>
      </v-row>

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
    ip: [],
    obj: [],
    customerArr: [],
    outfitArr: [],
    id_object: "",
    point_id: "",
    point_id2: "",
    customer: "",
    outfit: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  watch: {
    id_object() {
      this.sendPropsObjObj();
    },
    customer() {
      this.sendPropsObjCus();
    },
    point_id() {
      this.sendPropsObjP1();
    },
    point_id2() {
      this.sendPropsObjP2();
    },
    outfit() {
      this.sendPropsObjOut();
    },
  },
  mounted() {
    this.customerGet();
    this.objGet();
    this.pointGet();
    this.outfitGet();
  },
  methods: {
    sendPropsObjObj() {
      bus.$emit("filtr_Obj", this.id_object);
      console.log(this.id_object);
    },
    sendPropsObjCus() {
      bus.$emit("filtr_Cus", this.customer);
      console.log(this.customer);
    },
    sendPropsObjP1() {
      bus.$emit("filtr_P1", this.point_id);
      console.log(this.point_id);
    },
    sendPropsObjP2() {
      bus.$emit("filtr_P2", this.point_id2);
      console.log(this.point_id2);
    },
    sendPropsObjOut() {
      bus.$emit("filtr_Outfit", this.outfit);
      console.log(this.outfit);
    },
    clearAll() {
      this.id_object = "";
      this.point_id = "";
      this.point_id2 = "";
      this.outfit = "";
      this.customer = "";
    },
    customerGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/customer/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.customerArr = response.data;
          console.log(this.customerArr);
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
    pointGet() {
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
    outfitGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.outfitArr = response.data;
          console.log(this.desserts);
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
.backCardCirc {
  background-color: white;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}
</style>
