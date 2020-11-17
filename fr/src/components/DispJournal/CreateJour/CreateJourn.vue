<template>
  <v-container fluid class="ml-3 mr-3">
    <v-row justify="center">
      <v-col cols="12" sm="6" md="8">
        <FiltrCirc v-if="radioGroup == 2"></FiltrCirc>
        <FiltrIP v-if="radioGroup == 3"></FiltrIP>
        <FiltrObj v-if="radioGroup == 1"></FiltrObj>
        <FiltrNameUnk v-if="radioGroup == 4"></FiltrNameUnk>
        <!-- <span>{{filtrCirc}}</span> -->
      </v-col>
      <v-divider vertical></v-divider>
      <v-col cols="12" sm="6" md="3">
        <v-radio-group v-model="radioGroup" value="3">
          <v-radio
            v-for="item in radioArray"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          ></v-radio>
        </v-radio-group>
      </v-col>
    </v-row>
    <v-col v-if="radioGroup == 2 || radioGroup == 1">
      <v-card color="white" class="mx-auto backCard1">
        <v-card-text>
          <div>
            <span class="fontsiz">Трасса:</span>
            <span class="fontsiz" v-for="item in trassa" :key="item.indexOf"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</span
            >
          </div>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col v-else-if="radioGroup == 3">
      <v-card color="white" class="mx-auto backCard1">
        <v-card-text>
          <div>
            <span class="fontsiz">Название:</span>
            <span class="fontsiz">
              {{ nameIP }}
            </span>
          </div>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col>
      <DataTableCirc v-if="radioGroup == 2"></DataTableCirc>
      <DataTableIP v-if="radioGroup == 3"></DataTableIP>
      <DataTableObj v-if="radioGroup == 1"></DataTableObj>
      <div v-if="radioGroup == 4">
        <v-text-field
          height="60px"
          v-model="textFieldUnk"
          label="Текст"
          :outlined="true"
          :rounded="false"
          :clearable="true"
          :solo="true"
        ></v-text-field>
      </div>
    </v-col>
    <v-row justify="center"
      ><v-col cols="12" sm="6" md="11">
        <v-card class="mx-auto backCard1 pl-4 pr-4 pt-2" color="blue" dark>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Дата создания"
                type="date"
                v-model="datetimeCreate"
                outlined
                dense
                min="1990-06-01"
                max="2099-06-30"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Начало, дата и время"
                type="datetime-local"
                v-model="datetime"
                outlined
                dense
                min="1990-06-01T08:30"
                max="2099-06-30T16:30"
              ></v-text-field>
              <!-- <div>Datetime value: <span>{{datetime}}</span></div> -->
            </v-col>

            <v-col cols="12" sm="6" md="2">
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
            <v-col cols="12" sm="6" md="2">
              <v-autocomplete
                label="Вид журнала"
                v-model="editedItem.type_journal"
                :items="type_journal"
                item-value="id"
                item-text="name"
                dense
              >
              </v-autocomplete>
            </v-col>

            <!-- <v-col cols="12" sm="6" md="4">
              <v-text-field
                label="Конец, дата и время"
                type="datetime-local"
                v-model="datetime2"
                outlined
                class="datetime"
                name="date2"
                dense
                min="1990-06-01T08:30" max="2099-06-30T16:30"
              ></v-text-field>
            </v-col> -->
            <!-- <v-col cols="12" sm="6" md="4">
              <v-datetime-picker
                label="Конец"
                v-model="datetime2"
              ></v-datetime-picker>
               -->
            <!-- </v-col> -->
            <v-col cols="12" sm="6" md="2">
              <v-autocomplete
                label="Ответственный"
                v-model="editedItem.responsible_outfit"
                :items="outfit"
                item-value="id"
                item-text="outfit"
                dense
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6" md="2">
              <v-autocomplete
                label="Передал(предприятие)"
                v-model="send_fromG"
                :items="outfit"
                item-value="id"
                item-text="outfit"
                dense
              >
              </v-autocomplete> </v-col
            ><v-col cols="12" sm="6" md="2">
              <v-autocomplete
                label="ФИО передал"
                v-model="editedItem.contact_name"
                :items="usersOutfit"
                item-value="id"
                item-text="name"
                dense
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6" md="2">
              <v-autocomplete
                label="Причина"
                v-model="editedItem.reason"
                :items="reason"
                item-value="id"
                item-text="name"
                dense
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6" md="2">
              <v-autocomplete
                item-text="point"
                item-value="id"
                :items="ip"
                label="ИП от"
                dense
                v-model="editedItem.point1"
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6" md="2">
              <v-autocomplete
                item-text="point"
                item-value="id"
                :items="ip"
                label="ИП до"
                v-model="editedItem.point2"
                dense
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-combobox
                label="Примечание"
                v-model="editedItem.comments1"
                :items="comments"
                item-text="name"
                item-value="name"
                dense
                :return-object="false"
              >
              </v-combobox>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" sm="6" md="11"
        ><v-btn color="success" class="mr-12" @click="saveJourn"
          >Сохранить</v-btn
        >
        <v-btn color="primary" class="mr-12" @click="clearItemFun"
          >Очистить</v-btn
        >
        <v-btn color="orange" @click="initialize">Отмена</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FiltrCirc from "../CreateJour/FiltrCirc";
