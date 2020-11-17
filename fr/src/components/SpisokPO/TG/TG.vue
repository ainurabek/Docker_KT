<template>
  <v-card>
    <v-card-title>
      ТГ
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="TG"
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
          <DialogTG v-model="dialog" :itemForEdit="editForItem"></DialogTG>
          <DialogTGDelete v-model="dialogDelete" :itemForDelete="deleteForItem">
          </DialogTGDelete>
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
import DialogTG from "./DialogTG";
import DialogTGDelete from "./DialogTGDelete";
import router from "../../../router";

export default {
  name: "tg",
  components: { DialogTG, DialogTGDelete },
  data: () => ({
    search: "",
    dialog: false,
    dialogDelete: false,
    loading: true,
    errored: false,
    singleSelect: true,
    loaded: false,
    editForItem: [],
    idTraktForTG: [],
    selected: [],
    deleteForItem: {},
    headers: [
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1" },
      { text: "ИП до", value: "point2" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    TG: [],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  watch: {},

  mounted() {
    bus.$on("updateSPO_TG", () => {
      this.initialize();
    });
    bus.$on("deleteSPO_TG", () => {
      this.initialize();
    });
    bus.$on("idTraktForTG", (data) => {
      if (data.length > 0) {
        this.selected = [];
        this.itemTraktForTG = data;
        this.editForItem = data;
        this.initialize();
        console.log(this.editForItem);
      }
    });

    bus.$on("LPclear", () => {
      this.clearAll();
    });
    bus.$on("nullArrayTrakt", () => {
      this.selected = [];
      this.TG = [];
      this.itemTraktForTG = [];
      this.editForItem = [];
    });
  },
  beforeDestroy() {
    bus.$off("updateSPO_TG");
    bus.$off("deleteSPO_TG");
    bus.$off("idTraktForTG");
    bus.$off("LPclear");
    bus.$off("nullArrayTrakt");
  },

  methods: {
    clearAll() {
      this.selected = [];
      this.TG = [];
      this.itemTraktForTG = [];
      this.editForItem = [];
      this.loaded = false;
      console.log(this.itemTraktForTG);
    },
    initialize() {
      let id = this.itemTraktForTG[0].id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.TG = response.data;
          this.loaded = true;
          console.log(this.TG);
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
