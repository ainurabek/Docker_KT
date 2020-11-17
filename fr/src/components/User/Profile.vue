<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Профиль сотрудника</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form ref="form" v-model="valid" validation>
              <v-text-field
                label="Должность"
                name="position"
                :rules="positionRules"
                prepend-icon="person"
                type="text"
                v-model="position"
              />
              <v-text-field
                label="Имя"
                name="firstName"
                :rules="firstNameRules"
                prepend-icon="person"
                type="text"
                v-model="firstName"
              />

              <v-text-field
                label="Фамилия"
                name="lastName"
                prepend-icon="person"
                type="text"
                :rules="lastNameRules"
                v-model="lastName"
              />
              <v-text-field
                label="Отчество"
                name="middleName"
                prepend-icon="person"
                type="text"
                :rules="middleNameRules"
                v-model="middleName"
              />
              <v-text-field
                label="Номер телефона"
                name="phoneNumber"
                prepend-icon="phone"
                type="text"
                :rules="phoneNumberRules"
                v-model="phoneNumber"
              />
              <v-select
                label="Пол"
                name="gender"
                prepend-icon="person"
                :rules="genderRules"
                v-model="gender"
                :items="genderAr"
                item-value="gen"
                item-text="name"
              />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn @click="saveOrEditProfile" :disabled="!valid" color="primary"
              >Сохранить профиль</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      firstName: "",
      position: "",
      lastName: "",
      middleName: "",
      phoneNumber: "",
      gender: "",
      dataUser: "",
      genderAr: [
        {
          gen: "M",
          name: "Мужской",
        },
        {
          gen: "F",
          name: "Женский",
        },
      ],
      valid: false,
      genderRules: [(v) => !!v || "Выберите пол"],
      positionRules: [
        (v) => !!v || "Введите должность",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      firstNameRules: [
        (v) => !!v || "Введите имя",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      lastNameRules: [
        (v) => !!v || "Введите фамилию",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
      middleNameRules: [],
      phoneNumberRules: [
        (v) => !!v || "Введите номер телефона",
        (v) => (v && v.length <= 20) || "Name must be less than 20 characters",
      ],
    };
  },
  mounted() {
    this.initialize();
  },
  methods: {
    editProfile() {
      console.log(this.dataUser);
      this.firstName = this.dataUser[0].first_name;
      this.lastName = this.dataUser[0].last_name;
      this.position = this.dataUser[0].position;
      this.middleName = this.dataUser[0].middle_name;
      this.gender = this.dataUser[0].gender;
      this.phoneNumber = this.dataUser[0].phone_number;
      localStorage.removeItem("is_profile_created");
      localStorage.setItem(
        "is_profile_created",
        this.dataUser[0].user.is_profile_created
      );
    },
    initialize() {
      this.$http
        .get(`http://0.0.0.0:8000/apps/accounts/profile_list/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          this.dataUser = response.data;
          this.editProfile();
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    saveOrEditProfile() {
      let user = JSON.parse(localStorage.getItem("is_profile_created"));
      if (user == true) {
        this.editProfileSave();
      } else if (user == false) {
        this.profileSave();
      }
    },
    editProfileSave() {
      let id = this.dataUser[0].id;
      console.log(id);
      this.$http
        .put(
          `http://0.0.0.0:8000/apps/accounts/profile_list/${id}/`,
          {
            position: this.position,
            first_name: this.firstName,
            last_name: this.lastName,
            middle_name: this.middleName,
            phone_number: this.phoneNumber,
            gender: this.gender,
          },
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          if (response.status == 200) {
            this.initialize();
            this.$router.push("/");
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.error(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    profileSave() {
      console.log();
      this.$http
        .post(
          `http://0.0.0.0:8000/apps/accounts/profile_create/`,
          {
            position: this.position,
            first_name: this.firstName,
            last_name: this.lastName,
            middle_name: this.middleName,
            phone_number: this.phoneNumber,
            gender: this.gender,
          },
          { headers: { Authorization: `Token ${localStorage.token}` } }
        )
        .then((response) => {
          if (response.status == 201) {
            this.initialize();
            this.$router.push("/");
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.error(error.response);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
  },
};
</script>
