<template>

  <v-data-table
    v-model="selected"
    :single-select="singleSelect"
    show-select
    :headers="headers"
    :items="obj"
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
        <v-toolbar-title>Список КО</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
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
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1.point" },
      { text: "ИП до", value: "point2.point" },
      { text: "Предриятие", value: "id_outfit.outfit" },
      { text: "Арендатор", value: "customer.abr" },
    ],
    obj: [],
    filtrObj: {
      id_object: "",
      outfit: "",
      customer: "",
      point_id2: "",
      point_id: "",
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
        bus.$emit("trassaDisp", [])
        bus.$emit("objectData", [])
      }
    }
  },

  mounted() {
    bus.$on("filtr_P1", (data) => {
      this.filtrObj.point_id = data;
      this.initialize();
    });
    bus.$on("filtr_Obj", (data) => {
      this.filtrObj.id_object = data;
      this.initialize();
    });
    bus.$on("filtr_Cus", (data) => {
      this.filtrObj.customer = data;
      this.initialize();
    });
    bus.$on("filtr_P2", (data) => {
      this.filtrObj.point_id2 = data;
      this.initialize();
    });
    bus.$on("filtr_Outfit", (data) => {
      this.filtrObj.outfit = data;
      this.initialize();
    });
    this.initialize();
  },
  beforeDestroy() {
    bus.$off("filtr_P1");
    bus.$off("filtr_Obj");
    bus.$off("filtr_Cus");
    bus.$off("filtr_P2");
    bus.$off("filtr_Outfit");
  },

  methods: {
    sendTrassaDisp() { 
        bus.$emit("trassaDisp", this.selected[0].trassa)
        bus.$emit("idObj", this.selected[0].id)
        bus.$emit("objectData", this.selected[0])
    },
    arrayReverseTr(name) {
      for (let i = 0; i < name.length; i++) {
        let arrayrReverse = name[i].transit.reverse();
        let arrayTransit12 = [...arrayrReverse, ...name[i].transit2];
        let pushArray = {
          trassa: arrayTransit12,
        };
        let finArray = Object.assign(name[i], pushArray);
        console.log(finArray);
      }
    },
    initialize() {
      let customer = this.filtrObj.customer;
      let point_id = this.filtrObj.point_id;
      let point_id2 = this.filtrObj.point_id2;
      let id_object = this.filtrObj.id_object;
      let outfit = this.filtrObj.outfit;

      if (customer == null) {
        customer = "";
      }
      if (outfit == null) {
        outfit = "";
      }
      if (id_object == null) {
        id_object = "";
      }
      if (point_id == null) {
        point_id = "";
      }
      if (point_id2 == null) {
        point_id2 = "";
      }

      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/event/objects/?name=${id_object}&customer=${customer}&id_outfit=${outfit}&point1=${point_id}&point2=${point_id2}`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.obj = response.data;
          this.arrayReverseTr(this.obj)
          console.log(this.obj);
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
