<template>
  <v-data-table
    :headers="headers"
    :items="detailList"
    :search="search"
    sort-by="calories"
    class="elevation-1"
    hide-default-footer
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-btn color="green" dark class="mb-2" @click="createJourn"
          >Создать событие</v-btn
        >
        <v-dialog v-model="dialog2" max-width="650px">
          <v-card class="mx-auto backCard1 pl-4 pr-4 pt-2" color="blue" dark>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  label="Вид журнала"
                  v-model="editedItem2.type_journal"
                  :items="type_journal"
                  item-value="id"
                  item-text="name"
                >
                </v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-datetime-picker
                  label="Начало"
                  v-model="datetime"
                ></v-datetime-picker>
                <!-- <div>Datetime value: <span>{{datetime}}</span></div> --> </v-col
              ><v-col cols="12" sm="6" md="4">
                <v-datetime-picker
                  label="Конец"
                  v-model="datetime2"
                ></v-datetime-picker>
                <!-- <div>Datetime value: <span>{{datetime2}}</span></div> -->
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  label="Ответственный"
                  v-model="editedItem2.responsible_outfit"
                  :items="outfit"
                  item-value="id"
                  item-text="outfit"
                >
                </v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  label="Передал(предприятие)"
                  v-model="editedItem2.send_from"
                  :items="outfit"
                  item-value="id"
                  item-text="outfit"
                >
                </v-autocomplete> </v-col
              ><v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="ФИО передал"
                  v-model="editedItem2.contact_name"
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  label="Причина"
                  v-model="editedItem2.reason"
                  :items="reason"
                  item-value="id"
                  item-text="name"
                >
                </v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  label="Индекс-1"
                  v-model="editedItem2.index1"
                  :items="index"
                  item-value="id"
                  item-text="index"
                >
                </v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Примечание" v-model="editedItem2.comments">
                </v-text-field>
              </v-col>
            </v-row>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="white" text @click="close2">Отмена</v-btn>
              <v-btn color="white" text @click="saveJourn">Сохранить</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-dialog v-model="dialog" max-width="650px">
          <v-card>
            <v-card-title>
              <span class="headline">Редактировать</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.type_journal"
                      :items="type_journal"
                      item-text="name"
                      item-value="id"
                      dense
                      filled
                      label="Вид журнала"
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.contact_name"
                      dense
                      filled
                      label="ФИО передающего"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.reason"
                      :items="reason"
                      item-text="name"
                      item-value="id"
                      dense
                      filled
                      label="Причина"
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.index1"
                      :items="index"
                      item-text="index"
                      item-value="id"
                      dense
                      filled
                      label="Индекс-1"
                    ></v-autocomplete>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.responsible_outfit"
                      :items="outfit"
                      item-text="outfit"
                      item-value="id"
                      dense
                      filled
                      label="Ответственный"
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      v-model="editedItem.send_from"
                      :items="outfit"
                      item-text="outfit"
                      item-value="id"
                      dense
                      filled
                      label="Передал"
                    ></v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.comments"
                      dense
                      filled
                      label="Комментарий"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
              <v-btn color="blue darken-1" text @click="save">Сохранить</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
      <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
    </template>
    <template v-slot:[`item.created_by`]="{ item }">
      <span
        >{{ item.created_by.first_name }}
        {{ item.created_by.last_name }}
        {{ item.created_by.middle_name }}
      </span>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Обновить</v-btn>
    </template>
  </v-data-table>
</template>

