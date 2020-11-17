<template>
  <v-container>
    <v-toolbar-title>Редактирование Форма 5.1</v-toolbar-title>
    <v-row>
      <v-col cols="12" sm="4" md="3">
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
      <v-col cols="12" sm="4" md="3">
        <v-text-field
          v-model="editedItem.num_ouss"
          dense
          filled
          label="Номер ОУСС"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" md="3">
        <v-file-input
          label="Ордер"
          filled
          ref="files2"
          multiple
          v-on:change="handleFileUpload2()"
          prepend-icon="mdi-camera"
        ></v-file-input>
      </v-col>
      <v-col cols="12" sm="4" md="3">
        <v-file-input
          ref="files"
          v-on:change="handleFileUpload()"
          prepend-icon="mdi-camera"
          label="Схема"
          multiple
          filled
        ></v-file-input>
      </v-col>
      <v-col cols="12" sm="4" md="3">
        <v-text-field
          v-model="editedItem.reserve"
          dense
          filled
          label="Резерв"
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="4" md="3">
        <v-text-field
          v-model="editedItem.report_num"
          dense
          filled
          label="Номер донесения"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="4" md="3">
        <v-btn color="blue" dark :loading="loading" @click="orderSave"
          >Сохранить ордер</v-btn
        >
      </v-col>
      <v-col cols="12" sm="4" md="3">
        <v-btn color="blue" dark :loading="loading2" @click="schemaSave"
          >Сохранить схему</v-btn
        >
      </v-col>
    </v-row>
    <hr />
    <v-toolbar-title>Резерв объектов</v-toolbar-title>
    <v-row justify="center">
      <v-col cols="12" sm="4" md="4">
        <v-card class="mt-4 backCard51">
          <v-card-text>
            <span class="fontsiz" v-for="it in nameArr" :key="it.indexOf"
              >{{ it }},</span
            >
          </v-card-text>
        </v-card>
        <v-btn color="primary" class="mr-12 mt-6" @click="clearNameArr"
          >Очистить</v-btn
        >
      </v-col>
      <v-col cols="12" sm="4" md="2"> </v-col>
      <v-col cols="12" sm="4" md="4">
        <FirstEdit @sendIdFirst="firstId" @sendIdName="firstName"></FirstEdit>
      </v-col>
    </v-row>
    <hr />
    <v-row justify="center">
      <v-btn color="green" dark class="mr-12 mt-6" @click="pushArray"
        >Добавить резерв</v-btn
      >
      <v-btn color="green" dark class="mr-12 mt-6" @click="submitFile"
        >Сохранить</v-btn
      >
    </v-row>
  </v-container>
</template>

<script>
import FirstEdit from "./FirstEdit";
import router from "../../router";
export default {
  props: ["date"],
  components: { FirstEdit },
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
      loading: false,
      loading2: false,
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
      firstNameData: "",
      arrayReserveObj: [],
      nameArr: [],
      nullArr: [],
      files: "",
      files2: "",
      editedItem: {
        customer: null,
        num_ouss: null,
        order: "",
        schema: "",
        reserve: null,
        report_num: null,
        reserve_object: "",
      },
    };
  },
  watch: {},
  mounted() {
    this.customerGet();
    this.editIt();
    console.log(this.date.id);
  },
  methods: {
    clearNameArr() {
      this.nameArr = [];
      this.arrayReserveObj = [];
      console.log(this.arrayReserveObj);
    },
    editIt() {
      this.editedItem = Object.assign({}, this.date);
      for (let i = 0; i < this.date.reserve_object.length; i++) {
        this.nameArr.push(this.date.reserve_object[i].name);
        this.arrayReserveObj.push(this.date.reserve_object[i].id);
      }
      console.log(this.date);
    },
    firstId(data) {
      this.firstIdData = data;
    },
    firstName(data) {
      this.firstNameData = data;
    },
    editDate() {
      this.editedItem.num_ouss = this.date.num_ouss;
    },
    pushArray() {
      if (this.firstIdData != "") {
        let b = this.firstNameData;
        let a = this.firstIdData;
        this.arrayReserveObj.push(a);
        this.nameArr.push(b);
      }
      console.log(this.arrayReserveObj, this.nameArr);
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
    schemaSave() {
      this.loading2 = true;
      let formData = new FormData();
      if (this.files.length > 0) {
        for (let i = 0; i < this.files.length; i++) {
          let file = this.files[i];
          formData.append(`schema`, file);
        }
      }
      let id = this.date.id;
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/form51/api/schemaphoto/create/${id}/`,
          formData,
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            this.files = "";
            this.loading2 = false;
            alert("Схема успешно сохранена");
            console.log(response.status);
          }
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    orderSave() {
      this.loading = true;
      let formData = new FormData();
      if (this.files2.length > 0) {
        for (let i = 0; i < this.files2.length; i++) {
          let file = this.files2[i];
          formData.append(`order`, file);
        }
      }
      let id = this.date.id;
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/form51/api/orderphoto/create/${id}/`,
          formData,
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            this.files2 = "";
            this.loading = false;
            alert("Ордер успешно сохранен");
            console.log(response.status);
          }
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    submitFile() {
      if (this.editedItem.customer.id != undefined) {
        this.editedItem.customer = this.editedItem.customer.id;
      }
      let id = this.date.id;
      console.log(this.editedItem.customer);
      this.$http
        .put(
          `${this.url.baseUrl}/apps/opu/form51/api/update/${id}/`,
          {
            reserve_object: this.arrayReserveObj,
            customer: this.editedItem.customer,
            report_num: this.editedItem.report_num,
            reserve: this.editedItem.reserve,
            num_ouss: this.editedItem.num_ouss,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
              // "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.status);
          router.push({ name: "forma51" });
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    handleFileUpload2() {
      this.files2 = this.$refs.files2.lazyValue;
      console.log(this.files2);
    },

    handleFileUpload() {
      this.files = this.$refs.files.lazyValue;
      console.log(this.files);
    },
  },
};
</script>

<style scoped>
.backCard51 {
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
.back {
  background-color: aliceblue;
}
</style>
