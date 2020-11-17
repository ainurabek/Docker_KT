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
          <v-toolbar-title>Форма Арендаторов:Объекты</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>
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
      <template v-slot:[`item.trassa`]="{ item }">
        <span v-for="it in item.trassa" :key="it.indexOf"
          >({{ it.point1 }}){{ it.name }}({{ it.point2 }})</span
        >
      </template>
      <template v-slot:[`item.point1`]="{ item }">
        <span>{{ item.point1.name }}-{{ item.point1.point }} </span>
      </template>
      <template v-slot:[`item.point2`]="{ item }">
        <span> {{ item.point2.name }}-{{ item.point2.point }}</span>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          :disabled="isEditing"
          small
          class="mr-2"
          @click="createObj(item)"
          >mdi-view-dashboard</v-icon
        >
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import router from "../../router";
export default {
  props: ["date"],
  data: () => ({
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
      {
        text: "Трасса прохождение потока",
        value: "trassa",
      },
      { text: "Создать Форму Арен-ов", value: "actions", sortable: false },
    ],
    desserts: [],
    files2: "",
    signalization: [
      {
        id: 1,
      },
      {
        id: 2,
      },
    ],
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

  computed: {},

  watch: {},

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
    createObj(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },
    close() {
      this.files2 = "";
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    save() {
      const idCreateObj = this.desserts[this.editedIndex].id;
      console.log(idCreateObj);
      let formData = new FormData();
      if (this.files2.length > 0) {
        for (let i = 0; i < this.files2.length; i++) {
          let file = this.files2[i];
          formData.append(`order`, file);
        }
      }
      formData.append("amount_flow", this.editedItem.amount_flow);
      formData.append("signalization", this.editedItem.signalization);
      formData.append("type_of_using", this.editedItem.type_of_using);
      formData.append("num_order", this.editedItem.num_order);
      formData.append("comments", this.editedItem.comments);
      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/form_customer/api/object/create/${idCreateObj}/`,
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
          router.push({
            name: "formaarendatorov",
            params: { date: this.date },
          });
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
    initialize() {
      let idObj = this.date;
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/form_customer/api/object/${idObj}/`,
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
  },
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>
