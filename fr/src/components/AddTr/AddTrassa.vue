<template>
  <div class="back">
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-autocomplete
            label="Линия передачи"
            v-model="editedItemIdLp"
            filled
            :items="desserts"
            item-value="id"
            return-object
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
          </v-autocomplete>

          <v-autocomplete
            v-if="loaded"
            label="Тракт, тип"
            v-model="editedItemIdTrakt"
            filled
            :items="trakt"
            item-value="id"
            return-object
          >
            <template slot="selection" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
              {{ item.type_of_trakt.name }}</template
            >
            <template slot="item" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
              {{ item.type_of_trakt.name }}</template
            >
          </v-autocomplete>
        </v-col>

        <v-col cols="12" sm="6" md="4">
          <template v-if="typeTrakt >= 5">
            <v-autocomplete
              label="ЧГ"
              v-model="editedItemIdCHG"
              filled
              :items="CHG"
              item-value="id"
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
            </v-autocomplete>
          </template>
          <template v-if="typeTrakt >= 4">
            <v-autocomplete
              label="ТГ"
              v-model="editedItemIdTG"
              :items="TG"
              item-value="id"
              filled
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
            </v-autocomplete>
          </template>
          <template v-if="typeTrakt >= 3 ">
            <v-autocomplete
              label="ВГ"
              v-model="editedItemIdVG"
              :items="VG"
              item-value="id"
              filled
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
            </v-autocomplete>
          </template>
          <template v-if="typeTrakt >= 2">
            <v-autocomplete
              v-if="loadedAllG"
              label="ПГ"
              v-model="editedItemIdPG"
              filled
              :items="PG"
              item-value="id"
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt.name }}</template
              >
            </v-autocomplete>
          </template>
        </v-col>
        <v-col cols="12" sm="6" md="4">
          <v-toolbar-title class="mb-4"
            >Выбор объекта для создания трассы:</v-toolbar-title
          >
          <v-card>
            <v-card-text><span class="fontsiz">Объект: {{showObjForTrassa}}</span></v-card-text>
          </v-card>
          <v-btn color="primary" class="mt-4" @click.prevent="clearAll">Очистить</v-btn>
        </v-col>
      </v-row>
      <!-- <v-btn color="primary" class="ml-4 mr-12" @click="initialize"
            >Обновить</v-btn
          > -->

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
        <v-row>
          <v-col cols="6" md="4">
            <LeftTrassa :idTrassa="objForTrassa"></LeftTrassa>
          </v-col>
           <v-col cols="6" md="4">
            <CompTrassa :idTrassa="objForTrassa"></CompTrassa>
          </v-col>
          <v-col cols="6" md="4">
            <RightTrassa :idTrassa="objForTrassa"> </RightTrassa>
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
// import CompTraktAllG from "./CompTraktAllG"

