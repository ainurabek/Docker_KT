<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="trassaFin"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
    </v-data-table>
    <v-select
      v-model="value"
      :items="items"
      item-value="id"
      item-text="name"
      attach
      chips
      label="Сохранение"
      multiple
    >
    </v-select>
    <v-btn color="primary" class="mt-3" @click="save">Сохранить</v-btn>
  </div>
</template>

<script>
import { bus } from "../../main";

export default {
  props: {
    idTrassa: {
      type: Object,
      default: function() {
        return {};
      },
    },
  },
  data: () => ({
    value: [],
    items: [
      {
        id: 1,
        name: "Форма 5.1",
        bool: true,
      },
      {
        id: 2,
        name: "Список арендаторов",
        bool: true,
      },
    ],
    desserts: [],
    trassaFin: [],
    save_in: false,
    customer: false,

    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },

      {
        text: "",
        value: "point1",
      },
      {
        text: "",
        value: "name",
      },
      {
        text: "",
        value: "point2",
      },
      {
        text: "",
        value: "actions",
      },
    ],
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),

  computed: {},

  watch: {
    idTrassa(newValue) {
      if (newValue.id != undefined) {
        this.selectLp();
      }
    },
    value(newValue) {
      console.log(newValue)
    }

    // desserts(newValue) {
    //   if (newValue != []) {
    //     this.arrayTrassa();
    //   }
    // },
  },

  created() {},
  mounted() {
    bus.$on("updateTrassa", () => {
      this.selectLp();
    });
  },
  beforeDestroy() {
    bus.$off("updateTrassa");
  },

  methods: {
    arrayTrassa(item) {
      this.desserts = item
      let arrayReverse = item.transit.reverse();
      let arrayFin = [...arrayReverse, ...item.transit2];
      this.trassaFin = arrayFin
    },
    selectLp() {
      let id = this.idTrassa.id;
      console.log(this.idTrassa);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/select-lp/${id}/`, {
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
        })
        .then((response) => {
          // this.desserts = response.data;
          this.arrayTrassa(response.data);
          console.log(this.desserts);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    deleteItem(item) {
      let id = this.idTrassa.id;
      let id2 = item.id;
      console.log(id2);
      confirm("Вы уверены что хотите удалить") &&
        this.$http
          .delete(
            `${this.url.baseUrl}/apps/opu/objects/trakt/delete-trass/${id}/${id2}/`,
            {
              headers: {
                Authorization: `Token ${localStorage.token}`,
              },
            }
          )
          .then((response) => {
            if (response.status == "204") {
              this.selectLp();
              console.log("ok");
            }
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
    },
    saveTrassaComplete() {
      alert("Трасса успешно сохраненна!");
    },
    save() {
      let id = this.idTrassa.id;
      if (this.value[0] == 1) {
        this.save_in = true;
      }
      if (this.value[1] == 1) {
        this.save_in = true;
      }
      if (this.value[0] == 2) {
        this.customer = true;
      }
      if (this.value[1] == 2) {
        this.customer = true;
      }
      console.log(this.save_in);
      console.log(this.customer);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/save-trassa/${id}/`, {
          headers: {
            Authorization: `Token ${localStorage.token}`,
          },
        })
        .then((response) => {
          if (response.status == "201") {
            this.saveTrassaComplete();
            console.log("OK");
          }
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));

      this.$http
        .post(
          `${this.url.baseUrl}/apps/opu/objects/trakt/save-trassa/${id}/`,
          {
            save_in: this.save_in,
            customer: this.customer,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.token}`,
            },
          }
        )
        .then((response) => {
          this.save_in = false;
          this.customer = false;
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => 
          {
          this.loading = false
          this.save_in = false
          this.customer = false });
    },
  },
};
</script>

<style scoped>
.backCenter {
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
</style>
