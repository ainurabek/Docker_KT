<template>
  <v-card>
    <v-card-title>
      ЧГ
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="CHG"
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
          <DialogCHG v-model="dialog" :itemForEdit="editForItem"></DialogCHG>
          <DialogCHGDelete
            v-model="dialogDelete"
            :itemForDelete="deleteForItem"
          >
          </DialogCHGDelete>
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
import DialogCHG from "./DialogCHG";
import DialogCHGDelete from "./DialogCHGDelete";
import router from "../../../router";

export default {
  name: "chg",
  components: { DialogCHG, DialogCHGDelete },
  data: () => ({
    search: "",
    dialog: false,
    dialogDelete: false,
    loading: true,
    errored: false,
    singleSelect: true,
    loaded: false,
    editForItem: [],
    idTraktForCHG: [],
    selected: [],
    deleteForItem: {},
    headers: [
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1" },
      { text: "ИП до", value: "point2" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    CHG: [],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  watch: {},

  mounted() {
    bus.$on("updateSPO_CHG", () => {
      this.initialize();
    });
    bus.$on("deleteSPO_CHG", () => {
      this.initialize();
    });
    bus.$on("idLPForTrakt", (data) => {
      if (data.trakt.length > 0) {
        if (data.typeOfTrakt == 5) {
          this.selected = [];
          this.itemTraktForCHG = data.trakt;
          this.editForItem = data.trakt;
          this.initialize();
          console.log(this.editForItem);
        }
      }
    });
    bus.$on("nullArray", (data) => {
      if (data.number > 5) {
        this.selected = [];
        this.CHG = [];
        this.itemTraktForCHG = [];
        this.editForItem = [];
      }
    });
  },
  beforeDestroy() {
    bus.$off("updateSPO_CHG");
    bus.$off("deleteSPO_CHG");
    bus.$off("idLPForTrakt");
    bus.$off("nullArray");
  },

  methods: {
    clearAll() {
      this.selected = [];
      this.CHG = [];
      this.itemTraktForCHG = [];
      this.editForItem = [];
      console.log(this.itemTraktForCHG);
    },
    initialize() {
      let id = this.itemTraktForCHG[0].id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.CHG = response.data;
          console.log(this.CHG);
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
