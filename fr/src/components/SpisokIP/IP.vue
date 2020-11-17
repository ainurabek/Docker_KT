<template>
  <v-container
    id="scroll-target"
    style="max-height: 450px"
    class="overflow-y-auto"
  >
    <v-data-table
      :headers="headers"
      :items="desserts"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>Список Объектов</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>

          <!-- <v-dialog v-model="dialog" max-width="650px">
            <template v-slot:activator="{ on }">
              <v-btn color="primary" dark class="mb-2" v-on="on">Создать объект</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                    <v-autocomplete 
                      v-model="editedItem.point_id"
                      :items="point"
                      item-text="point"
                      item-value="id"
                      full-width
                      label="ИП"
                    ></v-autocomplete>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                       <v-autocomplete
                      v-model="editedItem.tpo_id"
                      :items="tpo"
                      item-text="index"
                      item-value="id"
                      
                      full-width
                      label="Индекс ТПО"
                    ></v-autocomplete>
                    </v-col>
                     <v-col cols="12" sm="6" md="4">
                      <v-autocomplete
                      v-model="editedItem.object_id"
                      :items="desserts"
                      item-text="object_id.name"
                      item-value="object_id.id"
                      
                      full-width
                      label="Название ЛП"
                    ></v-autocomplete>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
                <v-btn color="blue darken-1" text @click="save">Сохранить</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>-->
        </v-toolbar>
      </template>
      <!-- <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>-->
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Обновить</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  props: {
    editedItemTpoProps: null,
    editedItemPointProps: null,
    editedItemOutfitProps: null,
    editedItemNameProps: null,
  },
  data: () => ({
    search: "",
    dialog: false,
    loading: true,
    errored: false,

    headers: [
      {
        text: "",
        align: "start",
        sortable: false,
        value: "",
      },
      { text: "Предприятие", value: "id_outfit" },
      { text: "Название", value: "name" },
      { text: "ИП от", value: "point1" },
      { text: "ИП до", value: "point2" },
    ],
    desserts: [],
    tpo: [],
    point: [],
    editedIndex: -1,
    tpoUrl: {},
    outfitUrl: {},
    nameUrl: {},
    pointUrl: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  watch: {
    editedItemTpoProps(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
    editedItemPointProps(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
    editedItemOutfitProps(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
    editedItemNameProps(newValue) {
      if (newValue != {}) {
        this.initialize();
      }
    },
  },

  mounted() {
    this.initialize();
  },

  methods: {
    initialize() {
      let index = this.editedItemTpoProps;
      let outfit = this.editedItemOutfitProps;
      let point = this.editedItemPointProps;

      console.log(this.editedItemNameProps);
      this.$http
        .get(
          `${this.url.baseUrl}/apps/opu/objects/filter-object/?point=${point}&tpo=${index}&outfit=${outfit}`,
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          this.desserts = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    con() {
      console.log(this.editedItemTpoProps);
    },
  },
};
</script>

<style scoped></style>
