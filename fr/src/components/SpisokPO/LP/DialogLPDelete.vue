<template>
  <v-dialog v-model="show" max-width="500px">
    <v-card>
      <v-card-title class="headline"
        >Вы уверены что хотите удалить?</v-card-title
      >
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeDelete">Отмена</v-btn>
        <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { bus } from "../../../main";

export default {
  props: {
    value: {
      type: Boolean,
    },
    itemForDelete: {
      type: Object,
      default: function() {
        return {};
      },
    },
  },
  data: () => ({
    valid: false,
    idForDelete: "",
    url: {
      baseUrl: "http://0.0.0.0:8000",
    },
  }),
  computed: {
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
  watch: {
    itemForDelete(newValue) {
      if (newValue.id != undefined) {
        this.idDeleteItem(newValue);
      }
      console.log(newValue);
    },
  },
  methods: {
    idDeleteItem(item) {
      this.idForDelete = item.id;
    },
    closeDelete() {
      this.show = false;
    },
    deleteItemConfirm() {
      this.$http
        .delete(
          `${this.url.baseUrl}/apps/opu/objects/lp/${this.idForDelete}/`,
          {
            headers: { Authorization: `Token ${localStorage.token}` },
          }
        )
        .then((response) => {
          if (response.status == "204") {
            bus.$emit("deleteSPO_LP");
          }
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
          this.closeDelete();
        });
    },
  },
};
</script>
