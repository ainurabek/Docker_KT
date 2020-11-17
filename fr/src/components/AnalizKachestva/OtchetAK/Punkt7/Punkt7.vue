<template>
  <v-container>
    <v-card class="mb-4">
      <v-card-title>{{nametable}}</v-card-title>
      <v-card-actions>
        <div class="centerBtn">
          <v-btn color="green darken-1" dark @click="srKlink">
            Средний коэф.
          </v-btn>
        </div>
        <div class="centerBtn">
          <v-btn color="orange darken-1" dark @click="punkt5link">
            Пункт 5
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>
    <v-data-table
      :headers="headers"
      :items="dataTableP7"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Пункт 7</v-toolbar-title>
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
            <th colspan="5">КЛС</th>
            <th colspan="4">ВЛС</th>
            <th colspan="4">РРЛ</th>
            <th colspan="6">Удельный вес протяженности</th>
          </tr>
        </thead>
      </template>
      <template v-slot:body>
        <tbody color="white">
          <tr v-for="item in dataTableP7" :key="item.id">
            <td v-if="item.outfit == null">
              <span>Республика</span>
            </td>
            <td v-else>
              {{ item.outfit }}
            </td>
            <td>{{ item.total_number_kls }}</td>
            <td>{{ item.corresponding_norm_kls }}</td>
            <td>{{ item.percentage_compliance_kls }}</td>
            <td>{{ item.coefficient_kls }}</td>
            <td>{{ item.total_number_vls }}</td>
            <td>{{ item.corresponding_norm_vls }}</td>
            <td>{{ item.percentage_compliance_vls }}</td>
            <td>{{ item.coefficient_vls }}</td>
            <td>{{ item.total_number_rrl }}</td>
            <td>{{ item.corresponding_norm_rrl }}</td>
            <td>{{ item.percentage_compliance_rrl }}</td>
            <td>{{ item.coefficient_rrl }}</td>
            <td>{{ item.total_data7.total_length }}</td>
            <td>{{ item.total_data7.kls }}</td>
            <td>{{ item.total_data7.vls }}</td>
            <td>{{ item.total_data7.rrl }}</td>
            <td>{{ item.total_data7.total_coefficient }}</td>
            <td>
              <v-icon class="mr-2" @click.stop="editItem(item)"
                >mdi-pencil</v-icon
              >
              <v-icon @click="deleteItem(item)">mdi-delete</v-icon>
            </td>
          </tr>
        </tbody>
      </template>
    </v-data-table>
    <DialogP7 :itemForEdit="itemForEdit" v-model="dialog"></DialogP7>
  </v-container>
</template>

<script>
import { bus } from "../../../../main";
import DialogP7 from "./DialogP7";
import router from "../../../../router";

export default {
  components: { DialogP7 },
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
        text: "Общее количество линейных трактов",
        value: "total_number_kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "в т.ч.  соответствующих норме",
        value: "corresponding_norm_kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "процент соответствия",
        value: "percentage_compliance_kls",
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
        text: "Общее количество линейных трактов",
        value: "total_number_vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "в т.ч.  соответствующих норме",
        value: "corresponding_norm_vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "процент соответствия",
        value: "percentage_compliance_vls",
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
        text: "Общее количество линейных трактов",
        value: "total_number_rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "в т.ч.  соответствующих норме",
        value: "corresponding_norm_rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "процент соответствия",
        value: "percentage_compliance_rrl",
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
        text: "Общее количество линейных трактов",
        value: "total_data7.total_length",
        sortable: false,
        class: "black--text",
      },
      {
        text: "КЛС",
        value: "total_data7.kls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "ВЛС",
        value: "total_data7.vls",
        sortable: false,
        class: "black--text",
      },
      {
        text: "РРЛ",
        value: "total_data7.rrl",
        sortable: false,
        class: "black--text",
      },
      {
        text: "Расчет коэф.качества по ЛКХ (п.7)",
        value: "total_data7.total_coefficient",
        sortable: false,
        class: "black--text",
      },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    dataTableP7: [],
    json_fields: {},
    itemForEdit: {},
    nametable: "", 
    idForP7: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  mounted() {
    this.getIdForP7();
    this.initialize();
    bus.$on("updateOtchetP7", () => {
      this.getIdForP7();
      this.initialize();
    });
  },
  beforeDestroy() {
    bus.$off("updateOtchetP7");
  },

  methods: {
    srKlink() {
      localStorage.setItem("idSrK", JSON.stringify(this.idForP77));
      router.push({ name: "otchetsrk" });
    },
    punkt5link() {
      localStorage.setItem("idPunkt5", JSON.stringify(this.idForP77));
      router.push({ name: "otchetp5" });
    },
    deleteItem(item) {
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/analysis/punkt7/delete/${item.id}/`,
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
    getIdForP7() {
      this.idForP77 = JSON.parse(localStorage.getItem("idPunkt7"));
      this.idForP7 = JSON.parse(localStorage.getItem("idPunkt7")).id;
      this.nametable = this.idForP77.name
      console.log(this.idForP7);
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/analysis/punkt7/list/${this.idForP7}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.dataTableP7 = response.data;
          console.log(this.dataTableP7);
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
