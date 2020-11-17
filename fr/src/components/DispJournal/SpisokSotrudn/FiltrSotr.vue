<template>
  <v-container>
    <v-card class="mx-auto backCardDispList pl-4 pr-4 pt-3 pb-3">
      <v-row justify="center">
        <v-col cols="12" sm="6" md="4">
          <v-autocomplete
            label="ФИО"
            v-model="editedItemUser"
            :items="listSotr"
            item-text="user.last_name"
            item-value="user.id"
          >
          </v-autocomplete>
        </v-col>
        <v-col cols="12" sm="6" md="3">
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
                label="Начало"
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
              <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(date)"
                >OK</v-btn
              >
            </v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" sm="6" md="3">
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
        </v-col>
      </v-row>
      <v-btn color="primary" class="ml-8 mb-4" @click="clearAll"
        >Очистить</v-btn
      >
    </v-card>
    <hr class="mt-4" />
    <SpisokSotr
      :propsUser="editedItemUser"
      :propsDateFrom="date"
      :propsDateTo="date2"
    ></SpisokSotr>
  </v-container>
</template>

<script>
import SpisokSotr from "./SpisokSotr";

export default {
  components: { SpisokSotr },
  data: () => ({
    date: "",
    menu: false,
    date2: "",
    menu2: false,
    dates: [],
    editedItemUser: "",
    listSotr: [],
    date_to: "",
    date_from: "",
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
    this.getListDisp();
  },

  methods: {
    clearAll() {
      this.editedItemUser = "";
      this.date = "";
      this.date2 = "";
    },
    resFunc(data) {
      this.listSotr = data;
      console.log(this.listSotr);
    },
    getListDisp() {
      this.detailFunc("", this.url.urlListDisp);
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
