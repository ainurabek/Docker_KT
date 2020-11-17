<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="mx-auto mb-5" align="center">
          <v-navigation-drawer class="primary" dark permanent width="100%">
            <v-list>
              <v-list-item v-for="item in items" :key="item.title" :to="item.url" link>
                <!-- <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>-->
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
        </v-card>
        <v-card class="mx-auto mb-5" align="center">
          <v-navigation-drawer class="primary" dark permanent width="100%">
            <v-list>
              <v-list-item v-for="item in items1" :key="item.title" link>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
        </v-card>
        <v-card class="mx-auto mb-5" align="center">
          <v-navigation-drawer class="primary" dark permanent width="100%">
            <v-list>
              <v-list-item v-for="item in items2" :key="item.title" link>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
        </v-card>
        <template>
          <div class="pa-2">
            <v-btn @click="logout" block color="grey">Выйти</v-btn>
          </div>
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      items: [{ title: "НЦУ", icon: "dashboard", url: "/ncu" }],
      items1: [{ title: "ЦСП", icon: "account_box" }],
      items2: [{ title: "ЦКТ", icon: "gavel" }]
    };
  },
  methods: {
    logout(e) {
      e.preventDefault();
      if (localStorage.getItem("token") != null) {
        localStorage.removeItem("token");
        this.$router.push("/");
      }
    }
  }
};
</script>