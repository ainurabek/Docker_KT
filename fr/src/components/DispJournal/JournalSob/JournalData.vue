<template>
  <v-data-table
    v-model="selected"
    :single-select="singleSelect"
    show-select
    :headers="headers"
    :items="dispList"
    :items-per-page="7"
    :search="search"
    item-key="id"
    class="elevation-1"
    :footer-props="{
      showFirstLastPage: true,
      firstIcon: 'mdi-arrow-collapse-left',
      lastIcon: 'mdi-arrow-collapse-right',
      prevIcon: 'mdi-minus',
      nextIcon: 'mdi-plus',
    }"
  >
    <v-card-title>
      Nutrition
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>Список событий</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Поиск"
          single-line
          hide-details
        ></v-text-field>

        <v-spacer></v-spacer>
        <v-row justify="end">
          <v-btn
            color="green"
            dark
            class="mr-6 mt-2"
            :disabled="!isEditing"
            @click="pushCreateJ"
            >Создать событие</v-btn
          >
        </v-row>
      </v-toolbar>
    </template>
    <template v-slot:[`item.name`]="{ item }">
      <v-chip :class="getColor(item.index1)" dark>
        {{ item.name }}
      </v-chip>
    </template>
    <template v-slot:[`item.index1`]="{ item }">
      <v-chip :class="getColor(item.index1)" dark>
        {{ item.index1 }}
      </v-chip>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Обновить</v-btn>
    </template>
  </v-data-table>
</template>

<script>
import { bus } from "../../../main";
import router from "../../../router";
export default {
  props: {
    propsTypeJourn: null,
    propsIndex1: null,
    propsDateFrom: null,
    propsDateTo: null,
    propsValueDate: null,
  },
  data: () => ({
    search: "",
    singleSelect: true,
    selected: [],
    dialog: false,
    loading: true,
    errored: false,
    isEditing: true,
    headers: [
      { text: "Где", value: "name" },
      { text: "Индекс-1", value: "index1" },
      { text: "Начало", value: "date_from2" },
      { text: "Конец", value: "date_to2" },
      { text: "Предприятие", value: "responsible_outfit" },
    ],
    dispList: [],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    propsValueDate(newValue) {
      console.log(newValue);
    },
    propsTypeJourn() {
      this.initialize();
    },
    propsIndex1() {
      this.initialize();
    },
    propsDateFrom() {
      this.initialize();
    },
    propsDateTo() {
      this.initialize();
    },
    selected(newValue) {
      if (newValue.length == 1) {
        this.isEditing = false;
        this.sendIdDispJour();
        console.log(newValue);
      } else {
        this.isEditing = true;
        this.sendIdDispJourN();
      }
    },
  },

  mounted() {
    bus.$on("deleteUpdateJourn", () => {
      this.initialize();
      this.sendIdDispJourN();
    });
    bus.$on("updateJourn", () => {
      this.initialize();
    });
    this.initialize();
  },
  beforeDestroy() {
    bus.$off("deleteUpdateJourn");
    bus.$off("updateJourn");
  },

  methods: {
    getColor(item) {
      if (item != 4) {
        return "green";
      } else {
        return "blue";
      }
    },
    pushCreateJ() {
      router.push({ name: "createjourn" });
    },
    initialize() {
      if (this.propsValueDate == 1) {
        this.getStartDate();
      } else if (this.propsValueDate == 2) {
        this.getEndDate();
      }
    },
    sendIdDispJour() {
      this.$emit("sendSelDispJour", this.selected[0]);
      this.$emit("sendIdDispJour", this.selected[0].id);
    },
    sendIdDispJourN() {
      this.$emit("sendIdDispJour", this.selected);
    },
    dateTrans() {
      for (let i = 0; i < this.dispList.length; i++) {
        if (this.dispList[i].object != null) {
          let pushArray = {
            name: this.dispList[i].object.name,
          };
          Object.assign(this.dispList[i], pushArray);
        }
        if (this.dispList[i].circuit != null) {
          let pushArray = {
            name: this.dispList[i].circuit.name,
          };
          Object.assign(this.dispList[i], pushArray);
        }
        if (this.dispList[i].ips != null) {
          let pushArray = {
            name: this.dispList[i].ips.point_id.point,
          };
          Object.assign(this.dispList[i], pushArray);
        }
        if (this.dispList[i].index1 != "4") {
          let pushArray = {
            colorIndex: 1,
          };
          Object.assign(this.dispList[i], pushArray);
        }
        if (this.dispList[i].date_from != null) {
          let date_from2 =
            this.dispList[i].date_from.substring(0, 10) +
            " " +
            this.dispList[i].date_from.substring(11, 16);
          let pushArray = {
            date_from2: date_from2,
          };
          Object.assign(this.dispList[i], pushArray);
        }
        if (this.dispList[i].date_to != null) {
          let date_to2 =
            this.dispList[i].date_to.substring(0, 10) +
            " " +
            this.dispList[i].date_to.substring(11, 16);
          let pushArray = {
            date_to2: date_to2,
          };
          Object.assign(this.dispList[i], pushArray);
        }
      }
    },
    getStartDate() {
      let date_from = this.propsDateFrom;
      // let date_to = this.propsDateTo
      let type_journal = this.propsTypeJourn;
      let index1 = this.propsIndex1;
      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/list/?created_at=${date_from}&index1=${index1}&type_journal=${type_journal}`
        )
        .then((response) => {
          this.dispList = response.data;
          this.dateTrans();
          console.log(this.dispList);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getEndDate() {
      let date_from2 = this.propsDateFrom;
      let date_to2 = this.propsDateTo;
      let type_journal = this.propsTypeJourn;
      let index1 = this.propsIndex1;

      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/list/?date_from_to=${date_from2}&date_to_to=${date_to2}&index1=${index1}&type_journal=${type_journal}`
        )
        .then((response) => {
          this.dispList = response.data;
          this.dateTrans();
          console.log(this.dispList);
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

<style scoped>
.style-1 {
  background-color: rgb(215, 215, 44);
}
.style-2 {
  background-color: rgb(114, 114, 67);
}
</style>
