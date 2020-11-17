<template>
  <div>
    <v-card class="mx-auto backCardCirc pl-4 pr-4 pt-3 pb-3">
      <v-toolbar-title>Список Каналов</v-toolbar-title>
      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="КО"
            v-model="id_object"
            :items="obj"
            item-value="id"
            item-text="name"
          >
          </v-autocomplete>
          <!-- <span>{{editedItemCirc}}</span> -->
        </v-col>
        <v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Арендатор"
            v-model="customer"
            :items="customerArr"
            item-value="id"
            item-text="abr"
          >
          </v-autocomplete> </v-col
        ><v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Название"
            v-model="name"
            :items="circ"
            item-value="name"
            item-text="name"
          >
          </v-autocomplete> </v-col
        ><v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Тип использования"
            v-model="type_using"
            :items="circ"
            item-value="type_using"
            item-text="type_using"
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
    circ: [],
    obj: [],
    customerArr: [],
    id_object: "",
    customer: "",
    name: "",
    type_using: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  watch: {
    id_object() {
      this.sendPropsCircObj();
    },
    customer() {
      this.sendPropsCircCus();
    },
    name() {
      this.sendPropsCircName();
    },
    type_using() {
      this.sendPropsCircTy();
    },
  },
  mounted() {
    this.initialize();
    this.customerGet();
    this.objGet();
  },
  methods: {
    sendPropsCircObj() {
      bus.$emit("editedItemCircObj", this.id_object);
      console.log(this.id_object);
    },
    sendPropsCircName() {
      bus.$emit("editedItemCircName", this.name);
      console.log(this.name);
    },
    sendPropsCircCus() {
      bus.$emit("editedItemCircCus", this.customer);
      console.log(this.customer);
    },
    sendPropsCircTy() {
      bus.$emit("editedItemCircTy", this.type_using);
      console.log(this.type_using);
    },
    clearAll() {
      this.id_object = "";
      this.name = "";
      this.type_using = "";
      this.customer = "";
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/event/circuits/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.circ = response.data;
          console.log(this.circ);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
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
  },
};
</script>

<style scoped>
.backCardCirc {
  background-color: white;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}
</style>
