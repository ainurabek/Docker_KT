<template>
  <v-container>
    <v-data-table
      dense
      :headers="headers"
      :items="desserts"
      class="elevation-1 mt-3"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Форма 5.1</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" dark class="mb-2 ml-4">
            <download-excel
              class="btn btn-default"
              :data="desserts"
              :fields="json_fields"
              worksheet="My Worksheet"
              name="forma51.xls"
            >
              Скачать в excel
            </download-excel>
          </v-btn>

          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
      <template v-slot:[`item.object`]="{ item }">
        <span
          >{{ item.object.point1.name }}-{{ item.object.point1.point }}
          {{ item.object.point2.name }}-{{ item.object.point2.point }}</span
        >
      </template>
      <template v-slot:[`item.trassa`]="{ item }">
        <span v-for="it in item.trassa" :key="it.indexOf"
          >({{ it.point1 }}){{ it.name }}({{ it.point2 }})</span
        >
      </template>
      <template v-slot:[`item.reserve`]="{ item }">
        <span @click="sendIdReserve(item)" class="pointer">{{
          item.reserve
        }}</span>
      </template>
      <template v-slot:[`item.schema`]="{ item }">
        <span @click="imgUrl(item)" class="pointer">{{
          item.object.name
        }}</span>
      </template>
      <template v-slot:[`item.order`]="{ item }">
        <span @click="imgUrlOrd(item)" class="pointer">{{
          item.object.name
        }}</span>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
    <v-dialog persistent v-model="dialogImg">
      <v-card>
        <v-carousel hide-delimiters>
          <v-carousel-item
            v-for="(item, i) in itemsImg"
            :key="i"
            :src="item.src"
            class="imgwww"
          >
            <v-row class="fill-height" align="end" justify="center">
              <v-btn
                @click="deleteImg(item)"
                download
                depressed
                small
                color="primary"
                class="ml-12 mb-2"
                >Удалить</v-btn
              >

              <v-btn
                :href="item.src"
                target="_blank"
                class="ml-8 mb-2"
                download
                depressed
                small
                color="primary"
                >Скачать</v-btn
              >
            </v-row>
          </v-carousel-item>
        </v-carousel>

        <v-btn
          class="ml-8 mb-2 mt-2"
          download
          depressed
          small
          color="primary"
          @click="closeImg"
        >
          Закрыть
        </v-btn>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import router from "../../router";
