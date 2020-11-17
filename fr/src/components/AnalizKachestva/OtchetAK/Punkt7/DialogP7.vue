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
                КЛС
                <v-text-field
                  v-model="editedItem.total_number_kls"
                  label="Общее количество линейных трактов"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                КЛС
                <v-text-field
                  v-model="editedItem.corresponding_norm_kls"
                  label="в т.ч.  соответствующих норме"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                РРЛ
                <v-text-field
                  v-model="editedItem.total_number_vls"
                  label="Общее количество линейных трактов"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                РРЛ
                <v-text-field
                  v-model="editedItem.corresponding_norm_vls"
                  label="в т.ч.  соответствующих норме"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                ВЛС
                <v-text-field
                  v-model="editedItem.total_number_rrl"
                  label="Общее количество линейных трактов"
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                ВЛС
                <v-text-field
                  v-model="editedItem.corresponding_norm_rrl"
                  label="в т.ч.  соответствующих норме"
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
      total_number_kls: null,
      corresponding_norm_kls: null,
      total_number_vls: null,
      corresponding_norm_vls: null,
      total_number_rrl: null,
      corresponding_norm_rrl: null
    },
    defaultItem: {
      total_number_kls: null,
      corresponding_norm_kls: null,
      total_number_vls: null,
      corresponding_norm_vls: null,
      total_number_rrl: null,
      corresponding_norm_rrl: null
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
          `${this.url.baseUrl}/apps/analysis/punkt7/update/${this.idForEdit}/`,
          {
            total_number_kls: this.editedItem.total_number_kls,
            corresponding_norm_kls: this.editedItem.corresponding_norm_kls,
            total_number_vls: this.editedItem.total_number_vls,
            corresponding_norm_vls: this.editedItem.corresponding_norm_vls,
            total_number_rrl: this.editedItem.total_number_rrl,
            corresponding_norm_rrl: this.editedItem.corresponding_norm_rrl
          },
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == 200) {
            bus.$emit("updateOtchetP7")
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
