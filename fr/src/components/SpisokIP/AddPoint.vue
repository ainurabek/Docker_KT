<template>
  <v-container
    id="scroll-target"
    style="max-height: 450px"
    class="overflow-y-auto"
  >
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Список ИП</v-toolbar-title>
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
                      <v-text-field
                        v-model="editedItem.name"
                        label="Название"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedItem.point"
                        label="ИП"
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
                        <template slot="selection" slot-scope="{ item }"
                          >{{ item.name }} - {{ item.index }}</template
                        >
                        <template slot="item" slot-scope="{ item }"
                          >{{ item.name }} - {{ item.index }}</template
                        >
                      </v-select>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-autocomplete
                        v-model="editedItem.id_outfit"
                        :items="id_outfit"
                        item-text="outfit"
                        item-value="id"
                        label="Тип предприятия"
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
      { text: "ТПО", value: "tpo.index" },
      { text: "Наименование", value: "name" },
      { text: "ИП", value: "point" },
      { text: "Предприятия", value: "id_outfit.outfit" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    tpo: [],
    id_outfit: [],
    editedIndex: -1,
    editedItem: {
      point: "",
      name: "",
      tpo: "",
      id_outfit: "",
    },
    defaultItem: {
      point: "",
      name: "",
      tpo: "",
      id_outfit: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
    typeOutfit: ["Наш", "Местный", "Зарубежный"],
    nameItem: {},
    outfitItem: {},
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Создать ИП" : "Редактировать";
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
    this.outfitGet();
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
        .get(`${this.url.baseUrl}/apps/opu/objects/point/`, {
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
          .delete(`${this.url.baseUrl}/apps/opu/objects/point/${index}/`, {
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
        if (this.editedItem.tpo == undefined) {
          this.editedItem.tpo = "";
        } else if (this.editedItem.tpo.id != undefined) {
          this.editedItem.tpo = this.editedItem.tpo.id;
        }
        if (this.editedItem.id_outfit == undefined) {
          this.editedItem.id_outfit = "";
        } else if (this.editedItem.id_outfit.id != undefined) {
          this.editedItem.id_outfit = this.editedItem.id_outfit.id;
        }
        console.log(
          this.editedItem.point,
          this.editedItem.name,
          this.editedItem.tpo,
          this.editedItem.id_outfit
        );
        this.$http
          .put(
            `${this.url.baseUrl}/apps/opu/objects/point/edit/${index}/`,
            {
              point: this.editedItem.point,
              name: this.editedItem.name,
              tpo: this.editedItem.tpo,
              id_outfit: this.editedItem.id_outfit,
            },
            { headers: { Authorization: `Token ${localStorage.token}` } }
          )
          .then((response) => {
            this.initialize();
            console.log(response.status);
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
      } else {
        this.$http
          .post(
            `${this.url.baseUrl}/apps/opu/objects/point/create/`,
            {
              point: this.editedItem.point,
              name: this.editedItem.name,
              tpo: this.editedItem.tpo,
              id_outfit: this.editedItem.id_outfit,
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
