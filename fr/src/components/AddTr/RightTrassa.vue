<template>
  <div class="vvv">
    <v-container>
      <v-toolbar-title> Добавить объект </v-toolbar-title>
      <div>
        <div class="mt-4">
          <v-autocomplete
            label="ИП"
            v-model="editedItemIdIP"
            dense
            :items="desserts"
            item-value="id"
            item-text="point"
            return-object
          >
          </v-autocomplete>
        </div>
        <div>
          <v-autocomplete
            label="Линия передачи"
            v-model="editedItemIdLp"
            dense
            :items="LP"
            item-value="id"
            return-object
          >
            <template slot="selection" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{
                item.point2
              }})</template
            >
            <template slot="item" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{
                item.point2
              }})</template
            >
          </v-autocomplete>
        </div>
        <div>
          <v-autocomplete
            v-if="loaded"
            label="Тракт, тип"
            v-model="editedItemIdTrakt"
            dense
            :items="trakt"
            item-value="id"
            return-object
          >
            <template slot="selection" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
              {{ item.type_of_trakt }}</template
            >
            <template slot="item" slot-scope="{ item }"
              >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
              {{ item.type_of_trakt }}</template
            >
          </v-autocomplete>
        </div>

        <div>
          <template v-if="typeTrakt >= 5">
            <v-autocomplete
              label="ЧГ"
              v-model="editedItemIdCHG"
              dense
              :items="CHG"
              item-value="id"
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
            </v-autocomplete>
          </template>
          <template v-if="typeTrakt >= 4">
            <v-autocomplete
              label="ТГ"
              v-model="editedItemIdTG"
              :items="TG"
              item-value="id"
              dense
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
            </v-autocomplete>
          </template>
          <template v-if="typeTrakt >= 3">
            <v-autocomplete
              label="ВГ"
              v-model="editedItemIdVG"
              :items="VG"
              item-value="id"
              dense
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
            </v-autocomplete>
          </template>
          <template v-if="typeTrakt >= 2">
            <v-autocomplete
              v-if="loadedAllG"
              label="ПГ"
              v-model="editedItemIdPG"
              dense
              :items="PG"
              item-value="id"
              return-object
            >
              <template slot="selection" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
              <template slot="item" slot-scope="{ item }"
                >({{ item.point1 }}){{ item.name }}({{ item.point2 }}) -
                {{ item.type_of_trakt }}</template
              >
            </v-autocomplete>
          </template>
        </div>
        <div>
          <v-divider></v-divider>
          <v-row justify="center">
            <span class="fontsiz">
              {{showObjForTrassa}}
            </span></v-row
          >
          <v-divider></v-divider>
        </div>
        <div class="mt-2">
          <v-btn color="primary" class="ml-8 mr-12" @click="save">Добавить</v-btn>
          <v-btn color="primary" @click="clearAll">Очистить</v-btn>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import { bus } from "../../main"

