<template>
  <v-dialog v-model="show" max-width="700px">
    <v-card>
      <v-card-title>
        <span class="headline">Создать ЛП</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" validation>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.name"
                  label="Название"
                  dense
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.category"
                  :items="category"
                  item-text="index"
                  item-value="id"
                  dense
                  label="Категория"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.amount_channels"
                  :items="amount_channels"
                  item-text="name"
                  item-value="id"
                  dense
                  label="Каналы"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.tpo1"
                  :items="tpo"
                  item-text="index"
                  item-value="id"
                  dense
                  label="ТПО 1"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.point1"
                  :items="point"
                  item-text="point"
                  item-value="id"
                  dense
                  label="ИП от"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.tpo2"
                  :items="tpo"
                  item-text="index"
                  item-value="id"
                  dense
                  label="ТПО 2"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.point2"
                  :items="point"
                  item-text="point"
                  item-value="id"
                  dense
                  label="ИП до"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.id_outfit"
                  :items="outfit"
                  item-text="outfit"
                  item-value="id"
                  dense
                  label="Предприятие"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.trakt_line"
                  :items="trakt_line"
                  item-text="name"
                  item-value="bool"
                  dense
                  label="Линия/Тракт"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.type_line"
                  :items="type_line"
                  item-text="name"
                  item-value="id"
                  dense
                  label="Тип линии"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.customer"
                  :items="customer"
                  item-text="customer"
                  item-value="id"
                  dense
                  label="Арендаторы"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="editedItem.our"
                  :items="type_of_location"
                  item-text="name"
                  item-value="id"
                  dense
                  label="Тип принадл-ти"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="12">
                <v-text-field
                  v-model="editedItem.comments"
                  label="Примечание"
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click.stop="close">Отмена</v-btn>
        <v-btn color="blue darken-1" text @click.stop="save">Сохранить</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { bus } from "../../../main";

export default {
  props: {
    value: {
      type: Boolean,
    },
  },
  data: () => ({
    valid: false,
    idForEdit: "",
    type_of_location: [],
    category: [],
    type_line: [],
    customer: [],
    point: [],
    tpo: [],
    trakt_line: [
      {
        name: "Линия",
        bool: false,
      },
      {
        name: "Тракт",
        bool: true,
      },
    ],
    outfit: [],
    amount_channels: [],
    editedItem: {
      name: "",
      tpo1: "",
      point1: "",
      tpo2: "",
      point2: "",
      id_outfit: "",
      point_id: "",
      trakt_line: "",
      type_line: "",
      category: "",
      comments: "",
      customer: "",
      our: "",
      amount_channels: "",
    },
    defaultItem: {
      name: "",
      tpo1: "",
      point1: "",
      tpo2: "",
      point2: "",
      id_outfit: "",
      point_id: "",
      trakt_line: "",
      type_line: "",
      category: "",
      comments: "",
      customer: "",
      our: "",
      amount_channels: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  computed: {
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
  mounted() {
    this.getOutfit();
    this.tpoGet();
    this.pointGet();
    this.customerGet();
    this.type_lineGet();
    this.categoryGet();
    this.getChannels();
    this.type_of_locationGet();
  },
  methods: {
    type_of_locationGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/type-of-location/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.type_of_location = response.data;
          // console.log(this.type_of_location);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    categoryGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/category/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.category = response.data;
          // console.log(this.category);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    type_lineGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/line-type/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.type_line = response.data;
          // console.log(this.type_line);
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
          this.customer = response.data;
          console.log(this.customer);
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
          this.point = response.data;
          // console.log(this.point);
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
          // console.log(this.tpo);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getChannels() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/amount_channel/list/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.amount_channels = response.data;
          console.log(this.amount_channels);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getOutfit() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.outfit = response.data;
          // console.log(this.outfit);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem() {
      this.idForEdit = this.itemForEdit.id;
    },
    save() {
      console.log(
        "name",
        this.editedItem.name,
        "tpo1",
        this.editedItem.tpo1,
        "point1",
        this.editedItem.point1,
        "tpo2",
        this.editedItem.tpo2,
        "point2",
        this.editedItem.point2,
        "id_outfit",
        this.editedItem.id_outfit,
        "point_id",
        this.editedItem.point_id,
        "trakt_line",
        this.editedItem.trakt_line,
        "type_line",
        this.editedItem.type_line,
        "category",
        this.editedItem.category,
        "comments",
        this.editedItem.comments,
        "customer",
        this.editedItem.customer,
        "our",
        this.editedItem.our,
        "COdeliver",
        this.editedItem.COdeliver,
        "COreceive",
        this.editedItem.COreceive
      );
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/objects/lp/create/`,
          {
            name: this.editedItem.name,
            tpo1: this.editedItem.tpo1,
            point1: this.editedItem.point1,
            tpo2: this.editedItem.tpo2,
            point2: this.editedItem.point2,
            id_outfit: this.editedItem.id_outfit,
            point_id: this.editedItem.point_id,
            trakt: this.editedItem.trakt_line,
            type_line: this.editedItem.type_line,
            category: this.editedItem.category,
            amount_channels: this.editedItem.amount_channels,
            comments: this.editedItem.comments,
            customer: this.editedItem.customer,
            our: this.editedItem.our,
          },
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          if (response.status == "201") {
            bus.$emit("updateSPO_LP");
            // console.log(response.status);
          }
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
          this.close();
        });
    },
    close() {
      this.show = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        console.log(this.editedItem);
      });
    },
  },
};
</script>
