<template>
  <v-container>
    <template>
      <v-data-table
        :headers="headers"
        :items="report"
        :items-per-page="5"
        item-class="color"
   
        class="backCardDispList"
        dense
      >
        <template v-slot:top>
          <v-toolbar flat color="white">
            <v-toolbar-title>Форма анализа качества</v-toolbar-title>
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
              <!-- <download-excel
                class="btn btn-default"
                :data="report"
                :fields="json_fields"
                worksheet="My Worksheet"
                name="OtchetAK.xls"
              > -->
              Скачать в excel
              <!-- </download-excel> -->
            </v-btn>
          </v-toolbar>
        </template>
        <template v-slot:header>
          <thead color="white">
            <tr>
              <th class="borderStyle" colspan="4"></th>
              <th colspan="2">Откл. ЭЭ</th>
              <th colspan="2">ПВ апп.</th>
              <th colspan="2">Лин. ПВ</th>
              <th colspan="2">Хищение</th>
            </tr>
          </thead>
        </template>

        <template v-slot:body>
          <tbody color="white">
            <tr
              v-for="item in report"
              :key="report.indexOf(item)"
              :class="getColor(item)"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.date_from }}</td>
              <td>{{ item.amount_of_channels }}</td>
              <td>{{ item.comments }}</td>
              <td>{{ item.period_of_time.name1 }}</td>
              <td>{{ item.period_of_time.name2 }}</td>
              <td>{{ item.period_of_time.name3 }}</td>
              <td>{{ item.period_of_time.name4 }}</td>
              <td>{{ item.period_of_time.name5 }}</td>
              <td>{{ item.period_of_time.name6 }}</td>
              <td>{{ item.period_of_time.name7 }}</td>
              <td>{{ item.period_of_time.name8 }}</td>
            </tr>
          </tbody>
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
      { text: "Объект", value: "name", sortable: false, class: 'primary white--text', },
      { text: "Начало", value: "date_from", sortable: false, class: 'primary white--text',  },
      { text: "Кол-во каналов", value: "amount_of_channels", sortable: false, class: 'primary white--text', },
      { text: "Примечание", value: "comments", sortable: false, class: 'primary white--text', },
      { text: "КЛС", value: "period_of_time.name1", sortable: false, class: 'primary white--text', },
      { text: "ЦРРЛ", value: "period_of_time.name2", sortable: false, class: 'primary white--text', },
      { text: "КЛС", value: "period_of_time.name3", sortable: false, class: 'primary white--text', },
      { text: "ЦРРЛ", value: "period_of_time.name4", sortable: false, class: 'primary white--text', },
      { text: "КЛС", value: "period_of_time.name5", sortable: false, class: 'primary white--text', },
      { text: "ЦРРЛ", value: "period_of_time.name6", sortable: false, class: 'primary white--text', },
      { text: "КЛС", value: "period_of_time.name7", sortable: false, class: 'primary white--text', },
      { text: "ЦРРЛ", value: "period_of_time.name8", sortable: false, class: 'primary white--text', },
    ],
    desserts: [],
    json_fields: {},
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
    this.dateTrans();
  },

  methods: {
    getColor(item) {
      if (item.color == 1) return "colorOutfit";
      else if (item.color == 2) return "colorAllPred";
      else if (item.color == 3) return "colorAllMid";
      else if (item.color == 4) return "colorAllLast";
    },
    dateTrans() {
      for (let i = 0; i <= this.report.length - 1; i++) {
        // if (this.report[i].period_of_time.name1 != null) {
        //   if (
        //     this.report[i].type_line == 1 ||
        //     this.report[i].type_line == null
        //   ) {
        //     let pushArray = { period1: this.report[i].period_of_time.name1 };
        //     Object.assign(this.report[i], pushArray);
        //   } else {
        //     let pushArray = { period2: this.report[i].period_of_time.name1 };
        //     Object.assign(this.report[i], pushArray);
        //   }
        // }
        // if (this.report[i].period_of_time.name2 != null) {
        //   if (
        //     this.report[i].type_line == 1 ||
        //     this.report[i].type_line == null
        //   ) {
        //     let pushArray = { period3: this.report[i].period_of_time.name2 };
        //     Object.assign(this.report[i], pushArray);
        //   } else {
        //     let pushArray = { period4: this.report[i].period_of_time.name2 };
        //     Object.assign(this.report[i], pushArray);
        //   }
        // }
        if (this.report[i].date_from != null) {
          this.report[i].date_from = this.report[i].date_from
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
          `${this.url.baseUrl}/apps/analysis/api/form/?date_from=${date_from}&date_to=${date_to}&responsible_outfit=${outfit}`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.report = response.data;
          // this.array = response.data;
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
.backCardDispList {
  background-color: white;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}

thead tr th  {
  border-top: solid 1px #777777dd;
  border-right: solid 1px #777777dd;
  border-left: solid 1px #777777dd;
  font-size: 14px;
}
tbody tr td {
  border:solid 1px #777777dd;
  /* border-right: solid 1px #777777dd;
  border-left: solid 1px #777777dd; */
}
.colorOutfit {
  background-color: rgb(0, 204, 255);
}
.colorAllPred {
  background-color:rgb(238, 196, 134);
}
.colorAllLast {
  background-color: rgb(172, 255, 77);
}
.colorAllMid {
  background-color:rgb(255, 255, 57);
}
tfoot {
  margin: 10px;
  font-weight: bold;
}
</style>
