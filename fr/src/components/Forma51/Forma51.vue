<template>
  <v-container>
    <v-toolbar-title>Список регионов</v-toolbar-title>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-select
          label="Список регионов"
          v-model="editedItemRegions"
          :items="regions"
          item-value="name"
          item-text="name"
        >
          <!-- <template slot='selection' slot-scope='{ item }'>
        {{ item.name }} - {{ item.index }}
      </template>
      <template slot='item' slot-scope='{ item }'>
          {{ item.name }} - {{ item.index }}-->
          <!-- </template> -->
        </v-select>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-select
          label="Арендаторы"
          v-model="editedItemCustomer"
          :items="customer"
          item-value="customer"
          item-text="customer"
        ></v-select>
      </v-col>
    </v-row>
    <v-btn color="primary" class="mr-12" @click="initialize, customerGet"
      >Обновить</v-btn
    >
    <v-btn color="primary" @click="clearAll">Очистить</v-btn>
    <DataTable51
      :propsRegion="editedItemRegions"
      :propsCustomer="editedItemCustomer"
    ></DataTable51>
  </v-container>
</template>

<script>
import DataTable51 from "./DataTable51";
export default {
  components: { DataTable51 },
  data: () => ({
    regions: [],
    customer: [],
    editedItemRegions: "",
    editedItemCustomer: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  mounted() {
    this.initialize();
    this.customerGet();
  },
  methods: {
    clearAll() {
      this.editedItemRegions = "";
      this.editedItemCustomer = "";
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/form51/api/regions/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.regions = response.data;
          console.log(this.regions);
        })
        .catch((error) => {
          console.log(error.response.data);
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
          this.customer = response.data;
          console.log(this.customer);
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
