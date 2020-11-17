<template>
  <v-data-table
    v-model="selected"
    :single-select="singleSelect"
    show-select
    :headers="headers"
    :items="circ"
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
        <v-toolbar-title>Список Каналов</v-toolbar-title>
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
      { text: "Номер канала", value: "num_circuit" },
      { text: "Арендатор", value: "customer.customer" },
      { text: "Тип использования", value: "type_using" },
    ],
    circ: [],
    filtrCirc: {
      name: "",
      type_using: "",
      customer: "",
      id_object: "",
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
         bus.$emit("trassaDispCirc", [])
         bus.$emit("dispDataCirc", [])
      }
    }
  },

  mounted() {
    bus.$on("editedItemCircName", (data) => {
      this.filtrCirc.name = data;
      if (data == null) {
        data = ""
      }
      this.initialize();
    });
    bus.$on("editedItemCircObj", (data) => {
      this.filtrCirc.id_object = data;
      
      this.initialize();
    });
    bus.$on("editedItemCircCus", (data) => {
      this.filtrCirc.customer = data;
      
      this.initialize();
    });
    bus.$on("editedItemCircTy", (data) => {
      this.filtrCirc.type_using = data;
      
      this.initialize();
    });
    this.initialize();
  },
  beforeDestroy() {
    bus.$off("editedItemCircName");
    bus.$off("editedItemCircObj");
    bus.$off("editedItemCircCus");
    bus.$off("editedItemCircTy");
  },

  methods: {
     sendTrassaDisp() { 
        bus.$emit("idCirc", this.selected[0].id)
        bus.$emit("trassaDispCirc", this.selected[0].trassa)
        bus.$emit("dispDataCirc", this.selected[0])
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
     
      let customer = this.filtrCirc.customer;
      let type_using = this.filtrCirc.type_using;
      let id_object = this.filtrCirc.id_object;
      let name = this.filtrCirc.name;
      
      if ( customer == null ) {
        customer = ""
      } 
      if ( name == null ) {
        name = ""
      } 
      if ( id_object == null ) {
        id_object = ""
      } 
      if ( type_using == null ) {
        type_using = ""
      } 

      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/event/circuits/?id_object=${id_object}&name=${name}&customer=${customer}&type_using=${type_using}`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.circ = response.data;
          this.arrayReverseTr(this.circ)
          console.log(this.circ);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>
