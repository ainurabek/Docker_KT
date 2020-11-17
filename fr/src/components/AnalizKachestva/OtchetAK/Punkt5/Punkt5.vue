<template>
  <v-container>
    <v-card class="mb-2">
      <v-card-title>{{nametable}}</v-card-title>
      <v-card-actions>
        <div class="centerBtn">
          <v-btn color="green darken-1" dark @click="srKlink">
            Средний коэф.
          </v-btn>
        </div>
        <div class="centerBtn">
          <v-btn color="blue darken-1" dark @click="punkt7link">
            Пункт 7
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>
    <v-data-table
      :headers="headers"
      :items="dataTableP5"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Пункт 5</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Поиск"
            single-line
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
      <template v-slot:header>
        <thead color="white">
          <tr>
            <!-- <th class="borderStyle" colspan="4"></th> -->
            <th colspan="5">(ВОЛС) КЛС</th>
            <th colspan="4">ВЛС</th>
            <th colspan="4">РРЛ</th>
            <th colspan="6">Удельный вес протяженности</th>
          </tr>
        </thead>
      </template>
      <template v-slot:body>
        <tbody color="white">
          <tr v-for="item in dataTableP5" :key="item.id">
            <td v-if="item.outfit == null">
              <span>Республика</span>
            </td>
            <td v-else>
              {{item.outfit}}
            </td>
            <td>{{ item.outfit_period_of_time_kls }}</td>
            <td>{{ item.length_kls }}</td>
            <td>{{ item.downtime_kls }}</td>
            <td>{{ item.coefficient_kls }}</td>
            <td>{{ item.outfit_period_of_time_vls }}</td>
            <td>{{ item.length_vls }}</td>
            <td>{{ item.downtime_vls }}</td>
            <td>{{ item.coefficient_vls }}</td>
            <td>{{ item.outfit_period_of_time_rrl }}</td>
            <td>{{ item.length_rrl }}</td>
            <td>{{ item.downtime_rrl }}</td>
            <td>{{ item.coefficient_rrl }}</td>
            <td>{{ item.total_data5.total_length }}</td>
            <td>{{ item.total_data5.kls }}</td>
            <td>{{ item.total_data5.vls }}</td>
            <td>{{ item.total_data5.rrl }}</td>
            <td>{{ item.total_data5.total_coefficient }}</td>
            <td>
              <v-icon class="mr-2" @click.stop="editItem(item)">mdi-pencil</v-icon>
              <v-icon @click="deleteItem(item)">mdi-delete</v-icon>
            </td>
          </tr>
        </tbody>
      </template>
    </v-data-table>
    <DialogP5
    :itemForEdit="itemForEdit"
    v-model="dialog"
    ></DialogP5>
  </v-container>
</template>

<script>
import { bus } from "../../../../main"
import DialogP5 from "./DialogP5";
import router from "../../../../router";

export default {
  components: { DialogP5 },
  props: {},
  data: () => ({
    search: "",
    dialog: false,
    errored: false,
    valid: true,
    isEditing: null,
    headers: [
      {
        text: "Наименование КТ",
        value: "outfit",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Продолжительность всех ПВ кан*час",
        value: "outfit_period_of_time_kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Протяженность кан*км зад.",
        value: "length_kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Простои на 1000 кан*км",
        value: "downtime_kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Коэффициент качества",
        value: "coefficient_kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Продолжительность всех ПВ кан*час",
        value: "outfit_period_of_time_vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Протяженность кан*км",
        value: "length_vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Простои на 1000 кан*км",
        value: "downtime_vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Коэффициент качества",
        value: "coefficient_vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Продолжительность всех ПВ кан*час",
        value: "outfit_period_of_time_rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Протяженность кан*км",
        value: "length_rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Простои на 1000 кан*км",
        value: "downtime_rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Коэффициент качества",
        value: "coefficient_rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Общая протяж. кан*км",
        value: "total_data5.total_length",
        sortable: false,
        class: "black--text",
      },
      {
        text: "КЛС",
        value: "total_data5.kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "ВЛС",
        value: "total_data5.vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "РРЛ",
        value: "total_data5.rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Расчет коэф.качества по ЛКХ (п.5)",
        value: "total_data5.total_coefficient",
        sortable: false,
        class: "black--text",
      },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    dataTableP5: [],
    json_fields: {},
    itemForEdit: {},
    idForP5: "",
    nametable: "", 
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  mounted() {
    this.getIdForP5();
    this.initialize();
    bus.$on("updateOtchetP5",() => {
      this.getIdForP5();
      this.initialize();
    })
  },
  beforeDestroy() {
    bus.$off("updateOtchetP5")
  },

  methods: {
    srKlink() {
      localStorage.setItem("idSrK", JSON.stringify(this.idForP55))
      router.push({ name: "otchetsrk" });
    },
    punkt7link() {
      localStorage.setItem("idPunkt7", JSON.stringify(this.idForP55))
      router.push({ name: "otchetp7" });
    },
    deleteItem(item) {
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/analysis/punkt5/delete/${item.id}/`,
            {
              headers: { Authorization: `Token ${localStorage.token}` },
            }
          )
          .then((response) => {
            if (response.status == "204") {
              this.initialize();
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
    },
    editItem(item) {
      this.itemForEdit = Object.assign({}, item);
      this.dialog = true;
      console.log(this.itemForEdit);
    },
    getIdForP5() {
      this.idForP55 = JSON.parse(localStorage.getItem("idPunkt5"))
      this.idForP5 = JSON.parse(localStorage.getItem("idPunkt5")).id;
      this.nametable = this.idForP55.name
      console.log(this.idForP5);
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/analysis/punkt5/list/${this.idForP5}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.dataTableP5 = response.data;
          console.log(this.dataTableP5);
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

thead tr th {
  border-top: solid 1px #777777dd;
  border-right: solid 1px #777777dd;
  border-left: solid 1px #777777dd;
  font-size: 14px;
}
tbody tr td {
  border: solid 1px #777777dd;
  /* border-right: solid 1px #777777dd;
  border-left: solid 1px #777777dd; */
}

tfoot {
  margin: 10px;
  font-weight: bold;
}
.centerBtn {
  margin-left: auto;
  margin-right: auto;
}
</style>
