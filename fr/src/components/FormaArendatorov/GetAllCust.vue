<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Список Арендаторов</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>
          <v-btn color="primary" dark class="mb-2 ml-4">
            <download-excel
              class="btn btn-default"
              :data="desserts"
              :fields="json_fields"
              worksheet="My Worksheet"
              name="formaArendatorov.xls"
            >
              Скачать в excel
            </download-excel>
          </v-btn>

          <v-dialog v-model="dialog" max-width="700px">
            <v-card>
              <v-card-title>
                <span class="headline">Редактировать</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.amount_flow"
                        label="Количество потоков"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                        v-model="editedItem.signalization"
                        :items="signalization"
                        item-value="id"
                        item-text="id"
                        label="Сигнализация"
                      ></v-select>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.type_of_using"
                        label="Вид использования"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        label="№ распоряжения"
                        v-model="editedItem.num_order"
                      >
                      </v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4" md="3">
                      <v-file-input
                        label="Ордер"
                        ref="files2"
                        multiple
                        v-on:change="handleFileUpload2()"
                        prepend-icon="mdi-camera"
                      ></v-file-input>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.comments"
                        label="Примечание"
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
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon :disabled="isEditing" small class="mr-2" @click="editItem(item)"
          >mdi-pencil</v-icon
        >
        <v-icon :disabled="isEditing" small @click="deleteItem(item)"
          >mdi-delete</v-icon
        >
      </template>
      <template v-slot:[`item.trassa`]="{ item }">
        <span v-for="it in item.trassa" :key="it.indexOf"
          >({{ it.point1 }}) {{ it.name }} ({{ it.point2 }})</span
        >
      </template>
      <template v-slot:[`item.point1`]="{ item }">
        <span>{{ item.point1.name }}-{{ item.point1.point }} </span>
      </template>
      <template v-slot:[`item.point2`]="{ item }">
        <span> {{ item.point2.name }}-{{ item.point2.point }}</span>
      </template>
      <template v-slot:[`item.order`]="{ item }">
        <span @click="imgUrlOrd(item)" class="pointer">{{ item.name }}</span>
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
            :src="item.order"
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
                :href="item.order"
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
export default {
  props: {
    editedItemCustomerProps: null,
  },
  data: () => ({
    isEditing: null,
    search: "",
    dialog: false,
    loading: false,
    errored: false,
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
      {
        text: "Трасса прохождение потока",
        value: "trassa",
      },
      { text: "Количество потоков", value: "amount_flow" },
      { text: "Сигнализация", value: "signalization.name" },
      { text: "Вид использования", value: "type_of_using" },
      { text: "№ распоряжения", value: "num_order" },
      { text: "Распоряжение", value: "order" },
      { text: "Примечание", value: "comments" },
      { text: "Создать Форму Арен-ов", value: "actions", sortable: false },
    ],
    json_fields: {
      Название: "name",
      "ИП от": {
        field: "point1",
        callback: (value) => {
          return `${value.name}-${value.point}`;
        },
      },
      "ИП до": {
        field: "point2",
        callback: (value) => {
          return `${value.name}-${value.point}`;
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
      "Количество потоков": "amount_flow",
      Сигнализация: "signalization.name",
      "Вид использования": "type_of_using",
      "№ распоряжения": "num_order",
      Распоряжение: "order",
      Примечание: "comments",
    },
    desserts: [],
    tpo: [],
    itemsImg: [],
    idForImgDel: "",
    ifOrSc: "",
    dialogImg: false,
    files2: "",
    signalization: [
      {
        id: 1,
      },
      {
        id: 2,
      },
    ],
    type_outfit: [
      {
        id: 1,
        name: "Наш",
      },
      {
        id: 2,
        name: "Местный",
      },
      {
        id: 3,
        name: "Зарубежный",
      },
    ],
    idGetAll: "",
    imgParams: {
      src: "",
      name: "",
    },
    editedIndex: -1,
    editedItem: {
      amount_flow: "",
      signalization: "",
      type_of_using: "",
      num_order: "",
      order: null,
      comments: "",
    },
    defaultItem: {
      amount_flow: "",
      signalization: "",
      type_of_using: "",
      num_order: "",
      order: null,
      comments: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Создать предприятие" : "Редактировать";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    editedItemCustomerProps(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
  },

  mounted() {
    this.userGetSub();
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
    imgUrlOrd(item) {
      this.ifOrSc = 2;
      this.idForImgDel = item.id;
      this.itemsImg = item.order_cust_photo;
      this.dialogImg = true;
      console.log(this.idForImgDel);
    },
    closeImg() {
      this.idForImgDel = "";
      this.itemsImg = [];
      this.dialogImg = false;
      console.log(this.itemsImg);
    },
    arrayReverseTr() {
      for (let i = 0; i <= this.desserts.length; i++) {
        if (this.desserts[i].circuit != null) {
          let arrayrReverse = this.desserts[i].circuit.transit.reverse();
          let arrayTransit12 = [
            ...arrayrReverse,
            ...this.desserts[i].circuit.transit2,
          ];
          let pushArray = {
            trassa: arrayTransit12,
            name: this.desserts[i].circuit.name,
            point1: this.desserts[i].circuit.point1,
            point2: this.desserts[i].circuit.point2,
          };
          let finArray = Object.assign(this.desserts[i], pushArray);
          console.log(finArray);
        } else if (this.desserts[i].object != null) {
          let arrayrReverse = this.desserts[i].object.transit.reverse();
          let arrayTransit12 = [
            ...arrayrReverse,
            ...this.desserts[i].object.transit2,
          ];
          let pushArray = {
            trassa: arrayTransit12,
            name: this.desserts[i].object.name,
            point1: this.desserts[i].object.point1,
            point2: this.desserts[i].object.point2,
          };
          let finArray = Object.assign(this.desserts[i], pushArray);
          console.log(finArray);
        }
      }
    },
    initialize() {
      let idAll = this.editedItemCustomerProps;
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/form_customer/api/list/?customer=${idAll}`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
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
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },
    deleteImg(item) {
      this.ifos = "ordercusphoto";
      console.log(item);
      let idPic = item.id;
      let id = this.idForImgDel;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/opu/form_customer/api/${this.ifos}/delete/${id}/${idPic}/`,
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
          .delete(
            `${this.url.baseUrl}/apps/opu/form_customer/api/delete/${index}/`,
            {
              headers: { Authorization: `Token ${localStorage.token}` },
            }
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
          `${this.url.baseUrl}/apps/opu/form_customer/api/ordercusphoto/create/${id}/`,
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
      const idEdit = this.desserts[this.editedIndex].id;
      if (this.editedItem.signalization == undefined) {
        this.editedItem.signalization = "";
      } else if (this.editedItem.signalization.id != undefined) {
        this.editedItem.signalization = this.editedItem.signalization.id;
      }
      // let formData = new FormData();
      // formData.append("amount_flow", this.editedItem.amount_flow);
      // formData.append("signalization", this.editedItem.signalization);
      // formData.append("type_of_using", this.editedItem.type_of_using);
      // formData.append("num_order", this.editedItem.num_order);
      // formData.append("comments", this.editedItem.comments);
      this.$http
        .put(
          `${this.url.baseUrl}/apps/opu/form_customer/api/update/${idEdit}/`,
          {
            amount_flow: this.editedItem.amount_flow,
            signalization: this.editedItem.signalization,
            type_of_using: this.editedItem.type_of_using,
            num_order: this.editedItem.num_order,
            comments: this.editedItem.comments,
          },
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
  },
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>
