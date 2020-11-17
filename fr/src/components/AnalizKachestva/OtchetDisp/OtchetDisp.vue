<template>
  <v-container>
    <template>
      <v-data-table
        :headers="headers"
        :items="report"
        :items-per-page="10"
        class="elevation-1"
        dense
      >
        <template v-slot:top>
          <v-toolbar flat color="white">
            <v-toolbar-title>Отчет анализа качества</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-btn color="green" dark class="mb-2 ml-4">
              <download-excel
                class="btn btn-default"
                :data="report"
                :fields="json_fields"
                worksheet="My Worksheet"
                name="OtchetAK.xls"
              >
                Скачать в excel
              </download-excel>
            </v-btn>
            <div class="text-center">
              <v-dialog v-model="dialog" width="500">
                <v-card>
                  <v-card-title class="headline grey lighten-2">
                    История
                  </v-card-title>

                  <v-card-text>
                    <v-row v-for="item in history" :key="item.history_id">
                      <v-col cols="12" sm="6" md="10">
                        <div  class="text--secondary">
                          Метод действия:  <span class="text--primary">{{ item.change_method }}</span>
                        </div>
                        <div class="text--secondary">
                           Изменения: <span class="text--primary">{{ item.changes }}</span>
                        </div>
                        <div class="text--secondary">
                           Кем изменен:  <span class="text--primary">{{ item.updated_by }}</span>
                        </div>
                        <div class="text--secondary"> 
                          Дата изменения:  <span class="text--primary">{{ item.updated_date }} </span>
                        </div>
                      </v-col>
                    </v-row>
                  </v-card-text>

                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="dialog = false">
                      OK
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </div>
          </v-toolbar>
        </template>
        <template v-slot:[`item.name`]="{ item }">
          <template v-if="item.ips != null">
            {{ item.ips.point_id.point }}
          </template>
          <template v-if="item.object != null">
            {{ item.object.name }}
          </template>
          <template v-if="item.circuit != null">
            {{ item.circuit.name }}
          </template>
        </template>
        <template v-slot:[`item.actions`]="{ item }">
          <v-icon @click="historyDetail(item)"
            >mdi-arrow-down-drop-circle</v-icon
          >
        </template>
      </v-data-table>
    </template>
  </v-container>
</template>

<script>
export default {
  props: {
    propsDateFrom: null,
    propsDateTo: null,
    propsOutfit: null,
  },
  data: () => ({
    search: "",
    dialog: false,
    errored: false,
    valid: true,
    isEditing: null,
    headers: [
      { text: "Направление", value: "name" },
      { text: "Индекс 1", value: "index1" },
      { text: "Начало", value: "date_from" },
      { text: "Конец", value: "date_to" },
      { text: "ИП от", value: "point1.point" },
      { text: "ИП до", value: "point2.point" },
      // { text: "Причина", value: "reason" },
      { text: "Примечание", value: "comments1" },
      { text: "История", value: "actions", sortable: false },
    ],
    desserts: [],
    json_fields: {
      Направление: "nameAll",
      "Индекс 1": "index1",
      Начало: "date_from",
      Конец: "date_to",
      "ИП от": "point1.point",
      "ИП до": "point2.point",
      Примечание: "comments1",
    },
    arrayString: [
      {
        name1: /index1/g,
        name2: " Индекс ",
      },
      {
        name1: /date_to/g,
        name2: " Конец ",
      },
      {
        name1: /date_from/g,
        name2: " Начало ",
      },
      {
        name1: /point1/g,
        name2: " ИП от ",
      },
      {
        name1: /point2/g,
        name2: " ИП до ",
      },
      {
        name1: /comments1/g,
        name2: " Примечание ",
      },
      {
        name1: /reason/g,
        name2: " Причина ",
      },
    ],
    report: [],
    history: [],
    editedIndex: -1,
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    propsDateFrom(newValue) {
      this.initialize();
      console.log(newValue);
    },
    propsDateTo(newValue) {
      this.initialize();
      console.log(newValue);
    },
    propsOutfit(newValue) {
      this.initialize();
      console.log(newValue);
    },
  },

  mounted() {
    this.initialize();
  },

  methods: {
    historyDetail(item) {
      let id = item.id;
      console.log(id);
      this.$http
        .get(`${this.url.baseUrl}/apps/analysis/history/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          if (response.status == 200) {
            this.history = response.data;
            this.historyDateTrans();
            this.dialog = true;
          }
          console.log(this.history);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    historyDateTrans() {
      for (let i = 0; i < this.arrayString.length; i++) {
        let b = this.arrayString[i].name1;
        let c = this.arrayString[i].name2;
        for (let n = 0; n < this.history.length; n++) {
          if (this.history[n].updated_date != null) {
          this.history[n].updated_date = this.history[n].updated_date
            .split("T")
            .join(" - ")
            .substring(0, 18);
        }
          if (b.test(this.history[n].changes)) {
            this.history[n].changes = this.history[n].changes
              .replace(b, c)
              .replace(/None/g, " ---");
          }
        }
      }
      console.log(this.history);
    },
    dateTrans() {
      for (let i = 0; i < this.report.length; i++) {
        if (this.report[i].ips != null) {
          let pushArray = {
            nameAll: this.report[i].ips.point_id.point,
          };
          Object.assign(this.report[i], pushArray);
        }
        if (this.report[i].object != null) {
          let pushArray = {
            nameAll: this.report[i].object.name,
          };
          Object.assign(this.report[i], pushArray);
        }
        if (this.report[i].circuit != null) {
          let pushArray = {
            nameAll: this.report[i].circuit.name,
          };
          Object.assign(this.report[i], pushArray);
        }

        if (this.report[i].date_from != null) {
          this.report[i].date_from = this.report[i].date_from
            .split("T")
            .join(" - ")
            .substring(0, 18);
        }
        if (this.report[i].date_to != null) {
          this.report[i].date_to = this.report[i].date_to
            .split("T")
            .join(" - ")
            .substring(0, 18);
        }
      }
    },
    initialize() {
      let date_from = this.propsDateFrom;
      let date_to = this.propsDateTo;
      let outfit = this.propsOutfit;
      this.$http
        .get(
          `${this.url.baseUrl}/apps/analysis/disp/report/?date_from=${date_from}&date_to=${date_to}&responsible_outfit=${outfit}`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.report = response.data;
          this.dateTrans();
          console.log(this.report);
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

<style scoped>
caption {
  font-size: 40px;
}
thead th {
  background-color: aqua;
  padding: 5px 25px 5px 25px;
}
tbody {
  margin: 10px;
  font-size: 90%;
  font-style: italic;
}

tfoot {
  margin: 10px;
  font-weight: bold;
}
</style>
