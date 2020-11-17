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

          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on">Создать</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-form ref="form" v-model="valid" validation>
                  <v-container>
                    <v-row justify="center">
                      <v-col cols="12" sm="6" md="10">
                        <v-text-field
                          v-model="editedItem.name"
                          label="Сотрудник"
                          :rules="[(v) => !!v || `Введите текст`]"
                          type="text"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="10">
                        <v-autocomplete
                          v-model="editedItem.outfit"
                          label="Предприятие"
                          :items="id_outfit"
                          item-value="id"
                          item-text="outfit"
                          :rules="[(v) => !!v || `Выберите предприятие`]"
                        ></v-autocomplete>
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
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
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
    loading: true,
    errored: false,
    isEditing: null,
    valid: true,
    id_outfit: [],
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Сотрудник", value: "name" },
      { text: "Предприятие", value: "outfit.outfit" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      id: "",
      name: "",
    },
    defaultItem: {
      id: "",
      name: "",
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
    this.initialize();
    this.outfitGet();
  },

  methods: {
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/outfit_worker/`, {
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
    outfitGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.id_outfit = response.data;
          console.log(this.id_outfit);
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
          .delete(
            `${this.url.baseUrl}/apps/dispatching/api/outfit_worker/delete/${index}/`,
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
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        const index = this.desserts[this.editedIndex].id;
        if (this.editedItem.outfit == undefined) {
          this.editedItem.outfit = "";
        } else if (this.editedItem.outfit.id != undefined) {
          this.editedItem.outfit = this.editedItem.outfit.id;
        }
        this.$http
          .put(
            `${this.url.baseUrl}/apps/dispatching/api/outfit_worker/edit/${index}/`,
            {
              name: this.editedItem.name,
              outfit: this.editedItem.outfit,
            },
            { headers: { Authorization: `Token ${localStorage.token}` } }
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
            `${this.url.baseUrl}/apps/dispatching/api/outfit_worker/create/`,
            {
              name: this.editedItem.name,
              outfit: this.editedItem.outfit,
            },
            {
              headers: { Authorization: `Token ${localStorage.token}` },
            }
          )
          .then((response) => {
            this.initialize();
            console.log(response.data);
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