<script>
import { bus } from "../../../main";
// import router from "../../../router";
export default {
  props: {
    propsIdJourn: null,
    propsSelJourn: null,
  },
  data: () => ({
    search: "",
    dialog: false,
    dialog2: false,
    loading: true,
    errored: false,
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Время события", value: "created_at2" },
      { text: "Время сообщения", value: "date_from2" },
      { text: "Индекс 1", value: "index1.index" },

      { text: "Причина", value: "reason.name" },
      { text: "Ответственный", value: "responsible_outfit.outfit" },
      { text: "Передал", value: "send_from.outfit" },
      { text: "ФИО передающего", value: "contact_name.name" },
      { text: "Комментарий", value: "comments.name" },
      { text: "ИП от", value: "point1" },
      { text: "Ип до", value: "point2" },
      { text: "Диспетчер", value: "created_by" },
      { text: "Конец", value: "date_to2" },
      { text: "Редактировать/Удалить", value: "actions", sortable: false },
    ],
    detailList: [],
    outfit: [],

    index: [
      {
        id: 1,
        name: "01",
      },
      {
        id: 2,
        name: "0а",
      },
      {
        id: 3,
        name: "0д",
      },
      {
        id: 4,
        name: "0з",
      },
      {
        id: 5,
        name: "0тв",
      },
      {
        id: 6,
        name: "1",
      },
      {
        id: 7,
        name: "2",
      },
      {
        id: 8,
        name: "2-1",
      },
      {
        id: 9,
        name: "2-5",
      },
      {
        id: 10,
        name: "2-8",
      },
      {
        id: 11,
        name: "4",
      },
      {
        id: 12,
        name: "4-5",
      },
      {
        id: 13,
        name: "4-7",
      },
    ],
    reason: [
      {
        id: 1,
        name: "Линейные повреждения",
      },
      {
        id: 2,
        name: "Рилейные повреждения",
      },
    ],
    type_journal: [
      {
        id: 1,
        name: "По системам",
      },
      {
        id: 2,
        name: "Аренда",
      },
      {
        id: 3,
        name: "ГТС",
      },
      {
        id: 4,
        name: "ТВ и РВ",
      },
      {
        id: 5,
        name: "Телефонограммы",
      },
      {
        id: 6,
        name: "Стихия",
      },
      {
        id: 7,
        name: "Прочее",
      },
      {
        id: 8,
        name: "Автоматика",
      },
      {
        id: 9,
        name: "Телеграф",
      },
      {
        id: 10,
        name: "Ручные каналы",
      },
      {
        id: 11,
        name: "СПД",
      },
    ],
    datetime: null,
    datetime2: null,
    editedItemDate1: null,
    editedItemDate2: null,
    editedItem2: {
      type_journal: "",
      responsible_outfit: "",
      send_from: "",
      reason: "",
      index1: "",

      comments: "",
    },
    clearItem: {
      type_journal: "",
      responsible_outfit: "",
      send_from: "",
      reason: "",
      index1: "",

      comments: "",
    },
    editedIndex: -1,
    editedItem: {
      type_journal: "",
      contact_name: "",
      reason: "",
      index1: "",

      comments: "",
      responsible_outfit: "",
      send_from: "",
    },
    defaultItem: {
      type_journal: "",
      contact_name: "",
      reason: "",
      index1: "",

      comments: "",
      responsible_outfit: "",
      send_from: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
      urlIP: "/apps/dispatching/api/event/ips/create",
      urlObj: "/apps/dispatching/api/event/objects/create",
      urlCirc: "/apps/dispatching/api/event/circuits/create",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Создать" : "Редактировать";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    datetime(newValue) {
      let str = new Date(newValue).toISOString();
      this.editedItemDate1 = str;
      if (str == "1970-01-01T00:00:00.000Z") {
        this.editedItemDate1 = null;
      }
      console.log(this.editedItemDate1);
    },
    datetime2(newValue) {
      let str = new Date(newValue).toISOString();
      this.editedItemDate2 = str;
      if (str == "1970-01-01T00:00:00.000Z") {
        this.editedItemDate2 = null;
      }
      console.log(this.editedItemDate2);
    },
    propsIdJourn() {
      this.initialize();
    },
  },

  mounted() {
    this.initialize();
    this.getOutfit();
  },

  methods: {
    saveJourn() {
      if (this.propsSelJourn.object != null) {
        const id = this.propsSelJourn.object.id;
        this.saveFunc(id, this.url.urlObj);
      } else if (this.propsSelJourn.circuit != null) {
        const id = this.propsSelJourn.circuit.id;
        this.saveFunc(id, this.url.urlCirc);
      } else if (this.propsSelJourn.ips != null) {
        const id = this.propsSelJourn.ips.id;
        this.saveFunc(id, this.url.urlIP);
      }
    },
    saveFunc(idArg, urlFunc) {
      this.$http
        .post(
          `${this.url.baseUrl}${urlFunc}/${idArg}/`,
          {
            type_journal: this.editedItem2.type_journal,
            reason: this.editedItem2.reason,
            date_from: this.editedItemDate1,
            date_to: this.editedItemDate2,
            index1: this.editedItem2.index1,

            responsible_outfit: this.editedItem2.responsible_outfit,
            send_from: this.editedItem2.send_from,
            contact_name: this.editedItem2.contact_name,
            comments: this.editedItem2.comments,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          this.initialize();
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      this.close2();
    },
    getEmitUpdate() {
      bus.$emit("deleteUpdateJourn");
    },
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
    createJourn() {
      this.dialog2 = true;
    },
    dateTrans() {
      for (let i = 0; i < this.detailList.length; i++) {
        if (this.detailList[i].object != null) {
          let pushArray = {
            point2: this.detailList[i].object.point2,
            point1: this.detailList[i].object.point1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].circuit != null) {
          let pushArray = {
            point2: this.detailList[i].circuit.point2,
            point1: this.detailList[i].circuit.point1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].created_at != null) {
          let created_at2 = this.detailList[i].created_at.substring(0, 16);
          let pushArray = {
            created_at2: created_at2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].date_from != null) {
          let date_from2 = this.detailList[i].date_from.substring(0, 16);
          let pushArray = {
            date_from2: date_from2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].date_to != null) {
          let date_to2 = this.detailList[i].date_to.substring(0, 16);
          let pushArray = {
            date_to2: date_to2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
      }
    },
    initialize() {
      let id = this.propsIdJourn;
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/detail/${id}/`)
        .then((response) => {
          this.detailList = response.data;
          this.dateTrans();
          console.log(this.detailList);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem(item) {
      this.editedIndex = this.detailList.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/dispatching/api/event/delete/${index}/`,
            {
              headers: { Authorization: `Token ${localStorage.token}` },
            }
          )
          .then((response) => {
            if (response.status == "204") {
              this.getEmitUpdate();
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
    },
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    close2() {
      this.dialog2 = false;
      this.$nextTick(() => {
        this.editedItem2 = Object.assign({}, this.clearItem);
      });
    },
    funcSortEdit(name) {
      if (name == undefined) {
        name = null;
      } else if (name.id != undefined) {
        name = name.id;
      }
    },

    save() {
      if (this.editedIndex > -1) {
        const index = this.detailList[this.editedIndex].id;
        if (this.editedItem.type_journal == undefined) {
          this.editedItem.type_journal = null;
        } else if (this.editedItem.type_journal.id != undefined) {
          this.editedItem.type_journal = this.editedItem.type_journal.id;
        }
        if (this.editedItem.reason == undefined) {
          this.editedItem.reason = null;
        } else if (this.editedItem.reason.id != undefined) {
          this.editedItem.reason = this.editedItem.reason.id;
        }
        if (this.editedItem.index1 == undefined) {
          this.editedItem.index1 = null;
        } else if (this.editedItem.index1.id != undefined) {
          this.editedItem.index1 = this.editedItem.index1.id;
        }

        if (this.editedItem.responsible_outfit == undefined) {
          this.editedItem.responsible_outfit = null;
        } else if (this.editedItem.responsible_outfit.id != undefined) {
          this.editedItem.responsible_outfit = this.editedItem.responsible_outfit.id;
        }

        if (this.editedItem.send_from == undefined) {
          this.editedItem.send_from = null;
        } else if (this.editedItem.send_from.id != undefined) {
          this.editedItem.send_from = this.editedItem.send_from.id;
        }
        console.log(
          "type_journal",
          this.editedItem.type_journal,
          "contact_name",
          this.editedItem.contact_name,
          "reason",
          this.editedItem.reason,
          "index1",
          this.editedItem.index1,

          "comments",
          this.editedItem.comments,
          "responsible_outfit",
          this.editedItem.responsible_outfit,
          "send_from",
          this.editedItem.send_from
        );
        this.$http
          .put(
            `${this.url.baseUrl}/apps/dispatching/api/event/edit/${index}/`,
            {
              type_journal: this.editedItem.type_journal,
              contact_name: this.editedItem.contact_name,
              reason: this.editedItem.reason,
              index1: this.editedItem.index1,

              comments: this.editedItem.comments,
              responsible_outfit: this.editedItem.responsible_outfit,
              send_from: this.editedItem.send_from,
            },
            {
              headers: {
                Authorization: `Token ${localStorage.token}`,
              },
            }
          )
          .then((response) => {
            if (response.status == "200") {
              this.initialize();
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
      } else {
        console.log("post");
      }
      this.close();
    },
  },
};
</script>

<style scoped></style>
