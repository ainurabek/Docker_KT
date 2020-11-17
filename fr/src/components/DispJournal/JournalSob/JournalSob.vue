<template>
  <v-container>
    <v-card class="mx-auto backCardDispList pl-4 pr-4 pt-3 pb-3">
      <v-row justify="center">
        <v-col cols="12" sm="6" md="3">
          <v-select
            label="Вид Журнала"
            v-model="editedItemTypeJournal"
            :items="type_journal"
            item-value="id"
            item-text="name"
          >
          </v-select>
        </v-col>
        <v-col cols="12" sm="6" md="2">
          <v-select
            label="Индекс, 1"
            v-model="editedItemIndex1"
            :items="index"
            item-value="id"
            item-text="index"
          >
          </v-select>
        </v-col>
        <v-col cols="12" sm="6" md="4">
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="date"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date"
                label="Дата"
                prepend-icon="event"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date"
              :first-day-of-week="1"
              locale="ru"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu = false">Отмена</v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(date)"
                >OK</v-btn
              >
            </v-date-picker>
          </v-menu>
        </v-col>
        <!-- <v-col cols="12" sm="6" md="2">
          <v-menu
            ref="menu2"
            v-model="menu2"
            :close-on-content-click="false"
            :return-value.sync="date2"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date2"
                label="Конец"
                prepend-icon="event"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date2"
              :first-day-of-week="1"
              locale="ru"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu2 = false">Cancel</v-btn>
              <v-btn text color="primary" @click="$refs.menu2.save(date2)"
                >OK</v-btn
              >
            </v-date-picker>
          </v-menu>
        </v-col> -->
      </v-row>
      <v-row>
        <v-btn color="primary" class="ml-8 mt-4" @click="clearAll"
          >Очистить</v-btn
        >

        <!-- <v-radio-group class="ml-8" v-model="row" row>
          <v-radio label="Фильтр по началу события" value="1"></v-radio>
          <v-radio label="Фильтр по окончанию события" value="2"></v-radio>
        </v-radio-group> -->
      </v-row>
    </v-card>

    <hr class="mt-4" />
    <JournalData
      :propsTypeJourn="editedItemTypeJournal"
      :propsIndex1="editedItemIndex1"
      :propsDateFrom="date"
      :propsDateTo="date2"
      :propsValueDate="row"
      @sendIdDispJour="idJournDataFunc"
      @sendSelDispJour="selJournDataFunc"
    ></JournalData>
    <hr />
    <!-- <JournalDetail
      class="mt-4"
      v-if="idJournData > 0"
      :propsIdJourn="idJournData"
      :propsSelJourn="selJourn"
    ></JournalDetail> -->
    <JournalDetail1
      class="mt-4"
      v-if="idJournData > 0"
      :propsIdJourn="idJournData"
      :propsSelJourn="selJourn"
    ></JournalDetail1>
  </v-container>
</template>

<script>
import JournalDetail1 from "./JournalDetail1";
import JournalData from "./JournalData";
// import JournalDetail from "./JournalDetail";
export default {
  components: { JournalData, JournalDetail1 },
  data: () => ({
    date: "",
    row: "1",
    menu: false,
    date2: "",
    menu2: false,
    dates: [],
    editedItemTypeJournal: "",
    editedItemIndex1: "",
    date_to: "",
    date_from: "",
    idJournData: "",
    selJourn: "",
    index: [],
    type_journal: [],
    datetime: null,
    datetime2: null,
    url: {
      baseUrl: "http://0.0.0.0:8000",
      urlListDisp: "/apps/dispatching/api/list/",
    },
  }),
  computed: {},
  watch: {
    row() {
      this.date = "";
      this.date2 = "";
    },
    date() {
      console.log(this.date);
    },
    date2() {
      console.log(this.date2);
    },
  },
  mounted() {
    this.getListDisp();
    this.getIndex();
    this.getTypeJournal();
    this.getReason();
  },

  methods: {
    getTypeJournal() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/type_journal/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.type_journal = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getReason() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/reason/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.reason = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getIndex() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/index/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.index = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    idJournDataFunc(data) {
      this.idJournData = data;
      console.log(data);
    },
    selJournDataFunc(data) {
      this.selJourn = data;
      console.log(data);
    },
    clearAll() {
      this.editedItemTypeJournal = "";
      this.editedItemIndex1 = "";
      this.date = "";
      this.date2 = "";
    },
    getListDisp() {
      this.detailFunc("", this.url.urlListDisp);
    },
    resFunc(data) {
      this.listDisp = data;
      console.log(this.listDisp);
    },
    detailFunc(idArg, urlFunc) {
      this.$http
        .get(`${this.url.baseUrl}${urlFunc}${idArg}`, {
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
        })
        .then((response) => {
          this.resFunc(response.data);
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
.backCardDispList {
  background-color: white;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}
</style>
