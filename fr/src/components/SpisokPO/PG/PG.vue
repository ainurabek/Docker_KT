<template>
  <v-card>
    <v-card-title>
      ПГ
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="PG"
      sort-by="calories"
      class="elevation-1"
      :single-select="singleSelect"
      :search="search"
      v-model="selected"
      item-key="id"
      dense
      :items-per-page="8"
      show-select
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Поиск"
            single-line
            hide-details
          ></v-text-field>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn color="primary" dark class="mb-2" @click="createItem">
            Создать
          </v-btn>
          <DialogPG v-model="dialog" :itemForEdit="editForItem"></DialogPG>
          <DialogPGDelete v-model="dialogDelete" :itemForDelete="deleteForItem">
          </DialogPGDelete>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small @click="deleteItem(item)">
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:[`item.name`]="{ item }">
        <span small class="pointer" @click="editItem(item)">
          {{ item.name }}
        </span>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">
          Обновить
        </v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { bus } from "../../../main";
import DialogPG from "./DialogPG";
import DialogPGDelete from "./DialogPGDelete";
import router from "../../../router";

export default {
  name: "pg",
  components: { DialogPG, DialogPGDelete },
  data: () => ({
    search: "",
    dialog: false,
    dialogDelete: false,
    loading: true,
    errored: false,
    singleSelect: true,
    loaded: false,
    editForItem: [],
    idTraktForPG: [],
    selected: [],
    deleteForItem: {},
    headers: [
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1" },
      { text: "ИП до", value: "point2" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    PG: [],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  watch: {},

  mounted() {
    bus.$on("updateSPO_PG", () => {
      this.initialize();
    });
    bus.$on("deleteSPO_PG", () => {
      this.initialize();
    });
    bus.$on("idTraktForPG", (data) => {
      if (data.length > 0) {
        this.selected = [];
        this.itemTraktForPG = data;
        this.editForItem = data;
        this.initialize();
        console.log(data, this.editForItem);
      }
    });

    bus.$on("LPclear", () => {
      this.clearAll();
    });
    bus.$on("nullArrayTrakt", () => {
      this.selected = [];
      this.PG = [];
      this.itemTraktForPG = [];
      this.editForItem = [];
    });
  },
  beforeDestroy() {
    bus.$off("updateSPO_PG");
    bus.$off("deleteSPO_PG");
    bus.$off("idTraktForPG");
    bus.$off("LPclear");
    bus.$off("nullArrayTrakt");
  },

  methods: {
    clearAll() {
      this.selected = [];
      this.PG = [];
      this.itemTraktForPG = [];
      this.editForItem = [];
      this.loaded = false;
      console.log(this.itemTraktForPG);
    },
    initialize() {
      let id = this.itemTraktForPG[0].id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.PG = response.data;
          this.loaded = true;
          console.log(this.PG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem(item) {
      localStorage.setItem("idTraktForEdit", JSON.stringify(item));
      router.push({ name: "editpgitd" });
    },
    createItem() {
      this.dialog = true;
    },
    deleteItem(item) {
      this.deleteForItem = Object.assign({}, item);
      this.dialogDelete = true;
    },
  },
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>
