<template>
  <v-card>
    <v-card-title>
      Список ЛП
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="LP"
      sort-by="calories"
      class="elevation-1"
      :single-select="singleSelect"
      :search="search"
      v-model="selected"
      item-key="id"
      dense
      :items-per-page="8"
      :show-select="true"
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
          <DialogLP v-model="dialog"></DialogLP>
          <DialogLPDelete v-model="dialogDelete" :itemForDelete="deleteForItem">
          </DialogLPDelete>
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
import DialogLP from "./DialogLP";
import DialogLPDelete from "./DialogLPDelete";
import router from "../../../router";

export default {
  name: "LP",
  components: { DialogLP, DialogLPDelete },
  data: () => ({
    search: "",
    dialog: false,
    dialogDelete: false,
    loading: true,
    errored: false,
    singleSelect: true,
    selected: [],
    pushId: [],
    deleteForItem: {},
    headers: [
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1.point" },
      { text: "ИП до", value: "point2.point" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    LP: [],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  watch: {
    selected(newValue) {
      if (newValue.length > 0) {
        this.watchArrayId(newValue);

        bus.$emit("watchArrIdAll", 3);
        console.log(newValue, this.selected);
      } else {
        this.watchArrayId(newValue);
        bus.$emit("watchArrIdAll", 3);
        console.log(newValue, this.selected);
      }
    },
  },

  mounted() {
    bus.$on("updateSPO_LP", () => {
      this.initialize();
    });
    bus.$on("deleteSPO_LP", () => {
      this.initialize();
      bus.$emit("watchArrIdAll", 3);
    });
    this.initialize();
  },
  beforeDestroy() {
    bus.$off("updateSPO_LP");
    bus.$off("deleteSPO_LP");
  },

  methods: {
    watchArrayId(item) {
      if (item.length > 0) {
        let data_lp = {
          lp_item: item,
        };
        bus.$emit("watchArrId", data_lp);
      } else {
        let data_lp = {
          lp_item: [],
        };
        bus.$emit("watchArrId", data_lp);
      }
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/lp/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.LP = response.data;
          console.log(this.LP);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem(item) {
      localStorage.setItem("idPOForEdit", JSON.stringify(item));
      router.push({ name: "editpo" });
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
