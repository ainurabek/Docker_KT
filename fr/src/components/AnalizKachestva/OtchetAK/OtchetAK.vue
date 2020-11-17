<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6" md="6">
        <v-container>
          <v-card v-if="loadedOtchList" class="mx-auto" max-width="500">
            <v-list shaped>
              <v-list-item-group v-model="modelOtch">
                <template v-for="(item, i) in itemsTittleOtch">
                  <v-divider v-if="!item" :key="`divider-${i}`"></v-divider>
                  <v-list-item
                    v-else
                    :key="`item-${i}`"
                    :value="item"
                    active-class="deep-purple--text text--accent-4"
                  >
                    <template v-slot:default="{ active }">
                      <v-list-item-content>
                        <v-list-item-title v-text="item.name"></v-list-item-title>
                      </v-list-item-content>
                      <v-list-item-action>
                        <v-checkbox
                          :input-value="active"
                          color="deep-purple accent-4"
                        ></v-checkbox>
                      </v-list-item-action>
                    </template>
                  </v-list-item>
                </template>
              </v-list-item-group>
            </v-list>
          </v-card>
          <v-toolbar-title v-else>Создайте отчет</v-toolbar-title>
        </v-container>
      </v-col>
      <v-col cols="12" sm="6" md="6">
        <DataForListAK
        :itemOtch="modelOtch"
        ></DataForListAK>
        <CreateOtchetAK></CreateOtchetAK>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { bus } from "../../../main"
import CreateOtchetAK from "./CreateOtchetAK"
import DataForListAK from "./DataForListAK"

export default {
  components: { CreateOtchetAK, DataForListAK },
  data: () => ({
    errored: false,
    loading: false,
    loadedOtchList: false,
    itemsOtch: [],
    modelOtch: {},
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  mounted() {
    this.initOtch();
    bus.$on("updateOtchetAK",() => {
      this.initOtch()
    })
  },
  beforeDestroy() {
    bus.$off("updateOtchetAK")
  },
  methods: {
    modItemsOtch() {
      if( this.itemsOtch.length > 0 ) {
        this.loadedOtchList = true
        this.itemsTittleOtch = this.itemsOtch.map(t => {
        return {name:`${t.name} - (${t.date_from}/${t.date_to})`, id: t.id, date_to:t.date_to, date_from:t.date_from}
      });
      console.log(this.itemsTittleOtch)
      }
    },
    initOtch() {
      this.loadedOtchList = false
      this.$http
        .get(`${this.url.baseUrl}/apps/analysis/form/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          if (response.status == 200) {
            this.itemsOtch = response.data;
            this.modItemsOtch();
          }
          console.log(response);
        })
        .catch((error) => {
          console.log(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>
