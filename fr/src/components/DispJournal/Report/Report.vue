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
            <v-toolbar-title>Отчет</v-toolbar-title>
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
                :footer="propsDateFrom"
                worksheet="My Worksheet"
                name="report.xls"
              >
                Скачать в excel
              </download-excel>
            </v-btn>
          </v-toolbar>
        </template>
        <template v-slot:[`item.name`]="{ item }">
          <template v-if="item.type_journal != null">
            {{ item.type_journal }}
          </template>
          <template v-if="item.outfit != null">
            {{ item.outfit }}
          </template>
          <template v-if="item.name != null">
            {{ item.name }}
          </template>
        </template>
      </v-data-table>
    </template>
  </v-container>
</template>

<script>
export default {
  props: {
    propsIndex: null,
    propsDateFrom: {
      type: String,
      default: function() {
        return "";
      },
    },
  },
  data: () => ({
    search: "",
    dialog: false,
    errored: false,
    valid: true,
    isEditing: null,
    headers: [
      { text: "Направление", value: "name" },
      { text: "Начало", value: "date_from" },
      { text: "Конец", value: "date_to" },
      { text: "Участок", value: "region" },
      { text: "Индекс 1", value: "index1" },
      { text: "Примечание", value: "comments1" },
    ],
    desserts: [],
    json_fields: {
      Направление: "nameAll",
      Начало: "date_from",
      Конец: "date_to",
      Участок: "region",
      "Индекс 1": "index1",
      Примечание: "comments1",
    },
    report: [],
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
    propsIndex(newValue) {
      this.initialize();
      console.log(newValue);
    },
  },

  mounted() {
    this.initialize();
  },

  methods: {
    dateTrans() {
      for (let i = 0; i < this.report.length; i++) {
        if (this.report[i].name != null && this.report[i].index1 == null) {
          this.report.splice(i, 1);
        }
        if (this.report[i].name != null) {
          let pushArray = {
            nameAll: this.report[i].name,
          };
          Object.assign(this.report[i], pushArray);
        }
        if (this.report[i].type_journal != null) {
          let pushArray = {
            nameAll: this.report[i].type_journal,
          };
          Object.assign(this.report[i], pushArray);
        }
        if (this.report[i].outfit != null) {
          let pushArray = {
            nameAll: this.report[i].outfit,
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
      let index = this.propsIndex;
      let date_from = this.propsDateFrom;
      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/reports/?date=${date_from}&index=${index}`,
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
          console.log(error.response);
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