import FiltrIP from "../CreateJour/FiltrIP";
import FiltrObj from "../CreateJour/FiltrObj";
import FiltrNameUnk from "../CreateJour/FiltrNameUnk";
import DataTableCirc from "../CreateJour/DataTableCirc";
import DataTableIP from "../CreateJour/DataTableIP";
import DataTableObj from "../CreateJour/DataTableObj";

import { bus } from "../../../main";
import router from "../../../router";
export default {
  components: {
    FiltrCirc,
    DataTableCirc,
    FiltrIP,
    DataTableIP,
    FiltrObj,
    DataTableObj,
    FiltrNameUnk,
  },
  data: () => ({
    datetime: new Date(),
    datetime2: null,
    datetime12: null,
    datetime23: null,
    isEditing: null,
    datetimeCreate: new Date(),
    point: [],
    obj: [],
    circ: [],
    outfit: [],
    trassa: [],
    trassaBus: [],
    radioArray: [
      {
        id: 1,
        name: "Список КО",
      },
      {
        id: 2,
        name: "Список Каналов",
      },
      {
        id: 3,
        name: "Список ИП",
      },
      {
        id: 4,
        name: "Другое",
      },
    ],
    radioGroup: 3,
    usersOutfit: [],
    ip: [],
    comments: [],
    idOutfitWorker: "",
    textFieldUnk: "",
    index: [],
    reason: [],
    type_journal: [],
    nameIP: "",
    editedItemDate1: null,
    editedItemDate2: null,
    editedItemDateCreate: null,
    editedItemIdCirc: "",
    editedItemIdObj: "",
    editedItemIdPoint: "",
    editedItemId: "",
    editedItemIdRas: "",
    send_fromG: "",
    objectDataKo: "",
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
    urlBus: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
      urlIP: "/apps/dispatching/api/event/ips/create",
      urlObj: "/apps/dispatching/api/event/objects/create",
      urlCirc: "/apps/dispatching/api/event/circuits/create",
      urlUnk: "/apps/dispatching/api/event/unknown/create",
    },
  }),

  mounted() {
    bus.$on("objectData", (data) => {
      if (data.id != null) {
        this.objectDataKo = data;

        this.editedItem.type_journal = this.type_journal[0];
        this.editedItem.point1 = data.point1;
        this.editedItem.point2 = data.point2;
        this.editedItem.responsible_outfit = data.id_outfit;
        this.send_fromG = data.id_outfit;
        console.log(data);
      } else if (data.length < 1) {
        this.send_fromG = "";
        this.nameIP = "";
        this.editedItem = Object.assign({}, this.clearItem);
      }
    });
    bus.$on("trassaDisp", (data) => {
      this.trassa = data;
      console.log(data);
    });
    bus.$on("dispDataCirc", (data) => {
      if (data.id != null) {
        this.editedItem.type_journal = this.type_journal[0];
        this.editedItem.point1 = data.point1;
        this.editedItem.point2 = data.point2;
        this.editedItem.responsible_outfit = data.id_object.id_outfit;
        this.send_fromG = data.id_object.id_outfit;
        console.log(data);
      } else if (data.length < 1) {
        this.send_fromG = "";
        this.nameIP = "";
        this.editedItem = Object.assign({}, this.clearItem);
      }
    });
    bus.$on("trassaDispCirc", (data) => {
      this.trassa = data;
      console.log(data);
    });
    bus.$on("idObj", (data) => {
      this.editedItemId = data;
      this.urlBus = this.url.urlObj;
      console.log(data);
    });
    bus.$on("idCirc", (data) => {
      this.editedItemId = data;
      this.urlBus = this.url.urlCirc;
      console.log(data);
    });
    bus.$on("idIP", (data) => {
      this.editedItemId = data;
      this.urlBus = this.url.urlIP;
      console.log(data);
    });
    bus.$on("dispIpData", (data) => {
      console.log(data);
      if (data.id != null) {
        this.nameIP = data.point_id.name;
        this.editedItem.type_journal = this.type_journal[0];
        this.editedItem.point1 = data.object_id.point1;
        this.editedItem.point2 = data.object_id.point2;
        this.editedItem.responsible_outfit = data.object_id.id_outfit;
        this.send_fromG = data.object_id.id_outfit;
        console.log(data);
      } else if (data.length < 1) {
        this.send_fromG = "";
        this.nameIP = "";
        this.editedItem = Object.assign({}, this.clearItem);
      }
    });
    this.initialize();
    this.circGet();
    this.objectGet();
    this.outfitGet();
    this.pointGet();
    this.commentsList();
    this.consss();
    this.getIndex();
    this.getReason();
    this.getTypeJournal();
  },
  beforeDestroy() {
    bus.$off("objectData");
    bus.$off("trassaDisp");
    bus.$off("dispDataCirc");
    bus.$off("trassaDispCirc");
    bus.$off("idObj");
    bus.$off("idCirc");
    bus.$off("idIP");
    bus.$off("dispIpData");
  },
  watch: {
    send_fromG(newValue) {
      if (newValue != "") {
        this.editedItem.send_from = newValue;
        this.sendFormGet();
      }
    },
    datetimeCreate(newValue) {
      if (newValue != null) {
        this.editedItemDateCreate = newValue;
        console.log(newValue);
      } else if (newValue == null) {
        this.editedItemDateCreate = null;
      }
      console.log(this.editedItemDateCreate);
    },
    datetime(newValue) {
      if (newValue != null) {
        this.editedItemDate1 = newValue;
        console.log(newValue);
      } else if (newValue == null) {
        this.editedItemDate1 = null;
      }
      console.log(this.editedItemDate1);
    },
    datetime2(newValue) {
      if (newValue != null) {
        this.editedItemDate2 = newValue;
      } else if (newValue == null) {
        this.editedItemDate2 = null;
      }
      console.log(this.editedItemDate2);
    },
    radioGroup() {
      this.editedItemId = "";
      this.trassa = [];
    },
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
    consss() {
      if (this.datetime != null) {
        let tzoffset = this.datetime.getTimezoneOffset() * 60000;
        var localISOTime = new Date(Date.now() - tzoffset)
          .toISOString()
          .slice(0, 16);
        this.datetimeCreate = localISOTime.slice(0, 10);
        this.datetime = localISOTime;
        this.editedItemDate1 = localISOTime;
      }
      console.log(localISOTime);
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
      if (this.send_fromG.id != undefined) {
        this.idOutfitWorker = this.send_fromG.id;
      } else {
        this.idOutfitWorker = this.send_fromG;
      }
      this.$http
        .get(
          `${this.url.baseUrl}/apps/dispatching/api/outfit_worker/${this.idOutfitWorker}/`,
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
    pushFunc() {
      let nullObj = {
        id: null,
        point: "",
      };
      this.ip.push(nullObj);
    },
    pointGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/point/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.ip = response.data;
          this.pushFunc();
          console.log(this.ip);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    saveJourn() {
      if (this.radioGroup == 1) {
        // this.cons()
        const id = this.editedItemId;
        this.saveFunc(id, this.url.urlObj);
      } else if (this.radioGroup == 2) {
        const id = this.editedItemId;
        this.saveFunc(id, this.url.urlCirc);
      } else if (this.radioGroup == 3) {
        const id = this.editedItemId;
        this.saveFunc(id, this.url.urlIP);
      } else if (this.radioGroup == 4) {
        this.saveFuncUnk();
      }
    },
    saveFuncUnk() {
      this.$http
        .post(
          `${this.url.baseUrl}/apps/dispatching/api/event/unknown/create/`,
          {
            type_journal: this.editedItem.type_journal,
            reason: this.editedItem.reason,
            date_from: this.editedItemDate1,
            created_at: this.editedItemDateCreate,
            date_to: this.editedItemDate2,
            index1: this.editedItem.index1,
            responsible_outfit: this.editedItem.responsible_outfit,
            send_from: this.editedItem.send_from,
            point1: this.editedItem.point1,
            point2: this.editedItem.point2,
            name: this.textFieldUnk,
            contact_name: this.editedItem.contact_name,
            comments1: this.editedItem.comments1,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            this.textFieldUnk = "";
            router.push({ name: "journalsob" });
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    saveFunc(idArg, urlFunc) {
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
        this.editedItem.contact_name = "";
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
        "created_at",
        this.editedItemDateCreate,
      );

      this.$http
        .post(
          `${this.url.baseUrl}${urlFunc}/${idArg}/`,
          {
            type_journal: this.editedItem.type_journal,
            reason: this.editedItem.reason,
            date_from: this.editedItemDate1,
            created_at: this.editedItemDateCreate,
            date_to: this.editedItemDate2,
            index1: this.editedItem.index1,
            responsible_outfit: this.editedItem.responsible_outfit,
            send_from: this.editedItem.send_from,
            point1: this.editedItem.point1,
            point2: this.editedItem.point2,
            contact_name: this.editedItem.contact_name,
            comments1: this.editedItem.comments1,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            router.push({ name: "journalsob" });
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    clearItemFun() {
      this.editedItem = Object.assign({}, this.clearItem);
    },
    outfitGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/outfit/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.outfit = response.data;
          console.log(this.outfit);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    circGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/event/circuits/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.circ = response.data;
          console.log(this.circ);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    objectGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/event/objects/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.obj = response.data;
          console.log(this.obj);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/event/ips/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.point = response.data;
          console.log(this.point);
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
.backCard1 {
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
</style>
