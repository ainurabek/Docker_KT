<template>
  <v-dialog v-model="show" max-width="700px">
    <v-card>
      <v-card-title>
        <span class="headline">Создать ЧГ</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" validation>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  class="mt-3"
                  v-model="editedItem.name"
                  dense
                  label="Название"
                ></v-text-field>
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
                  v-model="editedItem.amount_channels"
                  :items="amount_channels"
                  item-text="channels"
                  item-value="channels"
                  dense
                  label="Каналы"
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
              <v-col cols="12" sm="6" md="8">
                <v-text-field
                  class="mt-3"
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
    itemForEdit: {
      type: Array,
      default: function() {
        return [];
      },
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
    outfit: [],
    type_of_trakt: [
      {
        id: 1,
        name: "ПГ",
      },
      {
        id: 2,
        name: "ВГ",
      },
      {
        id: 3,
        name: "ТГ",
      },
      {
        id: 4,
        name: "ЧГ",
      },
      {
        id: 5,
        name: "РГ",
      },
    ],
    amount_channels: [
      { id: 3, channels: "0" },
      { id: 1, channels: "12" },
      { id: 2, channels: "30" },
    ],
    editedItem: {
      name: "",
      tpo1: "",
      point1: "",
      tpo2: "",
      point2: "",
      id_outfit: "",
      trakt: "",
      type_of_trakt: "",
      amount_channels: "",
      comments: "",
      category: "",
      customer: "",
      system: "",
      type_line: "",
      our: "",
      num: "",
    },
    defaultItem: {
      name: "",
      tpo1: "",
      point1: "",
      tpo2: "",
      point2: "",
      id_outfit: "",
      trakt: "",
      type_of_trakt: "",
      amount_channels: "",
      comments: "",
      category: "",
      customer: "",
      system: "",
      type_line: "",
      our: "",
      num: "",
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
  watch: {
    show(newValue) {
      if (newValue) {
        this.idForEdit = this.itemForEdit[0].id;
        console.log(this.itemForEdit, newValue);
      } else {
        console.log(this.itemForEdit, newValue);
      }
    },
  },
  mounted() {
    this.getOutfit();
    this.tpoGet();
    this.pointGet();
    this.customerGet();
    this.type_lineGet();
    this.categoryGet();
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
          console.log(this.itemForEdit);
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
        this.editedItem.COreceive,
        "num",
        this.editedItem.num,
        "system",
        this.editedItem.system,
        "type_of_trakt",
        this.editedItem.type_of_trakt
      );
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/objects/trakt/object-create/${this.idForEdit}/`,
          {
            name: this.editedItem.name,
            tpo1: this.editedItem.tpo1,
            point1: this.editedItem.point1,
            tpo2: this.editedItem.tpo2,
            point2: this.editedItem.point2,
            id_outfit: this.editedItem.id_outfit,
            amount_channels: this.editedItem.amount_channels,
            category: this.editedItem.category,
            comments: this.editedItem.comments,
            customer: this.editedItem.customer,
            our: this.editedItem.our,
          },
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          if (response.status == "201") {
            bus.$emit("updateSPO_TG");
            console.log(response.status);
          }
        })
        .catch((error) => {
          console.log(error.response);
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
