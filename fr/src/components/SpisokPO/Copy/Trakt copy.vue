<template>
  <v-data-table
    dense
    :headers="headers"
    :items="desserts"
    :search="search"
    v-model="selected"
    :single-select="singleSelect"
    item-key="id"
    show-select
    sort-by="calories"
    class="elevation-1"
    height="350px"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>{{ typeTrakt }}</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="650px">
          <template v-slot:activator="{ on }">
            <v-btn
              :disabled="isEditing"
              color="primary"
              dark
              class="mb-2 ml-4"
              v-on="on"
              >Создать Тракт</v-btn
            >
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
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
                      :items="id_outfit"
                      item-text="outfit"
                      item-value="id"
                      dense
                      label="Предприятие"
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.type_of_trakt"
                      :items="type_of_trakt"
                      item-text="name"
                      item-value="id"
                      dense
                      label="Тип тракта"
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
                  <!-- <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.system"
                      :items="system"
                      item-text="name"
                      item-value="id"
                      dense
                      label="Система"
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.num"
                      label="Номер"
                    ></v-text-field>
                  </v-col> -->
                  <v-col cols="12" sm="6" md="12">
                    <v-text-field
                      dense
                      v-model="editedItem.comments"
                      label="Примечание"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
              <v-btn color="blue darken-1" text @click="save">Сохранить</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>

    <template v-slot:[`item.actions`]="{ item }">
      <!-- <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon> -->
      <v-icon :disabled="isEditing" small class="mr-2" @click="deleteItem(item)"
        >mdi-delete</v-icon
      >
      <!-- <v-icon small @click="circuitsTrakt(item)">mdi-arrow-down-drop-circle</v-icon> -->
    </template>
    <template v-slot:[`item.name`]="{ item }">
      <span class="pointer" @click="editItem(item)">{{ item.name }}</span>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Обновить</v-btn>
    </template>
  </v-data-table>
</template>

<script>
import router from "../../router";
// import {bus} from "../../main";
export default {
  name: "trakt",
  props: {
    indexIdLp: null,
  },
  data: () => ({
    search: "",
    selected: [],
    singleSelect: true,
    dialog: false,
    loading: true,
    errored: false,
    isEditing: null,
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1" },
      { text: "ИП до", value: "point2" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    id_outfit: [],
    point: [],
    customer: [],
    trassaFin: [],
    system: [],
    trakt_line: [],
    type_of_location: [],
    type_line: [],
    tpo: [],
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
    category: [],
    editedIndex: -1,
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
      COreceive: "",
      COdeliver: "",
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
      COreceive: "",
      COdeliver: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
    typeTrakt: "",
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Создать тракт" : "Редактировать";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    indexIdLp(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
    selected(newValue) {
      if (newValue != []) {
        this.handleClick();
      }
    },
  },

  mounted() {
    this.userGetSub();
    this.idOutfit();
    this.tpoGet();
    this.pointGet();
    this.customerGet();
    this.type_lineGet();
    this.categoryGet();
    this.type_of_locationGet();
  },

  methods: {
    userGetSub() {
      let user = JSON.parse(localStorage.getItem("user"));
      if (user.subdepartment == 2) {
        this.isEditing = true;
      } else {
        this.isEditing = false;
      }
      console.log(user);
    },
    circuitsTrakt(item) {
      console.log(item.id);
      router.push({ name: "spisokkanalov", params: { date: item.id } });
    },
    arrayReverseTr() {
      for (let i = 0; i <= this.desserts.length; i++) {
        let arrayrReverse = this.desserts[i].transit.reverse();
        let arrayTransit12 = [...arrayrReverse, ...this.desserts[i].transit2];
        let pushArray = {
          trassa: arrayTransit12,
        };
        let finArray = Object.assign(this.desserts[i], pushArray);
        console.log(finArray);
      }
    },
    handleClick() {
      const index = this.selected[0].id;
      this.typeTrakt = this.selected[0].type_of_trakt.name;
      this.$emit("sendTrassa", this.selected[0].trassa);
      this.$emit("sendIdTrakt", index);
      this.$emit("sendTypeTrakt", this.selected[0].type_of_trakt.id);
    },
    type_of_locationGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/type-of-location/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.type_of_location = response.data;
          console.log(this.type_of_location);
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
          console.log(this.category);
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
          console.log(this.type_line);
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
    idOutfit() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.id_outfit = response.data;
          // console.log(this.id_outfit);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    initialize() {
      let id = this.indexIdLp;
      // console.log(id)
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.desserts = response.data;
          this.arrayReverseTr();
          console.log(this.desserts);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem(item) {
      localStorage.setItem("idTraktForEdit", JSON.stringify(item));
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      router.push({ name: "edittrakt" });
    },

    deleteItem(item) {
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/opu/objects/trakt/object-detail/${index}/`,
            { headers: { Authorization: `Token ${localStorage.token}` } }
          )
          .then((response) => {
            if (response.status == "204") {
              this.initialize();
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      let id = this.indexIdLp;
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
          `${this.url.baseUrl}/apps/opu/objects/trakt/object-create/${id}/`,
          {
            name: this.editedItem.name,
            tpo1: this.editedItem.tpo1,
            point1: this.editedItem.point1,
            tpo2: this.editedItem.tpo2,
            point2: this.editedItem.point2,
            id_outfit: this.editedItem.id_outfit,
            type_of_trakt: this.editedItem.type_of_trakt,
            amount_channels: this.editedItem.amount_channels,
            category: this.editedItem.category,
            comments: this.editedItem.comments,
            customer: this.editedItem.customer,
            our: this.editedItem.our,
            // COreceive: this.editedItem.COreceive,
            // COdeliver: this.editedItem.COdeliver,
            // system: this.editedItem.system,
            // num: this.editedItem.num
          },
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          if (response.status == "201") {
            this.initialize();
            console.log(response.status);
          }
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));

      this.close();
    },
  },
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>
