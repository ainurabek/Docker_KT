<template>
  <v-data-table
    :headers="headers"
    :items="spisokSotr"
    :items-per-page="15"
    item-key="id"
    class="elevation-1"
    dense
    :footer-props="{
      showFirstLastPage: true,
      firstIcon: 'mdi-arrow-collapse-left',
      lastIcon: 'mdi-arrow-collapse-right',
      prevIcon: 'mdi-minus',
      nextIcon: 'mdi-plus',
    }"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>Список Сотрудников</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-dialog v-model="dialog" max-width="400px">
          <v-card class="mx-auto backCard1 pt-4" color="blue" dark>
            <v-text-field
              label="Начало, дата и время"
              type="datetime-local"
              v-model="dateTimeEnd"
              outlined
              dense
              class="mr-2 ml-2 mt-4"
              min="1990-06-01T08:30"
              max="2099-06-30T16:30"
            ></v-text-field>
            <!-- <div>Datetime value: <span>{{datetime}}</span></div> -->

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="white" text @click="close">Отмена</v-btn>
              <v-btn color="white" text @click="save">Сохранить</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon @click="editItem(item)">mdi-pencil</v-icon>
    </template>
    <template v-slot:[`item.name`]="{ item }">
      <span
        >{{ item.user.first_name }}
        {{ item.user.last_name }}
        {{ item.user.middle_name }}
      </span>
    </template>
    <template v-slot:[`item.end_time2`]="{ item }">
      <template v-if="item.end_time2 != null">
        {{ item.end_time2 }}
      </template>
      <template v-if="item.end_time2 == null">
        <v-btn
          @click="sendDateEnd(item)"
          small
          color="orange"
          class="mt-1 mb-1"
          dark
          >Выбрать</v-btn
        >
      </template>
    </template>

    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Обновить</v-btn>
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: {
    propsUser: null,
    propsDateFrom: null,
    propsDateTo: null,
  },
  data: () => ({
    dialogTime: false,
    search: "",
    singleSelect: true,
    selected: [],
    dialog: false,
    loading: true,
    errored: false,
    dateTimeEnd: null,
    userLast: "",
    menu: false,
    modal: false,
    menu2: false,
    date: new Date().toISOString().substr(0, 10),
    editedItemDateEnd: "",
    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      {
        text: "ФИО",
        value: "name",
      },
      {
        text: "Начало (Дата)",
        value: "start_at2",
      },
      {
        text: "Начало (Время)",
        value: "start_at_time",
      },
      {
        text: "Конец (Дата)",
        value: "end_time2",
      },
      {
        text: "Конец (Время)",
        value: "end_time3",
        width: "1%",
      },
      { text: "", value: "actions", sortable: false },
      {
        text: "Статус",
        value: "status",
      },
    ],
    spisokSotr: [],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    dateTimeEnd(newValue) {
      this.editedItemDateEnd = newValue;
      if (newValue == null) {
        this.editedItemDateEnd = null;
      }
      console.log(this.editedItemDateEnd);
    },
    propsUser(newValue) {
      this.initialize();
      console.log(newValue);
    },
    propsDateFrom(newValue) {
      this.initialize();
      console.log(newValue);
    },
    propsDateTo(newValue) {
      this.initialize();
      console.log(newValue);
    },
  },

  mounted() {
    this.initialize();
  },

  methods: {
    editItem(item) {
      this.idDateEnd = item.id;
      this.dateTimeEnd = item.end_time;
      this.dialog = true;
      console.log(this.idDateEnd);
    },
    sendDateEnd(item) {
      this.idDateEnd = item.id;
      this.dialog = true;
      console.log(this.idDateEnd);
    },
    save() {
      const id = this.idDateEnd;
      this.$http
        .put(
          `${this.url.baseUrl}/apps/accounts/log-user/update/${id}/`,
          {
            end_time: this.editedItemDateEnd,
          },
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          if (response.status == "200") {
            this.initialize();
            console.log(response.status);
          }
        })
        .catch((error) => {
          console.log(error.response);
          alert(error.response.data.detail);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      this.close();
    },
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.dateTimeEnd = null;
        this.editedItemDateEnd = null;
        this.idDateEnd = "";
      });
    },
    dateTrans() {
      for (let i = 0; i < this.spisokSotr.length; i++) {
        if (this.spisokSotr[i].start_at != null) {
          let start_at = this.spisokSotr[i].start_at.substring(0, 10);
          let start_at_time = this.spisokSotr[i].start_at.substring(11, 16);
          let pushArray = {
            start_at2: start_at,
            start_at_time: start_at_time,
          };
          Object.assign(this.spisokSotr[i], pushArray);
        }
        if (this.spisokSotr[i].end_time != null) {
          let end_time = this.spisokSotr[i].end_time.substring(0, 10);
          let end_time3 = this.spisokSotr[i].end_time.substring(11, 16);
          let pushArray = {
            end_time2: end_time,
            end_time3: end_time3,
          };
          Object.assign(this.spisokSotr[i], pushArray);
        }
        if (this.spisokSotr[i].user.online == true) {
          let pushArray = {
            status: "В сети",
          };
          Object.assign(this.spisokSotr[i], pushArray);
        } else if (this.spisokSotr[i].user.online == false) {
          let pushArray = {
            status: "Не в сети",
          };
          Object.assign(this.spisokSotr[i], pushArray);
        }
      }
    },
    initialize() {
      let date_from = this.propsDateFrom;
      let date_to = this.propsDateTo;
      let userId = this.propsUser;
      console.log(userId);
      this.$http
        .get(
          `${this.url.baseUrl}/apps/accounts/log-user-list/?start_at=${date_from}&end_time=${date_to}&user=${userId}`,
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          this.spisokSotr = response.data;
          this.dateTrans();
          console.log(this.spisokSotr);
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