export default {
  components: { LeftTrassa, RightTrassa, CompTrassa },

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
      loaded: false,
      loadedAllG: false,
      url: {
        baseUrl: "http://0.0.0.0:8000",
      },
      objForTrassa: {},
      showObjForTrassa: "",
      idLPForTrassa: "",
      idLP: "",
      editedItemIdLp: "",
      editedItemIdPG: "",
      editedItemIdVG: "",
      editedItemIdTG: "",
      editedItemIdCHG: "",
      editedItemIdTrakt: "",
      editedItemIdOther: "",
      numberTypeTrakt: 0,
      nameArray: "",
      typeTrakt: null,
    };
  },
  watch: {
    editedItemIdLp(newValue) {
      if (newValue.id != undefined) {
        this.trassa = newValue.trassa
        this.editedItemIdTrakt = "";
        this.editedItemIdCHG = "";
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.CHG = [];  this.TG = [];  this.VG = [];  this.PG = [];
        this.typeTrakt = "";
        this.objFuncTrassa(newValue)
        this.traktFunc();
      }
    },
    editedItemIdTrakt(newValue) {
      if (newValue.id != undefined) {
        this.typeTrakt = newValue.number;
        this.trassa = newValue.trassa
        this.numberTypeTrakt = newValue.number;
        this.objFuncTrassa(newValue)
        if (this.typeTrakt == 2) {
          this.clearLpTrAllG()
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        } else if (this.typeTrakt == 3) {
          this.clearLpTrAllG()
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        } else if (this.typeTrakt == 4) {
          this.clearLpTrAllG()
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        } else if (this.typeTrakt == 5) {
          this.clearLpTrAllG()
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        }
      }
    },
    editedItemIdPG(newValue) {
      if (newValue.id != undefined) {
        this.trassa = newValue.trassa
        this.objFuncTrassa(newValue)
      }
    },
    editedItemIdVG(newValue) {
      if (newValue.id != undefined) {
        this.trassa = newValue.trassa
        this.numberTypeTrakt = newValue.number;
        this.objFuncTrassa(newValue)
        this.clearLpTrAllG()
        this.idForAllG = newValue.id;
        this.traktAllGFunc();
      }
    },
    editedItemIdTG(newValue) {
      if (newValue.id != undefined) {
        this.trassa = newValue.trassa
        this.numberTypeTrakt = newValue.number;
        this.objFuncTrassa(newValue)
        this.clearLpTrAllG()
        this.idForAllG = newValue.id;
        this.traktAllGFunc();
      }
    },
    editedItemIdCHG(newValue) {
      if (newValue.id != undefined) {
        this.trassa = newValue.trassa
        this.objFuncTrassa(newValue)
        this.showObjForTrassa = newValue
        this.clearLpTrAllG()
        this.idForAllG = newValue.id;
        this.traktAllGFunc();
      }
    },
  },

  created() {},
  mounted() {
    this.initialize();
  },
  methods: {
    objFuncTrassa(item) {
      this.objForTrassa = item
      if(item.point1.point != undefined) {
        this.showObjForTrassa = `(${item.point1.point})${item.name}(${item.point2.point})`
      } else {
        this.showObjForTrassa = `(${item.point1})${item.name}(${item.point2})`
      }
    },
    clearLpTrAllG() {
      if (this.numberTypeTrakt == 2) {
        this.editedItemIdPG = "";
      } else if (this.numberTypeTrakt == 3) {
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.PG = [];
      } else if (this.numberTypeTrakt == 4) {
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.VG = [];  this.PG = [];
      } else if (this.numberTypeTrakt == 5) {
        this.editedItemIdCHG = "";
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.TG = [];  this.VG = [];  this.PG = [];
      }
    },
    arrayReverseTr(name) {
      for (let i = 0; i < name.length; i++) {
        let arrayrReverse = name[i].transit.reverse();
        let arrayTransit12 = [...arrayrReverse, ...name[i].transit2];
        let pushArray = {
          trassa: arrayTransit12,
        };
        Object.assign(name[i], pushArray);
      }
      console.log(this.desserts)
    },
    arrayReverseTr2(name) {
      for (let i = 0; i < name.length; i++) {
        if (name[i].type_of_trakt.name === "ПГ") {
          this.numberTypeTrakt = 1;
        } else if (name[i].type_of_trakt.name === "ВГ") {
          this.numberTypeTrakt = 2;
        } else if (name[i].type_of_trakt.name === "ТГ") {
          this.numberTypeTrakt = 3;
        } else if (name[i].type_of_trakt.name === "ЧГ") {
          this.numberTypeTrakt = 4;
        } else if (name[i].type_of_trakt.name === "РГ") {
          this.numberTypeTrakt = 5;
        }
        let arrayrReverse = name[i].transit.reverse();
        let arrayTransit12 = [...arrayrReverse, ...name[i].transit2];
        let pushArray = {
          number: this.numberTypeTrakt,
          trassa: arrayTransit12,
        };
        Object.assign(name[i], pushArray);
      }
    },
    clearAll() {
      this.editedItemIdLp = "";
      this.editedItemIdTrakt = "";
      this.typeTrakt = null;
      this.objForTrassa = {}
      this.showObjForTrassa = ""
      this.editedItemIdTrakt = "";
      this.editedItemIdCHG = "";
      this.editedItemIdTG = "";
      this.editedItemIdVG = "";
      this.editedItemIdPG = "";
      this.trakt = []; this.CHG = [];  this.TG = [];  this.VG = [];  this.PG = [];
    },
    traktFunc() {
      this.loaded = false;
      let id = this.editedItemIdLp.id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.trakt = response.data;
          this.arrayReverseTr2(this.trakt);
          // console.log(this.trakt);
          this.loaded = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    ifFuncArray(item) {
      if (this.numberTypeTrakt == 2) {
        this.PG = item;
        this.arrayReverseTr2(this.PG);
      } else if (this.numberTypeTrakt == 3) {
        this.VG = item;
        this.arrayReverseTr2(this.VG);
      } else if (this.numberTypeTrakt == 4) {
        this.TG = item;
        this.arrayReverseTr2(this.TG);
      } else if (this.numberTypeTrakt == 5) {
        this.CHG = item;
        this.arrayReverseTr2(this.CHG);
      }
    },
    traktAllGFunc() {
      this.loadedAllG = false;
      let id = this.idForAllG;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.ifFuncArray(response.data);
          // this.arrayReverseTr(this.desserts);
          // console.log(this.PG, this.VG, this.TG, this.CHG);
          this.loadedAllG = true;
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
          this.arrayReverseTr(this.desserts);
          // console.log(this.desserts);
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
  position: relative;
  margin: 0px;
  padding: 0px;
  max-width: 100%;
  min-height: 100%;
  max-height: 100%;
  overflow: hidden;
  background-color: rgb(230, 230, 230);
}
</style>
