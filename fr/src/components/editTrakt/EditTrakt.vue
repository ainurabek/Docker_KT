<template>
  <div>
    <v-container>
      <v-card color="white" class="mx-auto mb-4">
        <v-card-text>
          <div>
            <span class="fontsiz">Трасса:</span>
            <span class="fontsiz" v-for="item in trassa" :key="item.id"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</span
            >
          </div>
        </v-card-text>
      </v-card>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          Тракт
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="3">
                <v-text-field
                  class="mt-2"
                  v-model="editedItem.name"
                  label="Название"
                  dense
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.category"
                  :items="category"
                  item-text="index"
                  item-value="id"
                  dense
                  label="Категория"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.tpo1"
                  :items="tpo"
                  item-text="index"
                  item-value="id"
                  dense
                  label="ТПО 1"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.point1"
                  :items="point"
                  item-text="point"
                  item-value="id"
                  dense
                  label="ИП от"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.tpo2"
                  :items="tpo"
                  item-text="index"
                  item-value="id"
                  dense
                  label="ТПО 2"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.point2"
                  :items="point"
                  item-text="point"
                  item-value="id"
                  dense
                  label="ИП до"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.id_outfit"
                  :items="id_outfit"
                  item-text="outfit"
                  item-value="id"
                  dense
                  label="Предприятие"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.our"
                  :items="type_of_location"
                  item-text="name"
                  item-value="id"
                  dense
                  label="Тип принадлежности"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.type_of_trakt"
                  :items="type_of_trakt"
                  item-text="name"
                  item-value="id"
                  dense
                  label="Тип тракта"
                ></v-autocomplete>
              </v-col>
              <!-- <v-col cols="12" sm="6" md="3">
              <v-autocomplete
                v-model="editedItem.trakt_line"
                :items="trakt_line"
                item-text="name"
                item-value="bool"
                dense
                label="Линия/Тракт"
              ></v-autocomplete>
            </v-col> -->
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.type_line"
                  :items="type_line"
                  item-text="name"
                  item-value="id"
                  dense
                  label="Тип линии"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-autocomplete
                  v-model="editedItem.customer"
                  :items="customer"
                  item-text="customer"
                  item-value="id"
                  dense
                  label="Арендаторы"
                ></v-autocomplete>
              </v-col>

              <v-col cols="12" sm="6" md="3">
                <v-text-field
                  v-model="editedItem.amount_channels.value"
                  label="Кол-во каналов объекта"
                  dense
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-text-field
                  v-model="editedItem.total_amount_channels"
                  label="Общее кол-во каналов"
                  dense
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="3">
                <v-text-field
                  v-model="editedItem.total_amount_active_channels"
                  label="Кол-во активированных каналов"
                  dense
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field
                  class="mt-1"
                  v-model="editedItem.comments"
                  label="Примечание"
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" class=" ml-4" @click="circuitsGo"
            >Каналы</v-btn
          >
          <v-btn
            :disabled="isEditing"
            :loading="!loadingEd"
            @click="editSave"
            color="primary"
            dark
            class="ml-4"
          >
            Сохранить
          </v-btn>
          <v-btn color="blue darken-1" text @click="closeEdit">Назад</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
    <v-container>
      <v-data-table
        calculate-widths
        :headers="headers"
        :items="ip_object"
        hide-default-footer
        class="editpoback padd mt-4"
        :search="search"
        sort-by="calories"
      >
        <template v-slot:top>
          <v-toolbar flat color="white">
            <v-toolbar-title>ИП</v-toolbar-title>
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
                  class="mb-2"
                  v-on="on"
                  >Создать ИП</v-btn
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
                        <v-select
                          label="ТПО, Индекс"
                          v-model="editedItemIp.tpo_id"
                          :items="tpo"
                          item-value="id"
                          item-text="name"
                          dense
                        >
                          <template slot="selection" slot-scope="{ item }">
                            {{ item.name }} - {{ item.index }}
                          </template>
                          <template slot="item" slot-scope="{ item }">
                            {{ item.name }} - {{ item.index }}
                          </template>
                        </v-select>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-autocomplete
                          v-model="editedItemIp.point_id"
                          :items="point"
                          item-text="point"
                          item-value="id"
                          dense
                          label="ИП"
                        ></v-autocomplete>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="close"
                    >Отмена</v-btn
                  >
                  <v-btn color="blue darken-1" text @click="save"
                    >Сохранить</v-btn
                  >
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>

        <template v-slot:[`item.actions`]="{ item }">
          <v-icon :disabled="isEditing" small="" @click="deleteItem(item)"
            >mdi-delete</v-icon
          >
        </template>
        <template v-slot:no-data>
          <v-btn color="primary" @click="initialize">Обновить</v-btn>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
