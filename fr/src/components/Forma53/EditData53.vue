<template>
  <v-container>
    <v-toolbar-title>Редактирование Форма 5.1</v-toolbar-title>
    <v-row>
      <v-col cols="12" sm="4" md="4">
        <v-autocomplete
          v-model="editedItem.customer"
          :items="customer"
          item-text="customer"
          item-value="id"
          dense
          filled
          label="Арендаторы"
        ></v-autocomplete>
      </v-col>
      <v-col cols="12" sm="4" md="4">
        <v-text-field
          v-model="editedItem.num_ouss"
          dense
          filled
          label="Номер ОУСС"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" md="4">
        <v-text-field
          v-model="editedItem.order"
          dense
          filled
          label="Ордер"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" md="4">
        <v-text-field
          v-model="editedItem.schema"
          dense
          filled
          label="Схема"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" md="4">
        <v-text-field
          v-model="editedItem.reserve"
          dense
          filled
          label="Резерв"
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="4" md="4">
        <v-text-field
          v-model="editedItem.report_num"
          dense
          filled
          label="Номер донесения"
        ></v-text-field>
      </v-col>
    </v-row>
    <hr />
    <v-toolbar-title>Резерв объектов</v-toolbar-title>
    <v-row>
      <v-col>
        <FirstEdit @sendIdFirst="firstId"></FirstEdit>
      </v-col>
      <v-col>
        <SecondEdit @sendIdSecond="secondId"></SecondEdit>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center">
      <v-btn color="primary" class="mr-12 mt-6" @click="editData51"
        >Сохранить</v-btn
      >
    </v-row>
  </v-container>
</template>

<script>
import router from "../../router";
import SecondEdit from "./SecondEdit";
import FirstEdit from "./FirstEdit";
export default {
  props: ["date"],
  components: { SecondEdit, FirstEdit },
  data() {
    return {
      desserts: [],
      trakt: [],
      PG: [],
      VG: [],
      TG: [],
      CHG: [],
      customer: [],
      url: {
        baseUrl: "http://0.0.0.0:8000",
      },
      idLPForTrassa: "",
      idLP: "",
      editedItemIdLp: "",
      editedItemIdTrakt: "",
      editedItemIdPG: "",
      editedItemIdVG: "",
      editedItemIdTG: "",
      editedItemIdCHG: "",
      idTrassaSend: "",
      firstIdData: "",
      secondIdData: "",
      editedItem: {
        customer: null,
        num_ouss: null,
        order: null,
        schema: null,
        reserve: null,
        report_num: null,
      },
    };
  },
  watch: {},
  mounted() {
    this.customerGet();
    this.editIt();
  },
  methods: {
    editIt() {
      this.editedItem = Object.assign({}, this.date);
      console.log(this.date);
    },
    firstId(data) {
      this.firstIdData = data;
    },
    secondId(data) {
      this.secondIdData = data;
    },
    editDate() {
      this.editedItem.num_ouss = this.date.num_ouss;
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

    editData51() {
      if (this.editedItem.order == "") {
        this.editedItem.order = null;
      }
      // } else if (this.editedItem.order.id != undefined) {
      //   this.editedItem.order = this.editedItem.order.id;
      // }
      if (this.editedItem.schema == "") {
        this.editedItem.schema = null;
      }
      // else if (this.editedItem.tpo1.id != undefined) {
      //   this.editedItem.tpo1 = this.editedItem.tpo1.id;
      // }
      if (this.editedItem.customer == "") {
        this.editedItem.customer = null;
      }
      console.log(this.date);
      console.log(
        this.editedItem.customer,
        this.editedItem.num_ouss,
        this.editedItem.order,
        this.editedItem.schema,
        this.editedItem.reserve,
        this.editedItem.report_num,
        [this.firstIdData, this.secondIdData]
      );
      this.$http
        .put(
          `${this.url.baseUrl}/apps/opu/form51/api/update/${this.date.id}/`,
          {
            customer: this.editedItem.customer,
            num_ouss: this.editedItem.num_ouss,
            order: this.editedItem.order,
            schema: this.editedItem.schema,
            reserve: this.editedItem.reserve,
            reserve_object: [this.firstIdData, this.secondIdData],
            report_num: this.editedItem.report_num,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == "200") {
            router.push({ name: "forma51" });
          }
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
.back {
  background-color: aliceblue;
}
</style>
