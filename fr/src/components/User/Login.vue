<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Вход</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form ref="form" v-model="valid" validation>
              <v-text-field
                label="Логин"
                name="login"
                :rules="loginRules"
                prepend-icon="person"
                type="text"
                v-model="username"
              />

              <v-text-field
                id="password"
                label="Пароль"
                name="password"
                prepend-icon="lock"
                type="password"
                :rules="passwordRules"
                v-model="password"
              />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn @click="handleSubmit" :disabled="!valid" color="primary"
              >Войти</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { bus } from "../../main.js";
export default {
  data() {
    return {
      username: "",
      password: "",
      valid: false,
      loginRules: [
        (v) => !!v || "Введите логин",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      passwordRules: [
        (v) => !!v || "Введите пароль",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      if (this.password.length > 0) {
        this.$http
          .post("http://0.0.0.0:8000/apps/accounts/login/", {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            console.log(response.data);
            // let role = response.data.user.role;
            // let depart = response.data.user.department;
            // let subdepartment = response.data.user.subdepartment;
            localStorage.setItem("user", JSON.stringify(response.data.user));
            localStorage.setItem("userFull", JSON.stringify(response.data));
            localStorage.setItem("token", response.data.token);
            localStorage.setItem(
              "is_profile_created",
              response.data.user.is_profile_created
            );

            if (localStorage.getItem("token") != null) {
              this.$emit("loggedIn");
              bus.$emit("updateNav");
              if (this.$route.params.nextUrl != null) {
                // bus.$emit("updateNav");
                this.$router.push(this.$route.params.nextUrl);
              } else {
                this.$router.push("/");
                //  bus.$emit("updateNav")
                // } else if (role == 2 && subdepartment == 1) {
                //   this.$router.push("/");
                // } else if (role == 2 && subdepartment == 2) {
                //    this.$router.push("/");
                // }
              }
            }
          })
          .catch(function(error) {
            console.error(error.response);
          });
      }
    },
  },
};
</script>
