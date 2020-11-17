<template>
  <v-container>
    <v-card class="mx-auto backCardDispList">
      <v-row justify="center">
        <!-- <v-col cols="12" sm="6" md="3">
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
             locale="ru"
          ></v-text-field>
        </template>
        <v-date-picker v-model="date" :first-day-of-week="1"
      locale="ru" no-title scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="menu = false">Отмена</v-btn>
          <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
        </v-date-picker>
      </v-menu>
    </v-col> -->
        <v-col cols="12" sm="6" md="3">
          <v-text-field
            label="Дата"
            type="date"
            v-model="date"
            min="1990-06-01"
            max="2099-06-30"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Индекс"
            v-model="editedIndex"
            item-value="id"
            item-text="index"
            :items="index"
          >
          </v-autocomplete>
        </v-col>
        <v-col cols="12" sm="6" md="3" class="mt-4">
          <v-btn color="primary" class="ml-8" @click="clearAll">Очистить</v-btn>
        </v-col>
      </v-row>
    </v-card>
    <hr class="mt-4" />
    <Report :propsIndex="editedIndex" :propsDateFrom="date"></Report>
  </v-container>
</template>

<script>
import Report from "./Report";

export default {
  components: { Report },
  data: () => ({
    date: "",
    menu: false,
    date2: "",
    menu2: false,
    dates: [],
    date_to: "",
    date_from: "",
    editedIndex: "",
    index: [],
    datetime: null,
    datetime2: null,
    url: {
      baseUrl: "http://0.0.0.0:8000",
      urlListDisp: "/apps/accounts/log-user-list/",
    },
  }),
  computed: {},
  watch: {
    date() {
      console.log(this.date);
    },
    date2() {
      console.log(this.date2);
    },
  },
  mounted() {
    this.getIndex();
    if (this.date == "") {
      this.date = new Date().toISOString().substring(0, 10);
    }
  },

  methods: {
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
    clearAll() {
      this.date = "";
      this.date2 = "";
      this.editedIndex = "";
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
