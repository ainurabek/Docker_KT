<template>
  <div class="back">
    <v-container>
      <v-toolbar-title>Выбор объекта для создания трассы</v-toolbar-title>
      <v-row justify="center">
        <v-col cols="12" sm="6" md="4">
          

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
          </v-col>
          <v-col cols="12" sm="6" md="4">
          <v-select
            label="Тракт, тип"
            v-model="editedItemIdTrakt"
            :items="trakt"
          >
            <template slot="selection" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
              {{ item.type_of_trakt.name }}</template
            >
            <template slot="item" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
              {{ item.type_of_trakt.name }}</template
            >
          </v-select>
          </v-col>
          <v-col cols="12" sm="6" md="4">
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
          
        </v-col>
      </v-row>
        <v-btn color="primary" class="ml-4 mr-12" @click="initialize"
            >Обновить</v-btn
          >

          <v-btn color="primary" @click="clearAll">Очистить</v-btn>
      <v-container>
      <v-card color="white" class="mx-auto">
        <v-card-text>
          <div>
            <span class="fontsiz">Трасса:</span>
            <span class="fontsiz" v-for="item in trassa" :key="item.indexOf"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }})</span
            >
          </div>
        </v-card-text>
      </v-card>
    </v-container>

      <v-col cols="12">
        <v-row justify="center">
          <v-col cols="6" md="4">
            <LeftTrassa :idTrassa="idTrassaSend"></LeftTrassa>
          </v-col>
          <v-col cols="6" md="4">
            <CompTrassa :idTrassa="idTrassaSend"
                       ></CompTrassa>
          </v-col>
          <v-col cols="6" md="4">
            <RightTrassa :idTrassa="idTrassaSend"> </RightTrassa>
          </v-col>
        </v-row>
      </v-col>
    </v-container>
  </div>
</template>

<script>
// import { bus } from "../../main";
import LeftTrassa from "./LeftTrassa";
import RightTrassa from "./RightTrassa";
import CompTrassa from "./CompTrassa";

export default {
  components: { LeftTrassa, RightTrassa, CompTrassa },

  data() {
    return {
      trassa:[],
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
      
    };
  },
  watch: {
    editedItemIdLp(newValue) {
      if (newValue != {}) {
        (this.editedItemIdTrakt = {}),
          (this.editedItemIdPG = {}),
          (this.editedItemIdVG = {}),
          (this.editedItemIdTG = {}),
          (this.editedItemIdCHG = {}),
          (this.typeTrakt = "");
          this.trassa = this.editedItemIdLp.trassa
        this.idTrassaSend = this.editedItemIdLp.id;
        this.traktFunc();
        console.log(this.trassa);
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
          this.trassa = this.editedItemIdTrakt.trassa
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
        //   this.typeTrakt = idTraktType;
        //   this.idTrassaSend = this.editedItemIdTrakt.id;
        //   let idTraktType = this.editedItemIdTrakt.type_of_trakt.id;
        //   this.typeTrakt = idTraktType;
        //   if (this.typeTrakt == 2) {
        //     // (this.editedItemIdPG = {}), (this.editedItemIdVG = {}),
        //     this.getPG();
        //   } else if (this.typeTrakt == 3) {
        //     (this.editedItemIdPG = {}),
        //       (this.editedItemIdVG = {}),
        //       (this.editedItemIdTG = {}),
        //       this.getVG();
        //   } else if (this.typeTrakt == 4) {
        //     (this.editedItemIdPG = {}),
        //       (this.editedItemIdVG = {}),
        //       (this.editedItemIdTG = {}),
        //       (this.editedItemIdCHG = {}),
        //       this.getTG();
        //   } else if (this.typeTrakt == 5) {
        //     (this.editedItemIdPG = {}),
        //       (this.editedItemIdVG = {}),
        //       (this.editedItemIdTG = {}),
        //       (this.editedItemIdCHG = {}),
        //       this.getCHG();
        //   }
        //   console.log(this.idTrassaSend);
        // }
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
          this.trassa = this.editedItemIdPG.trassa
          this.idTrassaSend = this.editedItemIdPG.id;
        }
        console.log(this.idTrassaSend);
      }
    },
    editedItemIdVG(newValue) {
     
      if (newValue != {}) {
        this.editedItemIdPG = {};
        if (this.editedItemIdVG.id >= 1) {
           this.trassa = this.editedItemIdVG.trassa
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
          this.trassa = this.editedItemIdTG.trassa
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
          this.trassa = this.editedItemIdCHG.trassa
          this.idTrassaSend = this.editedItemIdCHG.id;
        }
        this.getTG();
      }
    },
  },
  created() {
  },
  mounted() {
    this.initialize();
  },
  methods: {
     arrayReverseTr(name) {
      for (let i = 0; i < name.length; i++) {
        let arrayrReverse = name[i].transit.reverse();
        let arrayTransit12 = [...arrayrReverse, ...name[i].transit2];
        let pushArray = {
          trassa: arrayTransit12,
        };
        let finArray = Object.assign(name[i], pushArray);
        console.log(finArray);
      }
    },
   
   
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
          this.arrayReverseTr(this.trakt)
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
          this.arrayReverseTr(this.desserts)
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
         this.arrayReverseTr(this.PG)
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
         this.arrayReverseTr(this.VG)
          // console.log(this.VG);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
      //   } else {
      //     let id = this.editedItemIdTrakt.id;
      //     // console.log(this.editedItemIdTrakt);
      //     this.$http
      //       .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
      //         headers: { Authorization: `Token ${localStorage.token}` }
      //       })
      //       .then(response => {
      //         this.VG = response.data;
      //         // console.log(this.VG);
      //       })
      //       .catch(error => {
      //         console.log(error);
      //         this.errored = true;
      //       })
      //       .finally(() => (this.loading = false));
      //   }
      // },
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
        this.arrayReverseTr(this.TG)
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
      //     .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
      //       headers: { Authorization: `Token ${localStorage.token}` }
      //     })
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
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.CHG = response.data;
         this.arrayReverseTr(this.CHG)
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
.fontsiz {
  font-size: 16px;
  margin-left: 10px;
  color: black;
}
.back {
  background-color: aliceblue;
}
</style>