export default {
  props: { propsRegion: null, propsCustomer: null },
  data: () => ({
    search: "",
    dialog: false,
    selected: [],
    jsonStrTr: [],
    singleSelect: true,
    headers: [
      { text: "КО", value: "object.name" },
      { text: "Участок, ИП Направление", value: "object" },
      {
        text: "Номер потока Трасса прохождение потока",
        value: "trassa",
      },
      { text: "Инд КО", value: "object.category.index" },
      { text: "Номер распоряжения ОУСС", value: "num_ouss" },
      { text: "Резерв потока", value: "reserve" },
      { text: "Примечание (№ID, MH, Аренда)", value: "customer.customer" },
      { text: "Распоряжение", value: "order" },
      { text: "Номер донесения", value: "report_num" },
      { text: "Схема", value: "schema" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    json_fields: {
      КО: "object.name",
      "Участок, ИП Направление": {
        field: "object",
        callback: (value) => {
          return `${value.point1.name}-${value.point1.point}
                             ${value.point2.name}-${value.point2.point}`;
        },
      },
      "Номер потока Трасса прохождение потока": {
        field: "trassa",
        callback: (value) => {
          const jsonStrTr = [];
          for (let i = 0; i < value.length; i++) {
            const elem = `(${value[i].point1})-${value[i].name}-(${value[i].point2})`;
            jsonStrTr.push(elem);
            console.log(jsonStrTr, elem);
          }
          return jsonStrTr.join();
        },
      },
      "Инд КО": "object.category.index",
      "Номер распоряжения ОУСС": "num_ouss",
      "Резерв потока": "reserve",
      "Примечание (№ID, MH, Аренда)": "customer.customer",
      Распоряжение: {
        field: "order_photo",
        callback: (value) => {
          const exHtp = [];
          for (let i = 0; i < value.length; i++) {
            exHtp.push(value[i].src);
          }
          return exHtp.join("  ");
        },
      },
      "Номер донесения": "report_num",
      Схема: {
        field: "schema_photo",
        callback: (value) => {
          const exHtp = [];
          for (let i = 0; i < value.length; i++) {
            exHtp.push(value[i].src);
          }
          return exHtp.join("  ");
        },
      },
    },
    desserts: [],
    trassaFin: [],

    point: [],
    itemsImg: [],
    idForImgDel: "",
    ifOrSc: "",
    imgParams: {
      src2: "",
      src: "",
      name: "",
    },
    dialogImg: false,
    idTrakt: "",
    category: [
      {
        id: 1,
        name: 1,
      },
      {
        id: 2,
        name: 2,
      },
      {
        id: 3,
        name: 3,
      },
      {
        id: 4,
        name: 4,
      },
      {
        id: 5,
        name: 5,
      },
      {
        id: 6,
        name: 6,
      },
      {
        id: 7,
        name: 7,
      },
      {
        id: 8,
        name: 8,
      },
      {
        id: 9,
        name: 9,
      },
      {
        id: 10,
        name: 10,
      },
    ],
    editedIndex: -1,
    editedItem: {
      customer: "",
      num_ouss: "",
      order: "",
      schema: "",
      reserve: "",
      reserve_object: "",
      report_num: "",
    },
    defaultItem: {
      customer: "",
      num_ouss: "",
      order: "",
      schema: "",
      reserve: "",
      reserve_object: "",
      report_num: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
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
    // selected(newValue) {
    //   if (newValue != {}) this.handleClick();
    // }
    propsRegion(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
    propsCustomer(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
  },

  mounted() {
    this.initialize();
  },

  methods: {
    // loading(item) {

    // },

    imgUrl(item) {
      this.ifOrSc = 1;
      this.idForImgDel = item.id;
      this.itemsImg = item.schema_photo;
      this.dialogImg = true;
      console.log(this.idForImgDel);
    },
    imgUrlOrd(item) {
      this.ifOrSc = 2;
      this.idForImgDel = item.id;
      this.itemsImg = item.order_photo;
      this.dialogImg = true;
      console.log(this.idForImgDel);
    },
    closeImg() {
      this.idForImgDel = "";
      this.itemsImg = [];
      this.dialogImg = false;
      console.log(this.itemsImg);
    },
    sendIdReserve(item) {
      router.push({ name: "reservepotoka", params: { date: item } });
    },
    arrayReverseTr() {
      for (let i = 0; i < this.desserts.length; i++) {
        let arrayrReverse = this.desserts[i].object.transit.reverse();
        let arrayTransit12 = [
          ...arrayrReverse,
          ...this.desserts[i].object.transit2,
        ];
        let pushArray = {
          trassa: arrayTransit12,
        };
        let finArray = Object.assign(this.desserts[i], pushArray);
        console.log(finArray, arrayrReverse);
      }
    },
    initialize() {
      let region = this.propsRegion;
      let customer = this.propsCustomer;
      console.log(region, customer);
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/form51/api/?region=${region}&customer=${customer}`,
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          this.desserts = response.data;
          console.log(this.desserts);
          this.arrayReverseTr();
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      router.push({ name: "editdata51", params: { date: item } });
    },
    deleteImg(item) {
      if (this.ifOrSc == 1) {
        this.ifos = "schemaphoto";
      } else if (this.ifOrSc == 2) {
        this.ifos = "orderphoto";
      }
      console.log(item);
      let idPic = item.id;
      let id = this.idForImgDel;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/opu/form51/api/${this.ifos}/delete/${id}/${idPic}/`,
            {
              headers: { Authorization: `Token ${localStorage.token}` },
            }
          )
          .then((response) => {
            if (response.status == "204") {
              this.closeImg();
              this.initialize();
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
    },

    deleteItem(item) {
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(`${this.url.baseUrl}/apps/opu/form51/api/delete/${index}/`, {
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
      if (this.editedIndex > -1) {
        const index = this.desserts[this.editedIndex].id;
        if (this.editedItem.customer.id != undefined) {
          this.editedItem.customer = this.editedItem.customer.id;
        }
        console.log();
        this.$http
          .put(
            `${this.url.baseUrl}/apps/opu/form51/api/update/${index}/`,
            {
              customer: this.editedItem.customer,
              num_ouss: this.editedItem.num_ouss,
              order: this.editedItem.order,
              schema: this.editedItem.schema,
              reserve: this.editedItem.reserve,
              reserve_object: this.editedItem.reserve_object,
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
              this.initialize();
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
      }
      this.close();
    },
  },
};
</script>

<style scoped>
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
.imgwww {
  width: auto;
  height: auto;
}
.pointer {
  cursor: pointer;
}
</style>
