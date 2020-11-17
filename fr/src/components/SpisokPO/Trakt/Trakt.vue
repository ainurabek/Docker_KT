<template>
  <v-card>
    <v-card-title>
      Тракт
      <v-spacer></v-spacer>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="trakt"
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
          <DialogTrakt
            v-model="dialog"
            :idLPForTrakt="idLPForTrakt"
          ></DialogTrakt>
          <DialogTraktDelete
            v-model="dialogDelete"
            :itemForDelete="deleteForItem"
          >
          </DialogTraktDelete>
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
import DialogTrakt from "./DialogTrakt";
import DialogTraktDelete from "./DialogTraktDelete";
import router from "../../../router";

export default {
  name: "trakt",
  components: { DialogTrakt, DialogTraktDelete },
  data: () => ({
    search: "",
    dialog: false,
    dialogDelete: false,
    loading: true,
    errored: false,
    singleSelect: true,
    loaded: false,
    idLPForTrakt: [],
    selected: [],
    deleteForItem: {},
    headers: [
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1" },
      { text: "ИП до", value: "point2" },
      { text: "Удалить", value: "actions", sortable: false },
    ],
    trakt: [],
    typeOfTrakt: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  watch: {
    selected(newValue) {
      if (newValue.length > 0) {
        this.watchArrayId(newValue);
        bus.$emit("watchArrIdAll", 4);
        console.log(newValue, this.selected);
      } else {
        this.watchArrayId(newValue);
        bus.$emit("watchArrIdAll", 4);
        console.log(newValue, this.selected);
      }
    },
  },

  mounted() {
    bus.$on("updateSPO_Trakt", () => {
      this.initialize();
    });
    bus.$on("deleteSPO_Trakt", () => {
      this.initialize();
      bus.$emit("watchArrIdAll", 4);
    });
    bus.$on("watchArrId", (data) => {
      if (data.lp_item.length > 0) {
        this.idLPForTrakt = data.lp_item;
        this.initialize(data);
      }
      console.log(data, this.idLPForTrakt);
    });
  },
  beforeDestroy() {
    bus.$off("watchArrId");
    bus.$off("updateSPO_Trakt");
    bus.$off("deleteSPO_Trakt");
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
    initialize(data) {
      let id = data.lp_item[0].id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.trakt = response.data;
          console.log(this.trakt);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem(item) {
      localStorage.setItem("idTraktForEdit", JSON.stringify(item));
      router.push({ name: "edittrakt" });
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
