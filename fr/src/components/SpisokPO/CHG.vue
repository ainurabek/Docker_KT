<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    :search="search"
    v-model="selected"
    :single-select="singleSelect"
    item-key="id"
    show-select
    sort-by="calories"
    class="elevation-1"
    dense
    height="200px"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>{{ typeOfTrakt }}</v-toolbar-title>
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
              @click="copyItem"
              >Создать</v-btn
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
                      :items="id_outfit"
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
                      item-text="name"
                      item-value="id"
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
export default {
  name: "pg",
  props: {
    indexIdTrakt: null,
  },
  data: () => ({
    selected: [],
    singleSelect: true,
    search: "",
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
    trassaFin: [],
    customer: [],
    system: [],
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
    amount_channels: [],
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
    typeOfTrakt: "",
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Создать" : "Редактировать";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    indexIdTrakt(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
    selected(newValue) {
      if (newValue != {}) this.handleClick();
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
    this.getChannels();
    this.type_of_locationGet();
    this.initialize();
  },

  methods: {
    copyItem() {
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/object-detail/${this.indexIdTrakt}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.editedItem = Object.assign({}, response.data);
          console.log(this.editedItem);
          console.log(this.response.data);
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
      this.$emit("sendIdCHG_RG", index);
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
      let id = this.indexIdTrakt;
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
      router.push({ name: "editpgitd", params: { date: item } });
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
      let id = this.indexIdTrakt;
      if (this.editedItem.amount_channels == undefined) {
        this.editedItem.amount_channels = "";
      } else if (this.editedItem.amount_channels.id != undefined) {
        this.editedItem.amount_channels = this.editedItem.amount_channels.id;
      }
      if (this.editedItem.id_outfit == undefined) {
        this.editedItem.id_outfit = "";
      } else if (this.editedItem.id_outfit.id != undefined) {
        this.editedItem.id_outfit = this.editedItem.id_outfit.id;
      }
      if (this.editedItem.tpo1 == undefined) {
        this.editedItem.tpo1 = "";
      } else if (this.editedItem.tpo1.id != undefined) {
        this.editedItem.tpo1 = this.editedItem.tpo1.id;
      }
      if (this.editedItem.tpo2 == undefined) {
        this.editedItem.tpo2 = "";
      } else if (this.editedItem.tpo2.id != undefined) {
        this.editedItem.tpo2 = this.editedItem.tpo2.id;
      }
      if (this.editedItem.point1 == undefined) {
        this.editedItem.point1 = "";
      } else if (this.editedItem.point1.id != undefined) {
        this.editedItem.point1 = this.editedItem.point1.id;
      }
      if (this.editedItem.point2 == undefined) {
        this.editedItem.point2 = "";
      } else if (this.editedItem.point2.id != undefined) {
        this.editedItem.point2 = this.editedItem.point2.id;
      }
      if (this.editedItem.type_line == undefined) {
        this.editedItem.type_line = "";
      } else if (this.editedItem.type_line.id != undefined) {
        this.editedItem.type_line = this.editedItem.type_line.id;
      }
      if (this.editedItem.category == undefined) {
        this.editedItem.category = "";
      } else if (this.editedItem.category.id != undefined) {
        this.editedItem.category = this.editedItem.category.id;
      }
      if (this.editedItem.our == undefined) {
        this.editedItem.our = "";
      } else if (this.editedItem.our.id != undefined) {
        this.editedItem.our = this.editedItem.our.id;
      }
      if (this.editedItem.customer == undefined) {
        this.editedItem.customer = "";
      } else if (this.editedItem.customer.id != undefined) {
        this.editedItem.customer = this.editedItem.customer.id;
      }
      if (this.editedItem.type_of_trakt == undefined) {
        this.editedItem.type_of_trakt = "";
      } else if (this.editedItem.type_of_trakt.id != undefined) {
        this.editedItem.type_of_trakt = this.editedItem.type_of_trakt.id;
      }
      if (this.editedItem.system == undefined) {
        this.editedItem.system = "";
      } else if (this.editedItem.system.id != undefined) {
        this.editedItem.system = this.editedItem.system.id;
      }
      if (this.editedItem.trakt_line == undefined) {
        this.editedItem.trakt_line = "";
      } else if (this.editedItem.trakt_line.id != undefined) {
        this.editedItem.trakt_line = this.editedItem.trakt_line.id;
      }
      if (this.editedItem.point_id == undefined) {
        this.editedItem.point_id = "";
      } else if (this.editedItem.point_id.id != undefined) {
        this.editedItem.point_id = this.editedItem.point_id.id;
      }
      if (this.editedItem.comments == null) {
        this.editedItem.comments = "";
      }
      if (this.editedItem.COreceive == null) {
        this.editedItem.COreceive = "";
      }
      if (this.editedItem.COdeliver == undefined) {
        this.editedItem.COdeliver = "";
      }
      console.log(id);
      console.log(
        this.editedItem.name,
        this.editedItem.tpo1,
        this.editedItem.point1,
        this.editedItem.tpo2,
        this.editedItem.point2,
        this.editedItem.ammount_channels
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
            this.initialize();
            console.log(response.status);
          }
        })
        .catch((error) => {
          // alert("ошибка", error.response.status);
          console.log(error.response.data);
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
