<template>
  <v-container>
    <v-card class="mx-auto backCardDispList pl-4 pr-4 pt-3 pb-3">
      <v-row justify="center">
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
              <v-btn text color="primary" @click="menu = false">Отмена</v-btn>
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

        <v-col cols="12" sm="6" md="3">
          <v-autocomplete
            label="Предприятия"
            v-model="editedItemOutfit"
            :items="outfit"
            item-value="id"
            item-text="outfit"
            
          >
          </v-autocomplete>
        </v-col>
        <v-col cols="12" sm="6" md="3" class="mt-4">
          <v-btn color="primary" class="ml-8" @click="clearAll">Очистить</v-btn>
        </v-col>
      </v-row>
    </v-card>
    <v-row justify="center">
      <v-col cols="12" sm="6" md="5">
        <v-btn color="orange" dark class="ml-8" @click="routToAK"
          >Форма анализа качества</v-btn
        >
      </v-col>
    </v-row>

    <hr />
    <OtchetDisp
      :propsOutfit="editedItemOutfit"
      :propsDateFrom="date"
      :propsDateTo="date2"
    ></OtchetDisp>
  </v-container>
</template>

<script>
import OtchetDisp from "./OtchetDisp";
import router from "../../../router";
export default {
  components: { OtchetDisp },
  data: () => ({
    date: "",
    menu: false,
    date2: "",
    menu2: false,
    dates: [],
    outfit: [],
    date_to: "",
    date_from: "",
    editedItemOutfit: "",
    datetime: null,
    datetime2: null,
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  computed: {},
  watch: {
    // date() {
    //   console.log(this.date);
    // },
    // date2() {
    //   console.log(this.date2);
    // },
  },
  mounted() {
    this.getOutfit();
  },

  methods: {
    getOutfit() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.outfit = response.data;
          console.log(this.outfit);
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
      this.editedItemOutfit = "";
    },
    routToAK() {
      router.push({
        name: "formaak",
        params: { dataProps: [this.date, this.date2, this.editedItemOutfit] },
      });
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
