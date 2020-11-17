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
          <v-toolbar-title>Арендаторы</v-toolbar-title>
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
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn
                :disabled="isEditing"
                color="primary"
                dark
                class="mb-2"
                v-on="on"
                >Добавить</v-btn
              >
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-form ref="form" v-model="valid" validation>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.customer"
                          :rules="[(v) => !!v || `Введите Арендатор`]"
                          label="Арендатор"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.abr"
                          :rules="[(v) => !!v || `Введите Абревиатура`]"
                          label="Абревиатура"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.address"
                          label="Адрес"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.email"
                          :rules="emailRules"
                          label="Email"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.adding"
                          label="Примечание"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.reuisits"
                          label="Реквизиты"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="4">
                        <v-text-field
                          v-model="editedItem.contact_name"
                          label="Ответственное лицо"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-form>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
                <v-btn
                  color="blue darken-1"
                  :disabled="!valid"
                  text
                  @click="save"
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
        <v-icon :disabled="isEditing" small @click="deleteItem(item)"
          >mdi-delete</v-icon
        >
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    search: "",
    dialog: false,
    isEditing: null,
    valid: true,
    emailRules: [(v) => /.+@.+\..+/.test(v) || "корректно введите E-mail"],
    headers: [
      { text: "Арендаторы", value: "customer" },
      { text: "Абревиатура", value: "abr" },
      { text: "Адрес", value: "address" },
      { text: "Примечание", value: "adding" },
      { text: "Email", value: "email" },
      { text: "Ответственное лицо", value: "contact_name" },
      { text: "Реквизиты", value: "reuisits" },
      { text: "Дата", value: "created_at" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      customer: "",
      abr: "",
      address: "",
      email: "",
      adding: "",
      reuisits: "",
      contact_name: "",
    },
    defaultItem: {
      customer: "",
      abr: "",
      address: "",
      email: "",
      adding: "",
      reuisits: "",
      contact_name: "",
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
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/customer/`, {
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

    deleteItem(item) {
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(`${this.url.baseUrl}/apps/opu/customer/${index}/`, {
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
        this.$http
          .put(
            `${this.url.baseUrl}/apps/opu/customer/${index}/`,
            {
              customer: this.editedItem.customer,
              abr: this.editedItem.abr,
              address: this.editedItem.address,
              email: this.editedItem.email,
              adding: this.editedItem.adding,
              reuisits: this.editedItem.reuisits,
              contact_name: this.editedItem.contact_name,
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
      } else {
        this.$http
          .post(
            `${this.url.baseUrl}/apps/opu/customer/`,
            {
              customer: this.editedItem.customer,
              abr: this.editedItem.abr,
              address: this.editedItem.address,
              email: this.editedItem.email,
              adding: this.editedItem.adding,
              reuisits: this.editedItem.reuisits,
              contact_name: this.editedItem.contact_name,
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
            console.log(error.response);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
      }
      this.close();
    },
  },
};
</script>

<style scoped></style>
