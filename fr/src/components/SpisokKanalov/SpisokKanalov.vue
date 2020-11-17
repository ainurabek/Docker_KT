<template>
  <v-container>
    <v-container>
      <v-card color="white" class="mx-auto">
        <v-card-text>
          <div>
            <span class="fontsiz">Трасса:</span>
            <span class="fontsiz" v-for="item in trassaFin" :key="item.id"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</span
            >
          </div>
        </v-card-text>
      </v-card>
    </v-container>
    <v-data-table
      dense
      :headers="headers"
      :items="desserts"
      class="elevation-1 mt-3"
      v-model="selected"
      :single-select="singleSelect"
      item-key="id"
      show-select
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Каналы</v-toolbar-title>
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
          <v-dialog v-model="dialog" max-width="650px">
            <!-- <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
            </template>-->
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.num_circuit"
                        label="№ канала"
                        readonly
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.name"
                        label="Название"
                        readonly
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.id_object.name"
                        items="desserts"
                        item-value="id"
                        label="Объект"
                        readonly
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.num_order"
                        label="№ расп-ия"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.date_order"
                        label="Дата расп-ия"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.type_using"
                        label="Тип исп-ия"
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
                        v-model="editedItem.first"
                        :items="first"
                        item-text="name"
                        item-value="bool"
                        dense
                        label="Активность к-ла"
                      ></v-autocomplete>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-autocomplete
                        v-model="editedItem.in_out"
                        label="Вх/Исх"
                        :items="in_out"
                        item-text="name"
                        item-value="id"
                        dense
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
                      <v-text-field
                        v-model="editedItem.adding"
                        label="Дополнит"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.num_arenda"
                        label="№ Аренды"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-autocomplete
                        v-model="editedItem.type_com"
                        :items="type_com"
                        item-text="name"
                        item-value="id"
                        dense
                        label="Тип свзяи"
                      ></v-autocomplete>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.speed"
                        label="Скорость"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-autocomplete
                        v-model="editedItem.measure"
                        label="Ед изм."
                        :items="measure"
                        item-text="name"
                        item-value="id"
                        dense
                      ></v-autocomplete>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-autocomplete
                        v-model="editedItem.mode"
                        label="Режим"
                        :items="mode"
                        item-text="name"
                        item-value="id"
                        dense
                      ></v-autocomplete>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.comments"
                        label="Коммент"
                      ></v-text-field>
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
                        v-model="editedItem.point2"
                        :items="point"
                        item-text="point"
                        item-value="id"
                        dense
                        label="ИП до"
                      ></v-autocomplete>
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
          <v-dialog v-model="dialog53" max-width="650px">
            <!-- <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
            </template>-->
            <v-card>
              <v-card-title>
                <span class="headline">Создание Формы 5.3</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="4" md="4">
                      <v-file-input
                        label="Ордер"
                        filled
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
                        filled
                      ></v-file-input>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem53.comments"
                        label="Комментарии"
                        filled
                      ></v-text-field>
                    </v-col>
                    <!-- <v-col cols="12" sm="6" md="4">
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
                    </v-col> -->
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close53"
                  >Отмена</v-btn
                >
                <v-btn color="blue darken-1" text @click="submitFile"
                  >Сохранить</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon :disabled="isEditing" small class="mr-2" @click="editItem(item)"
          >mdi-pencil</v-icon
        >
        <v-icon
          :disabled="isEditing"
          small
          class="mr-2"
          @click="editItem53(item)"
          >mdi-view-dashboard</v-icon
        >
      </template>
      <template v-slot:[`item.first`]="{ item }">
        <v-icon v-if="item.first == true" color="green"
          >mdi-checkbox-marked-circle</v-icon
        >
        <v-icon v-else>mdi-checkbox-marked-circle</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import router from "../../router";
