<template>
  <v-data-table
    v-model="selected"
    :single-select="singleSelect"
    show-select
    :headers="headers"
    :items="ip"
    :search="search"
    :items-per-page="5"
    item-key="id"
    class="elevation-1"
    dense
    :footer-props="{
      showFirstLastPage: true,
      firstIcon: 'mdi-arrow-collapse-left',
      lastIcon: 'mdi-arrow-collapse-right',
      prevIcon: 'mdi-minus',
      nextIcon: 'mdi-plus',
    }"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>Список ИП</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Поиск"
        single-line
        hide-details
      ></v-text-field>
      </v-toolbar>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Обновить</v-btn>
    </template>
  </v-data-table>
</template>

<script>
import { bus } from "../../../main";
export default {
  data: () => ({
    search: "",
    singleSelect: true,
    selected: [],
    dialog: false,
    loading: true,
    errored: false,
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Название", value: "point_id.name" },
      { text: "ИП", value: "point_id.point" },
       { text: "Предприятие", value: "point_id.id_outfit.outfit" },
    ],
    ip: [],
    filtrIP: {
      point_id: "",
      object_id: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    selected(newValue) {
      if (newValue.length > 0) {
        this.sendTrassaDisp()
        console.log(this.selected)
      } else {
        bus.$emit("dispIpData", [])
      }
    },
  },


  beforeDestroy() {
    bus.$off("point_idIP");
    bus.$off("object_idIP");
  },
  mounted() {
    bus.$on("point_idIP", (data) => {
      this.filtrIP.point_id = data;
      this.initialize();
    });
    bus.$on("object_idIP", (data) => {
      this.filtrIP.object_id = data;
      this.initialize();
    });
    this.initialize();
  },

  methods: {
     sendTrassaDisp() { 
        bus.$emit("idIP", this.selected[0].id)
        bus.$emit("dispIpData", this.selected[0])
    },
    initialize() {
      let point_id = this.filtrIP.point_id;
      let object_id = this.filtrIP.object_id;

      if (point_id == null) {
        point_id = "";
      }
      if (object_id == null) {
        object_id = "";
      }

      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/event/ips/?point_id=${point_id}`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.ip = response.data;
          console.log(this.ip);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>
