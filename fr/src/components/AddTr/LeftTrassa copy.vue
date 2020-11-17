<template>
  <div class="vvv">
    <v-container>
      <v-toolbar-title>Создать трассу</v-toolbar-title>
      <v-autocomplete
        label="ИП"
        v-model="editedItemIdPoint"
        :items="desserts"
        item-value="id"
        item-text="point"
      ></v-autocomplete>
      <v-autocomplete label="Линия передачи" v-model="editedItemIdLp" :items="lp">
        <template slot="selection" slot-scope="{ item }"
          >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
        >
        <template slot="item" slot-scope="{ item }"
          >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
        >
      </v-autocomplete>
      <v-autocomplete label="Тракт, тип" v-model="editedItemIdTrakt" :items="trakt">
        <template slot="selection" slot-scope="{ item }"
          >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
        >
        <template slot="item" slot-scope="{ item }"
          >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
        >
      </v-autocomplete>
      <template v-if="typeTrakt === 'ПГ'"></template>
      <template v-if="typeTrakt === 'ВГ'">
        <v-autocomplete label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-autocomplete>
      </template>
      <template v-if="typeTrakt === 'ТГ'">
        <v-select label="ВГ" v-model="editedItemIdVG" :items="VG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
      </template>
      <template v-if="typeTrakt === 'ЧГ'">
        <v-select label="ТГ" v-model="editedItemIdTG" :items="TG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
        <v-select label="ВГ" v-model="editedItemIdVG" :items="VG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
      </template>
      <template v-if="typeTrakt === 'РГ'">
        <v-select label="ЧГ" v-model="editedItemIdCHG" :items="CHG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
        <v-select label="ТГ" v-model="editedItemIdTG" :items="TG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
        <v-select label="ВГ" v-model="editedItemIdVG" :items="VG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
        <v-select label="ПГ" v-model="editedItemIdPG" :items="PG">
          <template slot="selection" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
          <template slot="item" slot-scope="{ item }"
            >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</template
          >
        </v-select>
      </template>
      <v-btn color="primary" class="mr-12" @click="save">Добавить</v-btn>

      <v-btn color="primary" @click="clearAll">Очистить</v-btn>
    </v-container>
  </div>
</template>