// import {bus} from "../../main"
export default {
  props: ["date"],
  data: () => ({
    search: "",
    dialog: false,
    dialog53: false,
    selected: [],
    singleSelect: true,
    isEditing: null,
    loading: false,
    loading2: false,
    headers: [
      { text: "№ канала", value: "num_circuit" },
      { text: "Активные", value: "first" },
      { text: "Название", value: "name" },
      { text: "Объект", value: "id_object.name" },
      { text: "№ расп-ия", value: "num_order" },
      { text: "Дата расп-ия", value: "date_order" },
      { text: "Тип исп-ия", value: "type_using" },
      { text: "Категория", value: "category.index" },
      { text: "Вх/Исх", value: "in_out.name" },
      { text: "Арендатор", value: "customer.customer" },
      { text: "Дополнит", value: "adding" },
      { text: "№ Аренды", value: "num_arenda" },
      { text: "Тип свзяи", value: "type_com.name" },
      { text: "Скорость", value: "speed" },
      { text: "Ед изм.", value: "measure.name" },
      { text: "Режим", value: "mode.name" },
      { text: "Коммент", value: "comments" },
      { text: "ИП от", value: "point1.point" },
      { text: "ИП до", value: "point2.point" },
      { text: "Редактировать", value: "actions", sortable: false },
    ],
    desserts: [],
    trassaFin: [],
    point: [],
    customer: [],
    files: "",
    files2: "",
    idTrakt: "",
    type_com: [],
    mode: [],
    measure: [],
    in_out: [],
    first: [
      {
        name: "Активный",
        bool: true,
      },
      {
        name: "Не активный",
        bool: false,
      },
    ],
    category: [],
    editedIndex: -1,
    editedItem53: {
      schema: null,
      order: null,
      comments: "",
    },
    defaultItem53: {
      schema: null,
      order: null,
      comments: "",
    },
    editedItem: {
      adding: "",
      category: "",
      comments: "",
      customer: "",
      date_order: "",
      final_destination: "",
      first: "",
      id: "",
      id_object: "",
      in_out: "",
      measure: "",
      mode: "",
      name: "",
      num_arenda: "",
      num_circuit: "",
      num_order: "",
      number: "",
      point1: "",
      point2: "",
      speed: "",
      type_com: "",
      type_using: "",
    },
    defaultItem: {
      adding: "",
      category: "",
      comments: "",
      customer: "",
      date_order: "",
      final_destination: "",
      first: "",
      id: "",
      id_object: "",
      in_out: "",
      measure: "",
      mode: "",
      name: "",
      num_arenda: "",
      num_circuit: "",
      num_order: "",
      number: "",
      point1: "",
      point2: "",
      speed: "",
      type_com: "",
      type_using: "",
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
    selected(newValue) {
      if (newValue != {}) this.handleClick();
    },
  },

  created() {
    //   bus.$on("sendIdTrakt", data => {
    //   this.idTrakt = data.id
    // })
  },
  mounted() {
    this.userGetSub();
    this.pointGet();
    this.customerGet();
    this.categoryGet();
    this.in_outGet();
    this.measureGet();
    this.initialize();
    this.modeGet();
    this.type_comGet();
    console.log(this.date);
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
    handleClick() {
      let arrayReverse = this.selected[0].transit.reverse();
      let arrayFin = [...arrayReverse, ...this.selected[0].transit2];
      this.trassaFin = arrayFin;
      console.log(this.date);
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
    in_outGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/in-out/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.in_out = response.data;
          console.log(this.in_out);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    measureGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/circuits/measure/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.measure = response.data;
          console.log(this.measure);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    modeGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/circuits/mode/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.mode = response.data;
          console.log(this.mode);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    type_comGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/circuits/type-com/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.type_com = response.data;
          console.log(this.type_com);
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
    initialize() {
      console.log(this.date);
      let id = this.date;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/circuits/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.desserts = response.data;
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
    editItem53(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem53 = Object.assign({}, item);
      this.dialog53 = true;
    },
    deleteItem(item) {
      const index = this.desserts.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.desserts.splice(index, 1);
    },
    close() {
      this.file = "";
      this.file2 = "";
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    close53() {
      this.files = "";
      this.files2 = "";
      this.dialog53 = false;
      this.$nextTick(() => {
        this.editedItem53 = Object.assign({}, this.defaultItem53);
        this.editedIndex = -1;
      });
    },
    submitFile() {
      const idKanala = this.desserts[this.editedIndex].id;
      console.log(this.editedItem53.comments);
      let formData = new FormData();
      if (this.files2.length > 0) {
        for (let i = 0; i < this.files2.length; i++) {
          let file = this.files2[i];
          formData.append(`order`, file);
        }
      }
      if (this.files.length > 0) {
        for (let i = 0; i < this.files.length; i++) {
          let file = this.files[i];
          formData.append(`schema`, file);
        }
      }
      formData.append("comments", this.editedItem53.comments);
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/form53/${idKanala}/create/`,
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
          router.push({ name: "forma53" });
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
    save() {
      if (this.editedIndex > -1) {
        const index = this.desserts[this.editedIndex].id;

        if (this.editedItem.category == undefined) {
          this.editedItem.category = "";
        } else if (this.editedItem.category.id != undefined) {
          this.editedItem.category = this.editedItem.category.id;
        }
        // if (this.editedItem.first == undefined) {
        //   this.editedItem.first = "";
        // } else if (this.editedItem.category.id != undefined) {
        //   this.editedItem.category = this.editedItem.category.id;
        // }

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

        if (this.editedItem.customer == undefined) {
          this.editedItem.customer = "";
        } else if (this.editedItem.customer.id != undefined) {
          this.editedItem.customer = this.editedItem.customer.id;
        }

        if (this.editedItem.in_out == undefined) {
          this.editedItem.in_out = "";
        } else if (this.editedItem.in_out.id != undefined) {
          this.editedItem.in_out = this.editedItem.in_out.id;
        }

        if (this.editedItem.measure == undefined) {
          this.editedItem.measure = "";
        } else if (this.editedItem.measure.id != undefined) {
          this.editedItem.measure = this.editedItem.measure.id;
        }

        if (this.editedItem.mode == undefined) {
          this.editedItem.mode = "";
        } else if (this.editedItem.mode.id != undefined) {
          this.editedItem.mode = this.editedItem.mode.id;
        }

        if (this.editedItem.type_com == undefined) {
          this.editedItem.type_com = "";
        } else if (this.editedItem.type_com.id != undefined) {
          this.editedItem.type_com = this.editedItem.type_com.id;
        }
        console.log(
          this.editedItem.adding,
          this.editedItem.category,
          this.editedItem.comments,
          this.editedItem.customer,
          this.editedItem.date_order,
          this.editedItem.id_object.id,
          this.editedItem.in_out,
          this.editedItem.measure,
          this.editedItem.mode,
          this.editedItem.name,
          this.editedItem.num_arenda,
          this.editedItem.num_circuit,
          this.editedItem.num_order,
          this.editedItem.point1,
          this.editedItem.point2,
          this.editedItem.speed,
          this.editedItem.type_com,
          this.editedItem.type_using
        );

        this.$http
          .put(
            `${this.url.baseUrl}/apps/opu/circuits/edit/${index}/`,
            {
              adding: this.editedItem.adding,
              category: this.editedItem.category,
              comments: this.editedItem.comments,
              customer: this.editedItem.customer,
              date_order: this.editedItem.date_order,
              id_object: this.editedItem.id_object,
              in_out: this.editedItem.in_out,
              measure: this.editedItem.measure,
              mode: this.editedItem.mode,
              name: this.editedItem.name,
              num_arenda: this.editedItem.num_arenda,
              num_circuit: this.editedItem.num_circuit,
              num_order: this.editedItem.num_order,
              point1: this.editedItem.point1,
              point2: this.editedItem.point2,
              speed: this.editedItem.speed,
              type_com: this.editedItem.type_com,
              type_using: this.editedItem.type_using,
              first: this.editedItem.first,
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
</style>
