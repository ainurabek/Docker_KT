<template>
  <v-container>
    <v-toolbar-title>Форма Арендаторов</v-toolbar-title>
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <v-select
          label="Список арендаторов"
          v-model="editedItemCustomer"
          :items="desserts"
          item-value="id"
          item-text="abr"
        >
          <template slot="selection" slot-scope="{ item }">
            {{ item.abr }} - {{ item.customer }}
          </template>
          <template slot="item" slot-scope="{ item }">
            {{ item.abr }} - {{ item.customer }}
          </template>
        </v-select>
      </v-col>

      <v-btn color="primary" class="ml-12 mt-12" @click="objectRout"
        >Объекты</v-btn
      >

      <v-btn color="primary" class="ml-12 mt-12" @click="circuitRout"
        >Каналы</v-btn
      >
    </v-row>
    <v-btn color="primary" class="mr-12" @click="initialize">Обновить</v-btn>

    <v-btn color="primary" @click="clearAll">Очистить</v-btn>

    <GetAllCust
      :editedItemCustomerProps="editedItemCustomer"
      :propsFromCircuit="date"
    ></GetAllCust>
  </v-container>
</template>

<script>
import router from "../../router";
import GetAllCust from "./GetAllCust";
export default {
  components: { GetAllCust },
  props: ["date"],
  data: () => ({
    search: "",
    dialog: false,
    loading: true,
    errored: false,
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Аббревиатура", value: "abr" },
      { text: "Арендатор", value: "customer" },
    ],
    desserts: [],
    editedItemCustomer: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    // date(newValue) {
    //   if (newValue != {}) {
    //     this.date = this.editedItemCustomer
    //   }
    // }
  },

  mounted() {
    this.initialize();
  },

  methods: {
    objectRout() {
      router.push({
        name: "objectfiltra",
        params: { date: this.editedItemCustomer },
      });
    },
    circuitRout() {
      router.push({
        name: "circuitfiltra",
        params: { date: this.editedItemCustomer },
      });
    },

    clearAll() {
      this.editedItemCustomer = "";
    },
    chooseAbr(item) {
      router.push({ name: "", params: { date: item } });
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/form_customer/api/customers/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.desserts = response.data;
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
.pointer {
  cursor: pointer;
}
</style>