<script>
import { bus } from "../../main";
export default {
  props: {
    idTrassa: null,
  },

  data() {
    return {
      desserts: [],
      lp: [],
      trakt: [],
      PG: [],
      VG: [],
      TG: [],
      CHG: [],
      url: {
        baseUrl: "http://0.0.0.0:8000",
      },
      idLPForTrassa: "",
      idLP: "",
      editedItemIdPoint: "",
      editedItemIdLp: "",
      editedItemIdTrakt: "",
      editedItemIdPG: "",
      editedItemIdVG: "",
      editedItemIdTG: "",
      editedItemIdCHG: "",
      idTrassaSend: "",
      idLPLeft: "",
      objectSend: "",
      id: "",
    };
  },
  watch: {
    editedItemIdPoint(newValue) {
      if (newValue != {}) {
        this.lpFunc();
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
        this.traktFunc();
        console.log(this.idTrassaSend);
      }
    },
    editedItemIdTrakt(newValue) {
      if (newValue != {}) {
        (this.editedItemIdPG = {}),
          (this.editedItemIdVG = {}),
          (this.editedItemIdTG = {}),
          (this.editedItemIdCHG = {});
        if (this.editedItemIdTrakt.id >= 1) {
          this.idTrassaSend = this.editedItemIdTrakt.id;
        }
        let idTraktType = this.editedItemIdTrakt.type_of_trakt;
        this.typeTrakt = idTraktType;
        if (this.typeTrakt == "ВГ") {
          this.getPG();
        } else if (this.typeTrakt == "ТГ") {
          this.getVG();
        } else if (this.typeTrakt == "ЧГ") {
          this.getTG();
        } else if (this.typeTrakt == "РГ") {
          this.getCHG();
        }
        // this.idTrassaSend = this.editedItemIdTrakt.id;
        // this.objectSend = this.editedItemIdTrakt
        // let idTraktType = this.editedItemIdTrakt.type_of_trakt;
        // this.typeTrakt = idTraktType;
        // if (this.typeTrakt == "ВГ") {
        //   (this.editedItemIdPG = {}), (this.editedItemIdVG = {}), this.getPG();
        // } else if (this.typeTrakt == "ТГ") {
        //   (this.editedItemIdPG = {}),
        //     (this.editedItemIdVG = {}),
        //     (this.editedItemIdTG = {}),
        //     this.getVG();
        // } else if (this.typeTrakt == "ЧГ") {
        //   (this.editedItemIdPG = {}),
        //     (this.editedItemIdVG = {}),
        //     (this.editedItemIdTG = {}),
        //     (this.editedItemIdCHG = {}),
        //     this.getTG();
        // } else if (this.typeTrakt == "РГ") {
        //   (this.editedItemIdPG = {}),
        //     (this.editedItemIdVG = {}),
        //     (this.editedItemIdTG = {}),
        //     (this.editedItemIdCHG = {}),
        //     this.getCHG();
        // }
        // console.log(this.objectSend);
      }
    },
    editedItemIdPG(newValue) {
      if (newValue != {}) {
        if (this.editedItemIdPG.id >= 1) {
          this.idTrassaSend = this.editedItemIdPG.id;
          this.objectSend = this.editedItemIdPG;
        }
        console.log(this.objectSend);
      }
    },
    editedItemIdVG(newValue) {
      if (newValue != {}) {
        this.editedItemIdPG = {};
        if (this.editedItemIdVG.id >= 1) {
          this.idTrassaSend = this.editedItemIdVG.id;
          this.objectSend = this.editedItemIdVG;
        }
        this.getPG();
        console.log(this.objectSend);
      }
    },
    editedItemIdTG(newValue) {
      if (newValue != {}) {
        (this.editedItemIdPG = {}), (this.editedItemIdVG = {});
        if (this.editedItemIdTG.id >= 1) {
          this.idTrassaSend = this.editedItemIdTG.id;
          this.objectSend = this.editedItemIdTG;
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
          this.idTrassaSend = this.editedItemIdCHG.id;
          this.objectSend = this.editedItemIdCHG;
        }

        this.getTG();
      }
    },
  },
  mounted() {
    this.initialize();
  },
  methods: {
    save() {
      let id = this.idTrassa;
      let id2 = this.idTrassaSend;

      console.log(
        "left trassa props id",
        this.idTrassa,
        "id left trassa",
        this.idTrassaSend
      );
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/left-trassa/${id}/${id2}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == 201) {
            console.log("Ok");
            bus.$emit("updateTrassa");
          }
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    clearAll() {
      this.editedItemIdLp = {};
      this.editedItemIdTrakt = {};
      this.editedItemIdPG = {};
      this.editedItemIdVG = {};
      this.editedItemIdTG = {};
      this.editedItemIdCHG = {};
    },
    lpFunc() {
      let id = this.editedItemIdPoint;
      console.log(this.lp);
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/select-point/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.lp = response.data;
          // console.log(this.trakt);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    traktFunc() {
      let id = this.editedItemIdLp.id;
      console.log(this.editedItemIdLp);
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.trakt = response.data;
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
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/point-list/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.desserts = response.data;
          // console.log(this.desserts);
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
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${this.id}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.PG = response.data;
          // console.log(this.PG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      // } else {
      //   let id = this.editedItemIdTrakt.id;
      //   // console.log(this.editedItemIdTrakt);
      //   this.$http
      //     .get(
      //       `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`,
      //       {
      //         headers: { Authorization: `Token ${localStorage.token}` }
      //       }
      //     )
      //     .then(response => {
      //       this.PG = response.data;
      //       // console.log(this.PG);
      //     })
      //     .catch(error => {
      //       console.log(error);
      //       this.errored = true;
      //     })
      //     .finally(() => (this.loading = false));
      // }
    },
    getVG() {
      if (this.editedItemIdTG.id >= 1) {
        this.id = this.editedItemIdTG.id;
      } else {
        this.id = this.editedItemIdTrakt.id;
      }
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${this.id}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.VG = response.data;
          // console.log(this.VG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      // } else {
      //   let id = this.editedItemIdTrakt.id;
      //   // console.log(this.editedItemIdTrakt);
      //   this.$http
      //     .get(
      //       `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`,
      //       {
      //         headers: { Authorization: `Token ${localStorage.token}` }
      //       }
      //     )
      //     .then(response => {
      //       this.VG = response.data;
      //       // console.log(this.VG);
      //     })
      //     .catch(error => {
      //       console.log(error);
      //       this.errored = true;
      //     })
      //     .finally(() => (this.loading = false));
      // }
    },
    getTG() {
      if (this.editedItemIdCHG.id >= 1) {
        this.id = this.editedItemIdCHG.id;
      } else {
        this.id = this.editedItemIdCHG.id;
      }
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${this.id}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.TG = response.data;
          // console.log(this.TG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      // } else {
      //   let id = this.editedItemIdTrakt.id;
      //   // console.log(this.editedItemIdTrakt);
      //   this.$http
      //     .get(
      //       `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`,
      //       {
      //         headers: { Authorization: `Token ${localStorage.token}` }
      //       }
      //     )
      //     .then(response => {
      //       this.TG = response.data;
      //       // console.log(this.TG);
      //     })
      //     .catch(error => {
      //       console.log(error);
      //       this.errored = true;
      //     })
      //     .finally(() => (this.loading = false));
      // }
    },
    getCHG() {
      let id = this.editedItemIdTrakt.id;
      // console.log(this.editedItemIdTrakt);
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          this.CHG = response.data;
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
.vvv {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  background-color: white;
}
</style>
