<template>
  <div class="back">
    <v-container>
      <v-card color="white" class="mx-auto">
        <v-card-text>
          <div>
            <span class="fontsiz">Трасса:</span>
            <span class="fontsiz" v-for="item in trassa" :key="item.indexOf"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</span
            >
          </div>
        </v-card-text>
      </v-card>
    </v-container>

    <v-container>
      <v-row>
        <v-col cols="6" md="6">
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
                <v-toolbar-title></v-toolbar-title>
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
                      >Создать ЛП</v-btn
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
                              item-text="channels"
                              item-value="channels"
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
                              :items="id_outfit"
                              item-text="outfit"
                              item-value="id"
                              dense
                              label="Предприятие"
                            ></v-autocomplete>
                          </v-col>
                          <!-- <v-col cols="12" sm="6" md="4">
                              <v-autocomplete
                                v-model="editedItem.trakt_line"
                                :items="trakt_line"
                                item-text="name"
                                item-value="bool"
                                dense
                                
                                label="Линия/Тракт"
                              ></v-autocomplete>
                            </v-col> -->
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
              <v-icon :disabled="isEditing" small @click="deleteItem(item)"
                >mdi-delete</v-icon
              >
            </template>
            <template v-slot:[`item.name`]="{ item }">
              <span @click="editItem(item)" class="pointer">{{
                item.name
              }}</span>
            </template>
            <template v-slot:no-data>
              <v-btn color="primary" @click="initialize">Обновить</v-btn>
            </template>
          </v-data-table>
        </v-col>
        <v-col cols="6" md="6">
          <trakt
            :indexIdLp="indexIdLp"
            @sendIdTrakt="sendIdTraktPar"
            @sendTrassa="sendTrassaPar"
            @sendTypeTrakt="sendTypeTraktPar"
          ></trakt>
        </v-col>

        <template v-if="typeTrakt === 1"></template>
        <template v-if="typeTrakt === 2">
          <v-col cols="6" md="6">
            <PG
              :indexIdTrakt="indexIdTrakt"
              @sendIdPG="sendIdPGPar"
              @sendTrassa="sendTrassaPGPar"
            ></PG>
          </v-col>
        </template>
        <template v-if="typeTrakt === 3">
          <v-col cols="6" md="6">
            <VG
              :indexIdTrakt="indexIdTrakt"
              @sendIdVG_TG="sendIdVGPar"
              @sendTrassa="sendTrassaVGPar"
            ></VG>
          </v-col>
          <v-col cols="6" md="6">
            <PG :indexIdTrakt="indexIdVG_TG" @sendTrassa="sendTrassaPGPar"></PG>
          </v-col>
        </template>
        <template v-if="typeTrakt === 4">
          <v-col cols="6" md="6">
            <TG
              :indexIdTrakt="indexIdTrakt"
              @sendIdTG_CHG="sendIdTGPar"
              @sendTrassa="sendTrassaTGPar"
            ></TG>
          </v-col>

          <v-col cols="6" md="6">
            <VG
              :indexIdTrakt="indexIdTG_CHG"
              @sendIdVG_TG="sendIdVGPar"
              @sendTrassa="sendTrassaVGPar"
            ></VG>
          </v-col>

          <v-col cols="6" md="6">
            <PG :indexIdTrakt="indexIdVG_TG" @sendTrassa="sendTrassaPGPar"></PG>
          </v-col>
        </template>
        <template v-if="typeTrakt === 5">
          <v-col cols="6" md="6">
            <CHG
              :indexIdTrakt="indexIdTrakt"
              @sendIdCHG_RG="sendIdCHGPar"
              @sendTrassa="sendTrassaCHGPar"
            ></CHG>
          </v-col>

          <v-col cols="6" md="6">
            <TG
              :indexIdTrakt="indexIdCHG_RG"
              @sendIdTG_CHG="sendIdTGPar"
              @sendTrassa="sendTrassaTGPar"
            ></TG>
          </v-col>

          <v-col cols="6" md="6">
            <VG
              :indexIdTrakt="indexIdTG_CHG"
              @sendIdVG_TG="sendIdVGPar"
              @sendTrassa="sendTrassaVGPar"
            ></VG>
          </v-col>

          <v-col cols="6" md="6">
            <PG :indexIdTrakt="indexIdVG_TG" @sendTrassa="sendTrassaPGPar"></PG>
          </v-col>
        </template>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import router from "../../router";