export default {
  props: {
    idTrassa: {
      type: Object,
      default: function() {
        return {}
      }
    }
  },
  data() {
    return {
      trassa: [],
      desserts: [],
      LP: [],
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
      objForLTrassa: "",
      showObjForTrassa: "",
      idLPForTrassa: "",
      idLP: "",
      editedItemIdIP: "",
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
    editedItemIdIP(newValue) {
      if (newValue.id != undefined) {
        this.editedItemIdLp = "";
        this.editedItemIdTrakt = "";
        this.editedItemIdCHG = "";
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.trakt = [];
        this.CHG = [];
        this.TG = [];
        this.VG = [];
        this.PG = [];
        this.typeTrakt = "";
        this.loaded = false
        this.loadedAllG = false
        this.objFuncTrassaIP(newValue);
        this.getLp(newValue);
      }
    },
    editedItemIdLp(newValue) {
      if (newValue.id != undefined) {
        this.clearLpTrAllG();
        this.typeTrakt = "";
        this.objFuncTrassa(newValue);
        this.traktFunc();
      }
    },
    editedItemIdTrakt(newValue) {
      if (newValue.id != undefined) {
        console.log(newValue)
        this.typeTrakt = newValue.number;
        this.numberTypeTrakt = newValue.number;
        this.objFuncTrassa(newValue);
        if (this.typeTrakt == 2) {
          this.clearLpTrAllG();
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        } else if (this.typeTrakt == 3) {
          this.clearLpTrAllG();
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        } else if (this.typeTrakt == 4) {
          this.clearLpTrAllG();
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        } else if (this.typeTrakt == 5) {
          this.clearLpTrAllG();
          this.idForAllG = newValue.id;
          this.traktAllGFunc();
        }
      }
    },
    editedItemIdPG(newValue) {
      if (newValue.id != undefined) {
        this.objFuncTrassa(newValue);
      }
    },
    editedItemIdVG(newValue) {
      if (newValue.id != undefined) {
        this.numberTypeTrakt = newValue.number;
        this.objFuncTrassa(newValue);
        this.clearLpTrAllG();
        this.idForAllG = newValue.id;
        this.traktAllGFunc();
      }
    },
    editedItemIdTG(newValue) {
      if (newValue.id != undefined) {
        this.numberTypeTrakt = newValue.number;
        this.objFuncTrassa(newValue);
        this.clearLpTrAllG();
        this.idForAllG = newValue.id;
        this.traktAllGFunc();
        console.log(newValue)
      }
    },
    editedItemIdCHG(newValue) {
      if (newValue.id != undefined) {
        this.objFuncTrassa(newValue);
        this.showObjForTrassa = newValue;
        this.clearLpTrAllG();
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
    save() {
      let id = this.idTrassa.id;
      let id2 = this.objForLTrassa;
      console.log(
        "right trassa props id",
        this.idTrassa,
        "id right trassa",
        this.objForLTrassa
      );
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/trakt/right-trassa/${id}/${id2}/`,
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
    objFuncTrassaIP(item) {
      // this.objForLTrassa = item.id;
      this.showObjForTrassa = item.point
    },
    objFuncTrassa(item) {
      this.objForLTrassa = item.id;
      if (item.point1.point != undefined) {
        this.showObjForTrassa = `(${item.point1.point})${item.name}(${item.point2.point})`;
      } else {
        this.showObjForTrassa = `(${item.point1})${item.name}(${item.point2})`;
      }
    },
    clearLpTrAllG() {
      if (this.editedItemIdLp.id > 0 && this.numberTypeTrakt < 1) {
        this.editedItemIdTrakt = "";
        this.editedItemIdCHG = "";
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.CHG = [];
        this.TG = [];
        this.VG = [];
        this.PG = [];
      } else if (this.numberTypeTrakt == 2) {
        this.editedItemIdPG = "";
      } else if (this.numberTypeTrakt == 3) {
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.PG = [];
      } else if (this.numberTypeTrakt == 4) {
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.VG = [];
        this.PG = [];
      } else if (this.numberTypeTrakt == 5) {
        this.editedItemIdCHG = "";
        this.editedItemIdTG = "";
        this.editedItemIdVG = "";
        this.editedItemIdPG = "";
        this.TG = [];
        this.VG = [];
        this.PG = [];
      } 
    },
    arrayReverseTr2(name) {
      for (let i = 0; i < name.length; i++) {
        if (name[i].type_of_trakt === "ПГ") {
          this.numberTypeTrakt = 1;
        } else if (name[i].type_of_trakt === "ВГ") {
          this.numberTypeTrakt = 2;
        } else if (name[i].type_of_trakt === "ТГ") {
          this.numberTypeTrakt = 3;
        } else if (name[i].type_of_trakt === "ЧГ") {
          this.numberTypeTrakt = 4;
        } else if (name[i].type_of_trakt === "РГ") {
          this.numberTypeTrakt = 5;
        }
        let pushArray = {
          number: this.numberTypeTrakt,
        };
        Object.assign(name[i], pushArray);
      }
    },
    clearAll() {
      this.editedItemIdIP = ""
      this.editedItemIdLp = "";
      this.editedItemIdTrakt = "";
      this.typeTrakt = null;
      this.objForLTrassa = "";
      this.showObjForTrassa = "";
      this.editedItemIdTrakt = "";
      this.editedItemIdCHG = "";
      this.editedItemIdTG = "";
      this.editedItemIdVG = "";
      this.editedItemIdPG = "";
      this.LP = []
      this.trakt = [];
      this.CHG = [];
      this.TG = [];
      this.VG = [];
      this.PG = [];
      this.loaded = false
      this.loadedAllG = false
    },
    traktFunc() {
      this.loaded = false;
      let id = this.editedItemIdLp.id;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.trakt = response.data;
          this.arrayReverseTr2(this.trakt);
          console.log(this.trakt);
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
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/select-object/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.ifFuncArray(response.data);
          // console.log(this.PG, this.VG, this.TG, this.CHG);
          this.loadedAllG = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    getLp(item) {
      let id = item.id ;
      this.$http
        .get(`${this.url.baseUrl}/apps/opu/objects/trakt/select-point/${id}/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.LP = response.data;
          console.log(this.LP);
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
          console.log(this.desserts)
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
  font-size: 18px;
  margin-left: 10px;
  color: black;
}
.vvv {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  background-color: white;
}
</style>
