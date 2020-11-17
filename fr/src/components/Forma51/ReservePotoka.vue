<template>
  <v-container>
    <v-data-table
      dense
      :headers="headers"
      :items="desserts[0].reserve_object"
      class="elevation-1 mt-3"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Резерв потока</v-toolbar-title>
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
        </v-toolbar>
      </template>
      <template v-slot:[`item.trassa`]="{ item }">
        <span v-for="it in item.trassa" :key="it.indexOf"
          >({{ it.point1 }}){{ it.name }}({{ it.point2 }})</span
        >
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small class="mr-2" @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  props: ["date"],
  data: () => ({
    search: "",
    dialog: false,
    selected: [],
    singleSelect: true,
    headers: [
      { text: "Объект", value: "name" },
      { text: "Категория", value: "category.name" },
      { text: "Трасса", value: "trassa" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    desserts: [],
    trassaFin: [],
    point: [],
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
      adding: "",
      category: "",
    },

    defaultItem: {
      adding: "",
      category: "",
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

  mounted() {
    this.initialize();
  },

  methods: {
    arrayReverseTr() {
      for (let i = 0; i <= this.desserts[0].reserve_object.length; i++) {
        let arrayrReverse = this.desserts[0].reserve_object[
          i
        ].transit.reverse();
        let arrayTransit12 = [
          ...arrayrReverse,
          ...this.desserts[0].reserve_object[i].transit2,
        ];
        let pushArray = {
          trassa: arrayTransit12,
        };
        let finArray = Object.assign(
          this.desserts[0].reserve_object[i],
          pushArray
        );
        console.log(finArray);
      }
    },
    initialize() {
      console.log(this.date);
      let id = this.date.id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/form51/api/reserve/${id}/`, {
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
      this.editedIndex = this.desserts.reserve_object.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      let id = this.date.id;
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/opu/form51/api/reserve/delete/${id}/${index}/`,
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
        this.$http
          .put(`${this.url.baseUrl}/apps/opu/circuits/edit/${index}/`, {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          })
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