import Trakt from "./Trakt";
import PG from "./PG";
import VG from "./VG";
import TG from "./TG";
import CHG from "./CHG";
// import { bus } from "../../main";
// import EditPO from "../EditPO/EditPO"
// import AddTrassa from "../AddTr/AddTrassa"

export default {
  name: "spisokpo",
  components: { Trakt, PG, VG, TG, CHG },
  data: () => ({
    search: "",
    singleSelect: true,
    selected: [],
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
      { text: "ИП от", value: "point1.point" },
      { text: "ИП до", value: "point2.point" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    customer: [],
    id_outfit: [],
    trassa: [],
    selectedRow: null,
    point: [],
    trakt_line: [
      {
        name: "Тракт",
        bool: true,
      },
      {
        name: "Линия",
        bool: false,
      },
    ],
    type_of_location: [],
    type_line: [],
    tpo: [],
    category: [],
    amount_channels: [
      { id: 3, channels: "0" },
      { id: 1, channels: "12" },
      { id: 2, channels: "30" },
    ],
    editedIndex: -1,
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
      COreceive: "",
      amount_channels: "",
      COdeliver: "",
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
      COreceive: "",
      amount_channels: "",
      COdeliver: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
    indexIdLp: "",
    indexIdTrakt: "",
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
      if (newValue != []) {
        this.handleClick();
        this.sendTypeTraktPar();
        if (this.selected[0].trassa == []) {
          this.sendTrassaPar();
          this.sendTrassaPGPar();
          this.sendTrassaVGPar();
          this.sendTrassaTGPar();
          this.sendTrassaCHGPar();
        }
        console.log(this.indexIdCHG_RG);
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
    this.initialize();
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
    cons() {
      console.log(this.indexIdLpForTrassa);
    },
    rowSelect(idx) {
      console.dir(idx);
      this.selectedRow = idx;
    },
    sendIdTraktPar(data) {
      this.indexIdTrakt = data;
    },
    sendIdCHGPar(data) {
      this.indexIdCHG_RG = data;
    },
    sendIdVGPar(data) {
      this.indexIdVG_TG = data;
    },
    sendIdTGPar(data) {
      this.indexIdTG_CHG = data;
    },
    sendIdPGPar(data) {
      this.indexIdPG = data;
    },
    sendTypeTraktPar(data) {
      this.typeTrakt = data;
    },
    sendTrassaPar(data) {
      this.trassa = data;
    },
    sendTrassaPGPar(data) {
      this.trassa = data;
    },
    sendTrassaVGPar(data) {
      this.trassa = data;
    },
    sendTrassaTGPar(data) {
      this.trassa = data;
    },
    sendTrassaCHGPar(data) {
      this.trassa = data;
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
      this.indexIdLp = index;
      this.indexIdLpForTrassa = index;
      this.trassa = this.selected[0].trassa;
      console.log(this.trassa);
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
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/lp/`, {
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
      localStorage.setItem("idPOForEdit", JSON.stringify(item));
      // console.log(JSON.parse(localStorage.getItem("idPOForEdit")))
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      router.push({ name: "editpo" });
    },

    deleteItem(item) {
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(`${this.url.baseUrl}/apps/opu/objects/lp/${index}/`, {
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
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
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
            this.initialize();
            // console.log(response.status);
          }
        })
        .catch((error) => {
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
.back {
  background-color: aliceblue;
}
.fixed {
  position: fixed;
}
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
.custom-highlight-row {
  background-color: pink;
}
.pointer {
  cursor: pointer;
}
</style>
