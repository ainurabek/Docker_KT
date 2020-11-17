<template>
  <div>
    <v-card class="mx-auto backCardCirc pl-4 pr-4 pt-3 pb-3">
      <v-toolbar-title>Список Другое</v-toolbar-title>
      <v-row justify="center">
        <v-col cols="12" sm="6" md="11">
          <v-autocomplete
            label="Название"
            v-model="id_object"
            :items="obj"
            item-value="name"
            item-text="name"
          >
          </v-autocomplete>
          <!-- <span>{{editedItemCirc}}</span> -->
        </v-col>
      </v-row>
      <v-btn color="primary" class="mr-12 mb-2" @click="clearAll"
        >Очистить</v-btn
      >
    </v-card>
  </div>
</template>

<script>
import { bus } from "../../../main";
export default {
  data: () => ({
    ip: [],
    obj: [],
    customerArr: [],
    outfitArr: [],
    id_object: "",
    point_id: "",
    point_id2: "",
    customer: "",
    outfit: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  watch: {
    id_object() {
      this.sendPropsObjObj();
    },
  },
  mounted() {
    this.objGet();
  },
  methods: {
    sendPropsObjObj() {
      bus.$emit("filtr_ObjUnk", this.id_object);
      console.log(this.id_object);
    },
    clearAll() {
      this.id_object = "";
    },
    objGet() {
      this.$http
        .get(`${this.url.baseUrl}/apps/dispatching/api/event/unknown/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.obj = response.data;
          console.log(this.obj);
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
.backCardCirc {
  background-color: white;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}
</style>
