<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    :search="search"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>Предприятия</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>

        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <v-btn
              :disabled="isEditing"
              color="primary"
              dark
              class="mb-2"
              v-on="on"
              >Создать предриятие</v-btn
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
                        v-model="editedItem.outfit"
                        label="Аббревиатура"
                        :rules="[(v) => !!v || `Введите Аббревиатура`]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.adding"
                        label="Название"
                        :rules="[(v) => !!v || `Введите Название`]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.num_outfit"
                        label="Номер"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-select
                        label="ТПО, Индекс"
                        v-model="editedItem.tpo"
                        :items="tpo"
                        item-value="id"
                        item-text="name"
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
                      <v-select
                        v-model="editedItem.type_outfit"
                        :items="type_outfit"
                        item-text="name"
                        item-value="id"
                        label="Тип предприятия"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-container>
              </v-form>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
              <v-btn :disabled="!valid" color="blue darken-1" text @click="save"
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
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Обновить</v-btn>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data: () => ({
    search: "",
    dialog: false,
    loading: true,
    errored: false,
    valid: true,
    isEditing: null,
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Название", value: "adding" },
      { text: "Аббревиатура", value: "outfit" },
      { text: "Номер", value: "num_outfit" },
      { text: "ТПО", value: "tpo.index" },
      { text: "Тип принадлежности", value: "type_outfit.name" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    tpo: [],
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

    editedIndex: -1,
    editedItem: {
      outfit: "",
      adding: "",
      num_outfit: "",
      tpo: "",
      type_outfit: "",
    },
    defaultItem: {
      outfit: "",
      adding: "",
      num_outfit: "",
      tpo: "",
      type_outfit: "",
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
  },

  mounted() {
    this.userGetSub();
    this.initialize();
    this.tpoGet();
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
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
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
          .delete(`${this.url.baseUrl}/apps/opu/objects/outfit/${index}/`, {
            headers: { Authorization: `Token ${localStorage.token}` },
          })
          .then((response) => {
            if (response.status == "204") {
              this.initialize();
            }
          })
          .catch((error) => {
            console.log(error.response.data);
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
        if (this.editedItem.tpo == undefined) {
          this.editedItem.tpo = "";
        } else if (this.editedItem.tpo.id != undefined) {
          this.editedItem.tpo = this.editedItem.tpo.id;
        }
        if (this.editedItem.type_outfit == undefined) {
          this.editedItem.type_outfit = "";
        } else if (this.editedItem.type_outfit.id != undefined) {
          this.editedItem.type_outfit = this.editedItem.type_outfit.id;
        }

        console.log(
          this.editedItem.outfit,
          this.editedItem.adding,
          this.editedItem.num_outfit,
          this.editedItem.tpo,
          this.editedItem.type_outfit
        );
        this.$http
          .put(
            `${this.url.baseUrl}/apps/opu/objects/outfit/edit/${index}/`,
            {
              outfit: this.editedItem.outfit,
              adding: this.editedItem.adding,
              num_outfit: this.editedItem.num_outfit,
              tpo: this.editedItem.tpo,
              type_outfit: this.editedItem.type_outfit,
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
            `${this.url.baseUrl}/apps/opu/objects/outfit/create/`,
            {
              outfit: this.editedItem.outfit,
              adding: this.editedItem.adding,
              num_outfit: this.editedItem.num_outfit,
              tpo: this.editedItem.tpo,
              type_outfit: this.editedItem.type_outfit,
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

<style scoped></style>
