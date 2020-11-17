<template>
  <v-data-table
    :headers="headers"
    :items="detailList"
    :search="search"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="green" dark class="mb-2" @click="createJourn"
          >Второй звонок</v-btn
        >
        <v-dialog v-model="dialogEdit" persistent max-width="600px">
          <v-card>
            <v-card-title>
              <span class="headline"></span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field
                      label="Начало, дата и время"
                      type="datetime-local"
                      v-model="datetime"
                      outlined
                      dense
                      min="1990-06-01T08:30"
                      max="2099-06-30T16:30"
                    ></v-text-field>
                  </v-col>
                  <!-- <v-col cols="12" sm="6" md="6">
                  <v-text-field
                    label="Конец, дата и время"
                    type="datetime-local"
                    v-model="datetime2"
                    name="date2"
                    outlined
                    dense
                    readonly
                    min="1990-06-01T08:30"
                    max="2099-06-30T16:30"
                  ></v-text-field>
                </v-col> -->
                  <v-col cols="12" sm="6" md="6">
                    <v-autocomplete
                      label="Индекс-1"
                      v-model="editedItem.index1"
                      :items="index"
                      item-value="id"
                      item-text="index"
                      dense
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      label="Вид журнала"
                      v-model="editedItem.type_journal"
                      :items="type_journal"
                      item-value="id"
                      item-text="name"
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      label="Ответственный"
                      v-model="editedItem.responsible_outfit"
                      :items="outfit"
                      item-value="id"
                      item-text="outfit"
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      label="Передал(предприятие)"
                      v-model="send_fromG"
                      :items="outfit"
                      item-value="id"
                      item-text="outfit"
                    >
                    </v-autocomplete> </v-col
                  ><v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      label="ФИО передал"
                      v-model="editedItem.contact_name"
                      :items="usersOutfit"
                      item-value="id"
                      item-text="name"
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      label="Причина"
                      v-model="editedItem.reason"
                      :items="reason"
                      item-value="id"
                      item-text="name"
                    >
                    </v-autocomplete>
                  </v-col>

                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      item-text="point"
                      item-value="id"
                      :items="ip"
                      label="ИП от"
                      v-model="editedItem.point1"
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-autocomplete
                      item-text="point"
                      item-value="id"
                      :items="ip"
                      label="ИП до"
                      v-model="editedItem.point2"
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" md="8">
                    <v-combobox
                      label="Примечание"
                      v-model="editedItem.comments1"
                      :items="comments"
                      item-text="name"
                      item-value="name"
                      :return-object="false"
                    >
                    </v-combobox>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeEdit"
                >Отмена</v-btn
              >
              <v-btn color="blue darken-1" text @click="saveJourn"
                >Сохранить</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
      <v-icon @click="deleteItem(item)">mdi-delete</v-icon>
    </template>
    <template v-slot:[`item.created_by`]="{ item }">
      <span
        >{{ item.created_by.first_name }}
        {{ item.created_by.last_name }}
        {{ item.created_by.middle_name }}
      </span>
    </template>
    <template v-slot:[`item.point`]="{ item }">
      <span>{{ item.point11 }}-{{ item.point22 }} </span>
    </template>
    <template v-slot:no-data>
      <!-- <v-btn color="primary" @click="initialize">Обновите страницу</v-btn> -->
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
    page: 1,
    dialogCreate: false,
    dialogEdit: false,
    loading: true,
    errored: false,
    headers: [
      {
        align: "left",
        sortable: false,
        text: "Начало",
        value: "date_from2",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Конец",
        value: "date_to2",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Индекс 1",
        value: "index1.index",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Причина",
        value: "reason.name",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Ответ-ый",
        value: "responsible_outfit.outfit",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Передал",
        value: "send_from.outfit",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "ФИО перед-го",
        value: "contact_name.name",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Примечание",
        value: "comments1",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Участок",
        value: "point",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Диспетчер",
        value: "created_by",
        width: "1%",
      },
      {
        align: "left",
        sortable: false,
        text: "Изменить/Удалить",
        value: "actions",
        width: "1%",
      },
    ],
    detailList: [],
    detailListObj: "",
    outfit: [],
    usersOutfit: [],
    comments: [],
    ip: [],
    send_fromG: "",
    flag: "",
    idForEdit: "",
    lengthDataList: 0,
    pageNumber: 1,
    index: [],
    reason: [],
    type_journal: [],
    datetime: null,
    datetime2: null,
    editedItemDate1: null,
    editedItemDate2: null,
    idSendFromG: "",
    idObjCreate: null,
    idIPCreate: null,
    idCirCreate: null,
    editedItem2: {
      type_journal: "",
      responsible_outfit: "",
      send_from: "",
      contact_name: "",
      reason: "",
      index1: "",
      comments1: "",
      point1: "",
      point2: "",
    },
    clearItem: {
      type_journal: "",
      responsible_outfit: "",
      send_from: "",
      contact_name: "",
      reason: "",
      index1: "",
      comments1: "",
      point1: "",
      point2: "",
    },
    editedIndex: -1,
    editedItem: {
      type_journal: "",
      responsible_outfit: "",
      send_from: "",
      contact_name: "",
      reason: "",
      index1: "",
      comments1: "",
      point1: "",
      point2: "",
    },
    defaultItem: {
      type_journal: "",
      responsible_outfit: "",
      send_from: "",
      contact_name: "",
      reason: "",
      index1: "",
      comments1: "",
      point1: "",
      point2: "",
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
      // urlIP: "/apps/dispatching/api/event/ips/create",
      // urlObj: "/apps/dispatching/api/event/objects/create",
      // urlCirc: "/apps/dispatching/api/event/circuits/create",
      // urlUnc: "/apps/dispatching/api/event/unknown/create/",
      urlCalls: "/apps/dispatching/api/event/calls/create",
    },
  }),

  computed: {},

  watch: {
    page(newValue) {
      this.detailListObj = this.detailList[newValue - 1];
      console.log(this.detailListObj);
    },
    send_fromG(newValue) {
      if (newValue != "") {
        this.editedItem.send_from = newValue;
        this.editedItem2.send_from = newValue;
        this.sendFormGet();
      }
    },
    datetime(newValue) {
      if (newValue != null) {
        // let str = new Date(newValue).toISOString();
        this.editedItemDate1 = newValue;
      } else if (newValue == null) {
        this.editedItemDate1 = null;
      }
      console.log(this.editedItemDate1);
    },
    datetime2(newValue) {
      if (newValue != null) {
        // let str = new Date(newValue).toISOString();
        this.editedItemDate2 = newValue;
        // if (str == "1970-01-01T00:00:00.000Z") {
        //   this.editedItemDate2 = null;
        // }
      } else if (newValue == null) {
        this.editedItemDate2 = null;
      }
      console.log(newValue);
    },
    propsIdJourn() {
      this.initialize();
    },
  },

  mounted() {
    this.initialize();
    this.getOutfit();
    this.pointGet();
    this.commentsList();
    this.getIndex();
    this.getReason();
    this.getTypeJournal();
  },

  methods: {
    getTypeJournal() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/type_journal/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.type_journal = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getReason() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/reason/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.reason = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
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
    commentsList() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/comment/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.comments = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    sendFormGet() {
      if (this.send_fromG.id != null) {
        this.idSendFromG = this.send_fromG.id;
      } else {
        this.idSendFromG = this.send_fromG;
      }
      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/outfit_worker/${this.idSendFromG}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.usersOutfit = response.data;

          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    pointGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/point/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.ip = response.data;
          console.log(this.ip);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    editItem(item) {
      this.idForEdit = item.id;
      this.datetime = item.date_from;
      this.datetime2 = item.date_to;
      this.send_fromG = item.send_from;
      this.editedItem = Object.assign({}, item);
      this.flagEditCreate = 2;
      this.dialogEdit = true;
      console.log(this.editedItem);
    },
    closeEdit() {
      this.dialogEdit = false;
      this.$nextTick(() => {
        this.idObjCreate = null;
        this.idIPCreate = null;
        this.idCirCreate = null;
        this.datetime2 = null;
        this.datetime = null;
        this.send_fromG = "";
        this.flagEditCreate = "";
        this.editedItem = Object.assign({}, this.defaultItem);
      });
    },
    editSave() {
      let id = this.idForEdit;
      if (this.editedItem.type_journal == undefined) {
        this.editedItem.type_journal = "";
      } else if (this.editedItem.type_journal.id != undefined) {
        this.editedItem.type_journal = this.editedItem.type_journal.id;
      }
      if (this.editedItem.reason == undefined) {
        this.editedItem.reason = "";
      } else if (this.editedItem.reason.id != undefined) {
        this.editedItem.reason = this.editedItem.reason.id;
      }
      if (this.editedItem.index1 == undefined) {
        this.editedItem.index1 = "";
      } else if (this.editedItem.index1.id != undefined) {
        this.editedItem.index1 = this.editedItem.index1.id;
      }
      if (this.editedItem.responsible_outfit == undefined) {
        this.editedItem.responsible_outfit = "";
      } else if (this.editedItem.responsible_outfit.id != undefined) {
        this.editedItem.responsible_outfit = this.editedItem.responsible_outfit.id;
      }
      if (this.editedItem.send_from == undefined) {
        this.editedItem.send_from = "";
      } else if (this.editedItem.send_from.id != undefined) {
        this.editedItem.send_from = this.editedItem.send_from.id;
      }
      if (this.editedItem.point1 == undefined) {
        this.editedItem.point1 = "";
      } else if (this.editedItem.point1.id != undefined) {
        this.editedItem.point1 = this.editedItem.point1.id;
      }
      if (this.editedItem.point2 == undefined) {
        this.editedItem.point2 = "";
      } else if (this.editedItem.point2.id != undefined) {
        this.editedItem.point2 = this.editedItem.point2.id;
      }
      if (this.editedItem.contact_name == undefined) {
        this.editedItem.type_journal = "";
      } else if (this.editedItem.contact_name.id != undefined) {
        this.editedItem.contact_name = this.editedItem.contact_name.id;
      }
      if (this.editedItem.comments1 == undefined) {
        this.editedItem.comments1 = "";
      } else if (this.editedItem.comments1.id != undefined) {
        this.editedItem.comments1 = this.editedItem.comments1.id;
      }
      console.log(
        "type_journal",
        this.editedItem.type_journal,
        "reason",
        this.editedItem.reason,
        "date_from",
        this.editedItemDate1,
        "date_to",
        this.editedItemDate2,
        "index1",
        this.editedItem.index1,
        "responsible_outfit",
        this.editedItem.responsible_outfit,
        "send_from",
        this.editedItem.send_from,
        "point1",
        this.editedItem.point1,
        "point2",
        this.editedItem.point2,
        "contact_name",
        this.editedItem.contact_name,
        "comments1",
        this.editedItem.comments1
        // "object",
        // this.idObjCreate,
        // "ips",
        // this.idIPCreate,
        // "circuit",
        // this.idCirCreate,
        // "id",
        // id
      );
      this.$http
        .put(
          `${this.url.baseUrl}/apps/dispatching/api/event/edit/${id}/`,
          {
            type_journal: this.editedItem.type_journal,
            reason: this.editedItem.reason,
            date_from: this.editedItemDate1,
            date_to: this.editedItemDate2,
            index1: this.editedItem.index1,
            responsible_outfit: this.editedItem.responsible_outfit,
            send_from: this.editedItem.send_from,
            point1: this.editedItem.point1,
            point2: this.editedItem.point2,
            contact_name: this.editedItem.contact_name,
            comments1: this.editedItem.comments1,
            // object: this.idObjCreate,
            // ips: this.idIPCreate,
            // circuit: this.idCirCreate,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == 200) {
            this.initialize();
            this.updateJourn();
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      this.closeEdit();
    },
    consss() {
      let tzoffset = new Date().getTimezoneOffset() * 60000;
      var localISOTime = new Date(Date.now() - tzoffset)
        .toISOString()
        .slice(0, 16);
      this.editedItemDate1 = localISOTime;
      this.datetime = localISOTime;
      console.log(localISOTime);
    },
    saveJourn() {
      if (this.flagEditCreate == 1) {
        if (this.propsSelJourn.object != null) {
          const id = this.propsSelJourn.object.id;
          this.idObjCreate = id;
          this.saveFunc(this.propsSelJourn.id, this.url.urlCalls);
        } else if (this.propsSelJourn.circuit != null) {
          const id = this.propsSelJourn.circuit.id;
          this.idCirCreate = id;
          this.saveFunc(this.propsSelJourn.id, this.url.urlCalls);
        } else if (this.propsSelJourn.ips != null) {
          const id = this.propsSelJourn.ips.id;
          this.idIPCreate = id;
          this.saveFunc(this.propsSelJourn.id, this.url.urlCalls);
        } else if (this.propsSelJourn.name != null) {
          // const id = this.propsSelJourn.id;
          this.saveFunc(this.propsSelJourn.id, this.url.urlCalls);
        }
      } else if (this.flagEditCreate == 2) {
        if (this.propsSelJourn.object != null) {
          const id = this.propsSelJourn.id;
          this.idObjCreate = id;
        } else if (this.propsSelJourn.circuit != null) {
          const id = this.propsSelJourn.id;
          this.idCirCreate = id;
        } else if (this.propsSelJourn.ips != null) {
          const id = this.propsSelJourn.id;
          this.idIPCreate = id;
        }
        this.editSave();
      }
    },
    saveFunc(idArg, urlFunc) {
      let id = this.detailListObj.id;
      if (this.editedItem.type_journal == undefined) {
        this.editedItem.type_journal = "";
      } else if (this.editedItem.type_journal.id != undefined) {
        this.editedItem.type_journal = this.editedItem.type_journal.id;
      }
      if (this.editedItem.reason == undefined) {
        this.editedItem.reason = "";
      } else if (this.editedItem.reason.id != undefined) {
        this.editedItem.reason = this.editedItem.reason.id;
      }
      if (this.editedItem.index1 == undefined) {
        this.editedItem.index1 = "";
      } else if (this.editedItem.index1.id != undefined) {
        this.editedItem.index1 = this.editedItem.index1.id;
      }
      if (this.editedItem.responsible_outfit == undefined) {
        this.editedItem.responsible_outfit = "";
      } else if (this.editedItem.responsible_outfit.id != undefined) {
        this.editedItem.responsible_outfit = this.editedItem.responsible_outfit.id;
      }
      if (this.editedItem.send_from == undefined) {
        this.editedItem.send_from = "";
      } else if (this.editedItem.send_from.id != undefined) {
        this.editedItem.send_from = this.editedItem.send_from.id;
      }
      if (this.editedItem.point1 == undefined) {
        this.editedItem.point1 = "";
      } else if (this.editedItem.point1.id != undefined) {
        this.editedItem.point1 = this.editedItem.point1.id;
      }
      if (this.editedItem.point2 == undefined) {
        this.editedItem.point2 = "";
      } else if (this.editedItem.point2.id != undefined) {
        this.editedItem.point2 = this.editedItem.point2.id;
      }
      if (this.editedItem.contact_name == undefined) {
        this.editedItem.type_journal = "";
      } else if (this.editedItem.contact_name.id != undefined) {
        this.editedItem.contact_name = this.editedItem.contact_name.id;
      }
      if (this.editedItem.comments1 == undefined) {
        this.editedItem.comments1 = "";
      } else if (this.editedItem.comments1.id != undefined) {
        this.editedItem.comments1 = this.editedItem.comments1.id;
      }
      console.log(
        "type_journal",
        this.editedItem.type_journal,
        "reason",
        this.editedItem.reason,
        "date_from",
        this.editedItemDate1,
        "date_to",
        this.editedItemDate2,
        "index1",
        this.editedItem.index1,
        "responsible_outfit",
        this.editedItem.responsible_outfit,
        "send_from",
        this.editedItem.send_from,
        "point1",
        this.editedItem.point1,
        "point2",
        this.editedItem.point2,
        "contact_name",
        this.editedItem.contact_name,
        "comments1",
        this.editedItem.comments1,
        "object",
        this.idObjCreate,
        "ips",
        this.idIPCreate,
        "circuit",
        this.idCirCreate
      );
      this.$http
        .post(
          `${this.url.baseUrl}${urlFunc}/${idArg}/${id}/`,
          {
            type_journal: this.editedItem.type_journal,
            reason: this.editedItem.reason,
            date_from: this.editedItemDate1,
            date_to: this.editedItemDate2,
            index1: this.editedItem.index1,
            responsible_outfit: this.editedItem.responsible_outfit,
            send_from: this.editedItem.send_from,
            point1: this.editedItem.point1,
            point2: this.editedItem.point2,
            contact_name: this.editedItem.contact_name,
            comments1: this.editedItem.comments1,
            object: this.idObjCreate,
            ips: this.idIPCreate,
            circuit: this.idCirCreate,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            this.initialize();
            this.updateJourn();
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      this.closeEdit();
    },
    updateJourn() {
      bus.$emit("updateJourn");
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
      this.consss();
      this.datetime2 = this.detailListObj.date_to;
      this.send_fromG = this.detailListObj.send_from;
      this.editedItem = Object.assign({}, this.detailListObj);
      this.flagEditCreate = 1;
      this.dialogEdit = true;
      // if (this.detailListObj.date_from != null) {
      //   let tzoffset = this.detailListObj.date_from
      //   new Date.getTimezoneOffset() * 60000;
      // var localISOTime = (new Date(Date.now() - tzoffset)).toISOString().slice(0, -1);
      // this.editedItemDate1 = localISOTime
      //   console.log(tzoffset)
      // }
      // console.log(tzoffset)
      console.log(this.editedItem);
    },
    dateTrans() {
      for (let i = 0; i < this.detailList.length; i++) {
        if (this.detailList[i].created_at != null) {
          let created_at2 = this.detailList[i].created_at.substring(0, 16);
          let pushArray = {
            created_at2: created_at2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].date_from != null) {
          let date_from2 =
            this.detailList[i].date_from.substring(0, 10) +
            " " +
            this.detailList[i].date_from.substring(11, 16);
          let pushArray = {
            date_from2: date_from2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].date_to != null) {
          let date_to2 =
            this.detailList[i].date_to.substring(0, 10) +
            " " +
            this.detailList[i].date_to.substring(11, 16);
          let pushArray = {
            date_to2: date_to2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].index1 != null) {
          let index11 = this.detailList[i].index1.index;
          let pushArray = {
            index11: index11,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].responsible_outfit != null) {
          let responsible_outfit1 = this.detailList[i].responsible_outfit
            .outfit;
          let pushArray = {
            responsible_outfit1: responsible_outfit1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].contact_name != null) {
          let contact_name1 = this.detailList[i].contact_name.name;
          let pushArray = {
            contact_name1: contact_name1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].send_from != null) {
          let send_from1 = this.detailList[i].send_from.outfit;
          let pushArray = {
            send_from1: send_from1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].type_journal != null) {
          let type_journal1 = this.detailList[i].type_journal.name;
          let pushArray = {
            type_journal1: type_journal1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].point1 != null) {
          let point1 = this.detailList[i].point1.point;
          let pushArray = {
            point11: point1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].point2 != null) {
          let point2 = this.detailList[i].point2.point;
          let pushArray = {
            point22: point2,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].reason != null) {
          let reason1 = this.detailList[i].reason.name;
          let pushArray = {
            reason1: reason1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        if (this.detailList[i].created_by != null) {
          let created_by1 =
            this.detailList[i].created_by.first_name +
            " " +
            this.detailList[i].created_by.last_name;
          let pushArray = {
            created_by1: created_by1,
          };
          Object.assign(this.detailList[i], pushArray);
        }
        this.lengthDataList = this.detailList.length;
        this.detailListObj = this.detailList[0];
        console.log(this.detailListObj);
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
    editItemFunc(item) {
      this.editedIndex = this.detailList.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const id = item.id;
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/dispatching/api/event/delete/${id}/`,
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
  },
};
</script>

<style scoped>
.textSize {
  font-size: 5px;
}
.padd {
  padding: 10px;
}
.editpoback {
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.hrline {
  margin-top: 5px;
  margin-bottom: 5px;
}
.fontSizeText {
  font-size: 14px;
}
.fontheader {
  font-size: 16px;
  /* margin-left: 8px;
  margin-right: 10px; */
  color: darkcyan;
}
.back {
  background-color: aliceblue;
}
.fixed {
  position: fixed;
}
.fontsiz {
  font-size: 16px;
  margin-right: 8px;
  color: black;
}
.custom-highlight-row {
  background-color: pink;
}
.pointer {
  cursor: pointer;
}
.backCard1 {
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  padding-top: 10px;
}
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
</style>
