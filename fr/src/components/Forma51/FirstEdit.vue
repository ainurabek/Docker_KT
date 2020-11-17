<template>
  <div class="back">
    <v-container>
      <v-toolbar-title>Резерв объектов</v-toolbar-title>

      <v-select
        label="Линия передачи"
        v-model="editedItemIdLp"
        :items="desserts"
      >
        <template slot="selection" slot-scope="{ item }"
          >({{ item.point1.point }}){{ item.name }}({{
            item.point2.point
          }})</template
        >
        <template slot="item" slot-scope="{ item }"
          >({{ item.point1.point }}){{ item.name }}({{
            item.point2.point
          }})</template
        >
      </v-select>
      <v-select label="Тракт, тип" v-model="editedItemIdTrakt" :items="trakt">
        <template slot="selection" slot-scope="{ item }"
          >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
          {{ item.type_of_trakt.name }}</template
        >
        <template slot="item" slot-scope="{ item }"
          >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
          {{ item.type_of_trakt.name }}</template
        >
      </v-select>
      <template v-if="typeTrakt === 1"></template>
      <template v-if="typeTrakt === 2">
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
      </template>
      <template v-if="typeTrakt === 3">
        <v-select label="ВГ" v-model="editedItemIdVG" :items="VG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
      </template>
      <template v-if="typeTrakt === 4">
        <v-select label="ТГ" v-model="editedItemIdTG" :items="TG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
        <v-select label="ВГ" v-model="editedItemIdVG" :items="VG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
      </template>
      <template v-if="typeTrakt === 5">
        <v-select label="ЧГ" v-model="editedItemIdCHG" :items="CHG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
        <v-select label="ТГ" v-model="editedItemIdTG" :items="TG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
        <v-select label="ВГ" v-model="editedItemIdVG" :items="VG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
            {{ item.type_of_trakt.name }}</template
          >
        </v-select>
      </template>
      <v-btn color="primary" class="mr-12" @click="initialize">Обновить</v-btn>

      <v-btn color="primary" @click="clearAll">Очистить</v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      trassa: [],
      desserts: [],
      trakt: [],
      PG: [],
      VG: [],
      TG: [],
      CHG: [],
      dataTrassa: [],
      url: {
        baseUrl: "http://0.0.0.0:8000",
      },
      chooseId: [],
      idLPForTrassa: "",
      idLP: "",
      editedItemIdLp: "",
      editedItemIdTrakt: "",
      editedItemIdPG: "",
      editedItemIdVG: "",
      editedItemIdTG: "",
      editedItemIdCHG: "",
      idTrassaSend: "",
      idLpSend: "",
      id: "",
      typeTrakt: "",
      sendTrassaFromComp: [],
    };
  },
  watch: {
    idTrassaSend(newValue) {
      if (newValue != "") {
        this.$emit("sendIdName", this.chooseId);
        this.$emit("sendIdFirst", this.idTrassaSend);
      }
    },
    editedItemIdLp(newValue) {
      if (newValue != {}) {
        (this.editedItemIdTrakt = {}),
          (this.editedItemIdPG = {}),
          (this.editedItemIdVG = {}),
          (this.editedItemIdTG = {}),
          (this.editedItemIdCHG = {}),
          (this.typeTrakt = "");
        this.idTrassaSend = this.editedItemIdLp.id;
        this.chooseId = this.editedItemIdLp.name;
        this.traktFunc();
        console.log(this.editedItemIdLp);
      }
    },
    editedItemIdTrakt(newValue) {
      if (newValue != {}) {
        (this.editedItemIdPG = {}),
          (this.editedItemIdVG = {}),
          (this.editedItemIdTG = {}),
          (this.editedItemIdCHG = {});
        if (this.editedItemIdTrakt.id >= 1) {
          this.chooseId = this.editedItemIdTrakt.name;
          this.idTrassaSend = this.editedItemIdTrakt.id;
        }
        let idTraktType = this.editedItemIdTrakt.type_of_trakt.id;
        this.typeTrakt = idTraktType;
        if (this.typeTrakt == 2) {
          this.getPG();
        } else if (this.typeTrakt == 3) {
          this.getVG();
        } else if (this.typeTrakt == 4) {
          this.getTG();
        } else if (this.typeTrakt == 5) {
          this.getCHG();
        }
      } else if (newValue == {}) {
        (this.editedItemIdPG = {}),
          (this.editedItemIdVG = {}),
          (this.editedItemIdTG = {}),
          (this.editedItemIdCHG = {}),
          (this.typeTrakt = "");
      }
      console.log(this.typeTrakt);
    },
    editedItemIdPG(newValue) {
      if (newValue != {}) {
        if (this.editedItemIdPG.id >= 1) {
          this.chooseId = this.editedItemIdPG.name;
          this.idTrassaSend = this.editedItemIdPG.id;
        }
        console.log(this.idTrassaSend);
      }
    },
    editedItemIdVG(newValue) {
      if (newValue != {}) {
        this.editedItemIdPG = {};
        if (this.editedItemIdVG.id >= 1) {
          this.chooseId = this.editedItemIdVG.name;
          this.idTrassaSend = this.editedItemIdVG.id;
        }
        this.getPG();
        console.log(this.idTrassaSend);
      }
    },
    editedItemIdTG(newValue) {
      if (newValue != {}) {
        this.editedItemIdPG = {};
        this.editedItemIdVG = {};
        if (this.editedItemIdTG.id >= 1) {
          this.chooseId = this.editedItemIdTG.name;
          this.idTrassaSend = this.editedItemIdTG.id;
        }
        this.getVG();
      }
    },
    editedItemIdCHG(newValue) {
      if (newValue != {}) {
        (this.editedItemIdPG = {}),
          (this.editedItemIdVG = {}),
          (this.editedItemIdTG = {});
        if (this.editedItemIdCHG.id >= 1) {
          this.chooseId = this.editedItemIdCHG.name;
          this.idTrassaSend = this.editedItemIdCHG.id;
        }
        this.getTG();
      }
    },
  },
  mounted() {
    this.initialize();
  },
  methods: {
    clearAll() {
      this.editedItemIdLp = {};
      (this.this.editedItemIdTrakt.type_of_trakt.id = {}),
        (this.editedItemIdTrakt = {}),
        (this.editedItemIdPG = {}),
        (this.editedItemIdVG = {}),
        (this.editedItemIdTG = {}),
        (this.editedItemIdCHG = {});
    },
    traktFunc() {
      let id = this.editedItemIdLp.id;
      console.log(this.id);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.trakt = response.data;
          // this.trassaCon()
          console.log(this.trakt);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    initialize() {
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/lp/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.desserts = response.data;
          // this.trassaCon()
          console.log(this.desserts);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getPG() {
      if (this.editedItemIdVG.id >= 1) {
        this.id = this.editedItemIdVG.id;
      } else {
        this.id = this.editedItemIdTrakt.id;
      }
      console.log(this.id);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${this.id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.PG = response.data;
          // this.trassaCon()
          // console.log(this.PG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getVG() {
      if (this.editedItemIdTG.id >= 1) {
        this.id = this.editedItemIdTG.id;
      } else {
        this.id = this.editedItemIdTrakt.id;
      }
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${this.id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.VG = response.data;
          // this.trassaCon()
          // console.log(this.VG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getTG() {
      if (this.editedItemIdCHG.id >= 1) {
        this.id = this.editedItemIdCHG.id;
      } else {
        this.id = this.editedItemIdCHG.id;
      }
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${this.id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.TG = response.data;
          // this.trassaCon()
          // console.log(this.TG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getCHG() {
      let id = this.editedItemIdTrakt.id;
      // console.log(this.editedItemIdTrakt);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.CHG = response.data;
          // this.trassaCon()
          // console.log(this.CHG);
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
.back {
  background-color: aliceblue;
}
</style>
