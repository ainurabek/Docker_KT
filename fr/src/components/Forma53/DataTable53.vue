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
          <v-toolbar-title>Форма 5.3</v-toolbar-title>
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
              name="forma53.xls"
            >
              Скачать в excel
            </download-excel>
          </v-btn>

          <v-dialog v-model="dialog" max-width="650px">
            <v-card>
              <v-card-title>
                <span class="headline">Редактировать</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="4" md="4">
                      <v-file-input
                        label="Ордер"
                        ref="files2"
                        multiple
                        v-on:change="handleFileUpload2()"
                        prepend-icon="mdi-camera"
                      ></v-file-input>
                    </v-col>
                    <v-col cols="12" sm="4" md="4">
                      <v-file-input
                        ref="files"
                        v-on:change="handleFileUpload()"
                        prepend-icon="mdi-camera"
                        label="Схема"
                        multiple
                      ></v-file-input>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.comments"
                        label="Комментарии"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-btn
                        color="blue"
                        dark
                        :loading="loading"
                        @click="orderSave"
                        >Сохранить ордер</v-btn
                      >
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-btn
                        color="blue"
                        dark
                        :loading="loading2"
                        @click="schemaSave"
                        >Сохранить схему</v-btn
                      >
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
                <v-btn color="blue darken-1" text @click="save"
                  >Сохранить</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
      <template v-slot:[`item.circuit`]="{ item }">
        <span
          >{{ item.circuit.point1.name }}-{{ item.circuit.point1.point }}
          {{ item.circuit.point2.name }}-{{ item.circuit.point2.point }}</span
        >
      </template>
      <template v-slot:[`item.trassa`]="{ item }">
        <span v-for="it in item.trassa" :key="it.indexOf"
          >({{ it.point1 }}){{ it.name }}({{ it.point2 }})</span
        >
      </template>
      <template v-slot:[`item.schema`]="{ item }">
        <span @click="imgUrl(item)" class="pointer">{{
          item.circuit.name
        }}</span>
      </template>
      <template v-slot:[`item.order`]="{ item }">
        <span @click="imgUrlOrd(item)" class="pointer">{{
          item.circuit.name
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
    singleSelect: true,
    loading: false,
    loading2: false,
    headers: [
      { text: "Номер канала", value: "circuit.num_circuit" },
      { text: "Название", value: "circuit.name" },
      { text: "Участок, ИП Направление", value: "circuit" },
      {
        text: "Трасса прохождение потока",
        value: "trassa",
      },
      { text: "Арендатор", value: "circuit.customer.customer" },
      { text: "Категория", value: "circuit.category.index" },
      { text: "№ приказа потока", value: "circuit.num_order" },
      { text: "Дата приказа", value: "circuit.date_order" },

      { text: "Распоряжение", value: "order" },
      { text: "Схема", value: "schema" },
      { text: "Примечание", value: "circuit.adding" },
      { text: "Комментарии", value: "comments" },
      { text: "Дата создания", value: "date" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    json_fields: {
      "Номер канала": "circuit.num_circuit",
      Название: "circuit.name",
      "Участок, ИП Направление": {
        field: "circuit",
        callback: (value) => {
          return `${value.point1.name}-${value.point1.point}
                             ${value.point2.name}-${value.point2.point}`;
        },
      },
      "Трасса прохождение потока": {
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
      Арендатор: "circuit.customer.customer",
      Категория: "circuit.category.index",
      "№ приказа потока": "circuit.num_order",
      "Дата приказа": "circuit.date_order",
      Распоряжение: {
        field: "order53_photo",
        callback: (value) => {
          const exHtp = [];
          for (let i = 0; i < value.length; i++) {
            exHtp.push(value[i].src);
          }
          return exHtp.join("  ");
        },
      },
      Схема: {
        field: "schema53_photo",
        callback: (value) => {
          const exHtp = [];
          for (let i = 0; i < value.length; i++) {
            exHtp.push(value[i].src);
          }
          return exHtp.join("  ");
        },
      },
      Примечание: "circuit.adding",
      Комментарии: "comments",
      "Дата создания": "date",
    },
    desserts: [],
    trassaFin: [],
    itemsImg: [],
    idForImgDel: "",
    ifOrSc: "",
    point: [],
    dialogImg: false,
    files: "",
    files2: "",
    imgParams: {
      src: "",
      name: "",
    },
    idTrakt: "",
    category: [
      { id: 1 },
      { id: 2 },
      { id: 3 },
      { id: 4 },
      { id: 5 },
      { id: 6 },
      { id: 7 },
      { id: 8 },
      { id: 9 },
    ],
    editedIndex: -1,
    editedItem: {
      schema: null,
      order: null,
      comments: "",
    },
    defaultItem: {
      schema: null,
      order: null,
      comments: "",
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
    imgUrl(item) {
      this.ifOrSc = 1;
      this.idForImgDel = item.id;
      this.itemsImg = item.schema53_photo;
      this.dialogImg = true;
      console.log(this.idForImgDel);
    },
    imgUrlOrd(item) {
      this.ifOrSc = 2;
      this.idForImgDel = item.id;
      this.itemsImg = item.order53_photo;
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
      for (let i = 0; i <= this.desserts.length; i++) {
        let arrayrReverse = this.desserts[i].circuit.transit.reverse();
        let arrayTransit12 = [
          ...arrayrReverse,
          ...this.desserts[i].circuit.transit2,
        ];
        let date = this.desserts[i].created_at.split("T");
        let pushArray = {
          trassa: arrayTransit12,
          date: date[0],
        };
        let finArray = Object.assign(this.desserts[i], pushArray);
        console.log(date);
        console.log(finArray);
      }
    },
    initialize() {
      let region = this.propsRegion;
      console.log(region);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/form53/list/?region=${region}`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.desserts = response.data;
          console.log(this.desserts);
          this.arrayReverseTr();
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.files = "";
      this.files2 = "";
      this.dialog = true;
    },
    deleteImg(item) {
      if (this.ifOrSc == 1) {
        this.ifos = "schema53photo";
      } else if (this.ifOrSc == 2) {
        this.ifos = "order53photo";
      }
      console.log(item);
      let idPic = item.id;
      let id = this.idForImgDel;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/opu/form53/api/${this.ifos}/delete/${id}/${idPic}/`,
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
          .delete(`${this.url.baseUrl}/apps/opu/form53/${index}/delete/`, {
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
      this.files = "";
      this.files2 = "";
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
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
      const id = this.desserts[this.editedIndex].id;
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/form53/api/order53photo/create/${id}/`,
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
    schemaSave() {
      this.loading2 = true;
      let formData = new FormData();
      if (this.files.length > 0) {
        for (let i = 0; i < this.files.length; i++) {
          let file = this.files[i];
          formData.append(`schema`, file);
        }
      }
      const id = this.desserts[this.editedIndex].id;
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/form53/api/schema53photo/create/${id}/`,
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

    save() {
      const idKanala = this.desserts[this.editedIndex].id;
      console.log(this.editedItem.comments);
      let formData = new FormData();
      formData.append("comments", this.editedItem.comments);
      this.$http
        .put(
          `${this.url.baseUrl}/apps/opu/form53/${idKanala}/edit/`,
          formData,
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.status);
          this.initialize();
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      this.close();
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
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
.pointer {
  cursor: pointer;
}
</style>
