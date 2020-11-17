<template>
  <v-container>
    <v-card class="createOtch">
      <v-card-title>
        <span class="headline">Создание отчета</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <div>
            <v-text-field
              label="Начало, дата и время"
              type="date"
              v-model="datetime"
              outlined
              dense
              min="1990-06-01"
              max="2099-06-30"
            ></v-text-field>
          </div>
          <div>
            <v-text-field
              label="Конец, дата и время"
              type="date"
              v-model="datetime2"
              outlined
              dense
              min="1990-06-01"
              max="2099-06-30"
            ></v-text-field>
          </div>
          <div>
            <v-text-field
              label="Наименование"
              v-model="editNameAF"
              :rules="[(v) => !!v || `Введите наименование`]"
            >
            </v-text-field>
          </div>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="createAF">
          Создать
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { bus } from "../../../main"
export default {
  data: () => ({
    errored: false,
    loading: false,
    datetime: null,
    datetime2: null,
    editNameAF: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  methods: {
    createAF() {
      this.$http
        .post(
          `${this.url.baseUrl}/apps/analysis/form/`,
          {
            date_from: this.datetime,
            date_to: this.datetime2,
            name: this.editNameAF,
          },
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            bus.$emit("updateOtchetAK")
          }
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
.createOtch {
  background-color: rgb(255, 255, 255);
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.5);
}
</style>
