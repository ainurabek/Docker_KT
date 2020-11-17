<template>
  <v-dialog v-model="show" max-width="700px">
    <v-card>
      <v-card-title>
        <span class="headline">Изменить коэффициент</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" validation>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                (ВОЛС) КЛС
                <v-text-field
                  v-model="editedItem.outfit_period_of_time_kls"
                  label="Продолжительность всех ПВ кан*час"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                (ВОЛС) КЛС
                <v-text-field
                  v-model="editedItem.length_kls"
                  label="Протяженность кан*км зад."
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                РРЛ
                <v-text-field
                  v-model="editedItem.outfit_period_of_time_rrl"
                  label="Продолжительность всех ПВ кан*час"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                РРЛ
                <v-text-field
                  v-model="editedItem.length_rrl"
                  label="Протяженность кан*км"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                ВЛС
                <v-text-field
                  v-model="editedItem.outfit_period_of_time_vls"
                  label="Продолжительность всех ПВ кан*час"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                ВЛС
                <v-text-field
                  v-model="editedItem.length_vls"
                  label="Протяженность кан*км"
                  type="number"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click.stop="close">Отмена</v-btn>
        <v-btn color="blue darken-1" text @click.stop="save">Сохранить</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { bus } from "../../../../main"

export default {
  props: {
    itemForEdit: {
      type: Object,
      default: function() {
        return {};
      },
    },
    value: {
      type: Boolean,
    }
  },
  data: () => ({
    valid: false,
    editedItem: {
      outfit_period_of_time_kls: "",
      outfit_period_of_time_rrl: "",
      outfit_period_of_time_vls: "",
      length_kls: "",
      length_vls: "",
      length_rrl: ""
    },
    defaultItem: {
      outfit_period_of_time_kls: "",
      outfit_period_of_time_rrl: "",
      outfit_period_of_time_vls: "",
      length_kls: "",
      length_vls: "",
      length_rrl: ""
    },
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  computed: {
    show: {
      get () {
        return this.value
      },
      set (value) {
         this.$emit('input', value)
      }
    }
  },
  watch: {
    itemForEdit(newValue) {
      if(newValue.id != undefined) {
        this.editItem()
      }
      console.log(newValue)
    }
  },
  methods: {
    editItem() {
      this.idForEdit = this.itemForEdit.id
      this.editedItem = Object.assign({}, this.itemForEdit);
      console.log(this.itemForEdit)
    },
    save() {
      this.$http
        .put(
          `${this.url.baseUrl}/apps/analysis/punkt5/update/${this.idForEdit}/`,
          {
            outfit_period_of_time_kls: this.editedItem.outfit_period_of_time_kls,
            outfit_period_of_time_rrl: this.editedItem.outfit_period_of_time_rrl,
            outfit_period_of_time_vls: this.editedItem.outfit_period_of_time_vls,
            length_kls: this.editedItem.length_kls,
            length_vls: this.editedItem.length_vls,
            length_rrl: this.editedItem.length_rrl
          },
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == 200) {
            bus.$emit("updateOtchetP5")
          }
          console.log(response);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => {
          this.close()
          this.loading = false
        });
    },
    close() {
      this.show = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        console.log(this.editedItem)
      });
    },
  }
};
</script>