import router from "../../router";
export default {
  props: ["date"],
  data: () => ({
    search: "",
    singleSelect: true,
    selected: [],
    dialog: false,
    loading: true,
    loadingEd: true,
    errored: false,
    isEditing: null,
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "ИП", value: "point_id" },
      { text: "ТПО", value: "tpo_id" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    customer: [],
    id_outfit: [],
    trassa: [],
    ip_object: [],
    selectedRow: null,
    point: [],
    system: [],
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
    tpo: [],
    type_of_location: [],
    type_line: [],
    category: [],
    editedItemIp: {
      tpo_id: "",
      point_id: "",
    },
    editedIndex: -1,
    editedItem: {
      name: "",
      tpo1: "",
      point1: "",
      tpo2: "",
      point2: "",
      id_outfit: "",
      trakt_line: "",
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
      trakt_line: "",
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
    indexIdLp: "",
    indexIdTrakt: "",
    idTraktForEdit: "",
    typeTrakt: "",
    indexIdPG: "",
    indexIdVG_TG: "",
    indexIdTG_CHG: "",
    indexIdCHG_RG: "",
    indexIdLpForTrassa: "",
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Создать ЛП" : "Редактировать";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
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
    this.type_of_locationGet();
    this.initialize();
  },

  methods: {
    userGetSub() {
      this.idTraktForEdit = JSON.parse(
        localStorage.getItem("idTraktForEdit")
      ).id;
      let user = JSON.parse(localStorage.getItem("user"));
      if (user.subdepartment == 2) {
        this.isEditing = true;
      } else {
        this.isEditing = false;
      }
      console.log(user);
    },
    arrayTrassa() {
      let arrayReverse = this.desserts.transit.reverse();
      let arrayFin = [...arrayReverse, ...this.desserts.transit2];
      this.trassa = arrayFin;
      console.log(this.trassa);
    },

    circuitsGo() {
      router.push({
        name: "spisokkanalov",
        params: { date: this.desserts.id },
      });
    },
    cons() {
      console.log(this.indexIdLpForTrassa);
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
          console.log(this.point);
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
          console.log(this.tpo);
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
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/object-detail/${this.idTraktForEdit}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.desserts = response.data;
          this.ip_object = response.data.ip_object;
          this.arrayTrassa();
          this.editItem();
          console.log(this.desserts);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem() {
      this.editedItem = Object.assign({}, this.desserts);
      console.log(this.editedItem);
    },
    deleteItem(item) {
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(`${this.url.baseUrl}/apps/opu/objects/ip/delete/${index}/`, {
            headers: { Authorization: `Token ${localStorage.token}` },
          })
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
        this.editedItemIp = Object.assign({}, this.defaultItemIp);
        this.editedIndex = -1;
      });
    },
    closeEdit() {
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
      });
      router.push({
        name: "spisokpo",
      });
    },
    save() {
      const index = this.desserts.id;
      // if (this.editedItemIp.tpo_id.id != undefined) {
      //   this.editedItemIp.tpo_id = this.editedItemIp.tpo_id.id;
      // }
      // if (this.editedItemIp.point_id.id != undefined) {
      //   this.editedItemIp.point_id = this.editedItem.point2.id;
      // }
      console.log(this.editedItemIp.tpo_id, this.editedItemIp.point_id);
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/objects/ip/create/${index}/`,
          {
            tpo_id: this.editedItemIp.tpo_id,
            point_id: this.editedItemIp.point_id,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == "201") {
            this.initialize();
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      this.close();
    },
    editSave() {
      const index = this.desserts.id;
      this.loadingEd = false;
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
      console.log(
        // "name",this.editedItem.name
        //    "tpo1", this.editedItem.tpo1,
        //    "point1", this.editedItem.point1,
        //    "tpo2", this.editedItem.tpo2,
        //    "point2", this.editedItem.point2,
        //    "id_outfit", this.editedItem.id_outfit,
        //    "point_id", this.editedItem.point_id,
        //    "trakt_line", this.editedItem.trakt_line,
        "type_line",
        this.editedItem.type_line
        //    "category", this.editedItem.category,
        //    "comments", this.editedItem.comments,
        //    "customer", this.editedItem.customer,
        //    "our", this.editedItem.our,
        //    "COdeliver", this.editedItem.COdeliver,
        //    "COreceive", this.editedItem.COreceive,
        //   "system",
        //   this.editedItem.system
      );
      this.$http
        .put(
          `${this.url.baseUrl}/apps/opu/objects/trakt/object-edit/${index}/`,
          {
            name: this.editedItem.name,
            tpo1: this.editedItem.tpo1,
            point1: this.editedItem.point1,
            tpo2: this.editedItem.tpo2,
            point2: this.editedItem.point2,
            id_outfit: this.editedItem.id_outfit,
            type_of_trakt: this.editedItem.type_of_trakt,
            category: this.editedItem.category,
            comments: this.editedItem.comments,
            customer: this.editedItem.customer,
            our: this.editedItem.our,
            // COreceive: this.editedItem.COreceive,
            // COdeliver: this.editedItem.COdeliver,
            // trakt: this.editedItem.trakt_line,
            // type_line: this.editedItem.type_line,
            // system: this.editedItem.system,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == "200") {
            this.initialize();
            this.loadingEd = true;
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>

<style scoped>
.padd {
  padding: 10px;
}
.editpoback {
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.hrline {
  margin-top: 5px;
  margin-bottom: 5px;
}
.fontheader {
  font-size: 16px;
  /* margin-left: 8px;
  margin-right: 10px; */
  color: darkcyan;
}
.back {
  background-color: aliceblue;
}
.fixed {
  position: fixed;
}
.fontsiz {
  font-size: 16px;
  margin-right: 8px;
  color: black;
}
.custom-highlight-row {
  background-color: pink;
}
.pointer {
  cursor: pointer;
}
</style>
