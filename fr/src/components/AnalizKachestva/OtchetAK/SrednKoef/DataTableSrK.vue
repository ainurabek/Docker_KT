<template>
  <v-container>
   <v-data-table
      :headers="headers"
      :items="dataTableSrK"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Средний  коэффициент  качества  по ЛКХ  и  трактам</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Поиск"
            single-line
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="headline">Изменить коэффициент</span>
              </v-card-title>
              <v-card-text>
                <v-form ref="form" v-model="valid" validation>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          v-model="editedItem.tv_coefficient"
                          label="Коэффициент качества ТВ"
                          type="number"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="6" md="6">
                        <v-text-field
                          v-model="editedItem.average_coefficient"
                          label="Норматив. коэффициент качества"
                          type="number"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                  >Сохранить</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon class="mr-2" @click="editItem(item)"
          >mdi-pencil</v-icon
        >
      </template>
      <template v-slot:[`item.outfit`]="{ item }">
        <span v-if="item.outfit == null" >Республика</span>
        <span v-else>{{item.outfit}}</span>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import { bus } from "../../../../main"

export default {
  props: {

  },
  data: () => ({
    search: "",
    dialog: false,
    errored: false,
    valid: true,
    isEditing: null,
    headers: [
      { text: "Наименование КТ", value: "outfit", sortable: false, class: 'black--text', },
      { text: "Расчет коэф. качества по ЛКХ (п.5)", value: "punkt5.total_data5", sortable: false, class: 'black--text',  },
      { text: "Расчет коэф. качества по ЛКХ (п.7)", value: "punkt7.total_data7", sortable: false, class: 'black--text', },
      { text: "Коэффициент качества ТВ", value: "tv_coefficient", sortable: false, class: 'black--text',},
      { text: "Средний коэффициент качества", value: "coefficient", sortable: false, class: 'black--text',},
      { text: "Норматив. коэффициент качества", value: "average_coefficient", sortable: false, class: 'black--text', },
      { text: "Редактировать", value: "actions", sortable: false },
    ],
    dataTableSrK: [],
    json_fields: {},
    idForEdit: "",
    editedItem: {
      tv_coefficient: null,
      average_coefficient: null
    },
    defaultItem: {
      tv_coefficient: null,
      average_coefficient: null
    },
    idForSrk: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    dialog(val) {
      val || this.close();
    },
  },

  mounted() {
    this.getIdForSrK()
    this.initialize();
    bus.$on("updateOtchetSrK", () => {
      this.getIdForSrK()
      this.initialize();
    })
  },
  beforeDestroy() {
    bus.$off("updateOtchetSrK")
  },

  methods: {
    editItem(item) {
      this.idForEdit = item.id
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
      });
    },
    save() {
      this.$http
        .put(
          `${this.url.baseUrl}/apps/analysis/form/${this.idForEdit}/edit/`,
          {
            tv_coefficient: this.editedItem.tv_coefficient,
            average_coefficient: this.editedItem.average_coefficient
          },
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == 200) {
            this.initialize()
          }
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => {
          this.close()
          this.loading = false
        });
        // this.close()
    },
    getIdForSrK() {
      this.idForSrk = JSON.parse(localStorage.getItem("idSrK")).id
      console.log(this.idForSrk)
    },
    initialize() {
      this.$http
        .get(
          `${this.url.baseUrl}/apps/analysis/form/${this.idForSrk}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.dataTableSrK = response.data;
          console.log(response);
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

</style>
