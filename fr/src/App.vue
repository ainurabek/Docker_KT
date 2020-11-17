<template>
  <v-app>
    <v-navigation-drawer
      app
      hide-overlay
      class="mx-auto"
      sc
      v-model="drawer"
      :color="color"
      :expand-on-hover="expandOnHover"
      :mini-variant="miniVariant"
      :right="right"
      :src="bg"
      dark
    >
      <v-list dense nav class="py-0" v-if="userRole == 1">
        <v-list-item-content>
          <v-list-item-title class="mt-2 ml-2"
            >Имя: {{ username }}
            <v-btn @click="logout" class="ml-8" small color="success"
              >Выйти</v-btn
            >
          </v-list-item-title>
        </v-list-item-content>
        <v-divider></v-divider>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>face</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/profile" tag="span" class="pointer"
              >Профиль сотрудника</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/" tag="span" class="pointer"
              >Домашняя страница</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-group color="white">
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>ОПУ</v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item
            v-for="item in itemsOpu"
            :key="item.title"
            :to="item.url"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
        <v-list-group color="white">
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Диспетчерская cлужба</v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item
            v-for="item in itemsDisp"
            :key="item.title"
            :to="item.url"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
      <v-list dense nav class="py-0" v-if="userRole == 2">
        <v-list-item-content>
          <v-list-item-title class="mt-2 ml-2"
            >Имя: {{ username }}
            <v-btn @click="logout" class="ml-12" small color="success"
              >Выйти</v-btn
            >
          </v-list-item-title>
        </v-list-item-content>
        <v-divider></v-divider>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>face</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/profile" tag="span" class="pointer"
              >Профиль сотрудника</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/" tag="span" class="pointer"
              >Домашняя страница</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item
          v-for="item in itemsOpu"
          :key="item.title"
          :to="item.url"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list dense nav class="py-0" v-if="userRole == 3">
        <v-list-item-content>
          <v-list-item-title class="mt-2 ml-2"
            >Имя: {{ username }}
            <v-btn @click="logout" class="ml-12" small color="success"
              >Выйти</v-btn
            >
          </v-list-item-title>
        </v-list-item-content>
        <v-divider></v-divider>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>face</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/profile" tag="span" class="pointer"
              >Профиль сотрудника</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/" tag="span" class="pointer"
              >Домашняя страница</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item
          v-for="item in itemsDisp"
          :key="item.title"
          :to="item.url"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-group color="white">
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>ОПУ</v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item
            v-for="item in itemsDisp2"
            :key="item.title"
            :to="item.url"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
      <v-list dense nav class="py-0" v-if="userRole == 4">
        <v-list-item-content>
          <v-list-item-title class="mt-2 ml-2"
            >Имя: {{ username }}
            <v-btn @click="logout" class="ml-12" small color="success"
              >Выйти</v-btn
            >
          </v-list-item-title>
        </v-list-item-content>
        <v-divider></v-divider>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>face</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/profile" tag="span" class="pointer"
              >Профиль сотрудника</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title
            ><router-link to="/" tag="span" class="pointer"
              >Домашняя страница</router-link
            ></v-list-item-title
          >
        </v-list-item>
        <v-list-item
          v-for="item in itemsAK"
          :key="item.title"
          :to="item.url"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list dense nav class="py-0" v-if="userRole == 5">
        
       <v-list-item
          
        >
          <v-list-item-icon>
            <v-icon>face</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Войдите в систему</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app color="primary" dark :src="bg">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>

      <v-toolbar-title>
        <router-link to="/" tag="span" class="pointer"
          >КыргызТелеком</router-link
        >
      </v-toolbar-title>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import { bus } from "./main";
export default {
  data() {
    return {
      drawer: true,
      items: [{ title: "Профиль сотрудника", icon: "face", url: "/profile" }],
      itemsOpu: [
        {
          title: "Список простых объектов",
          icon: "mdi-view-dashboard",
          url: "/spisokpo",
        },
        {
          title: "Создание трассы",
          icon: "mdi-view-dashboard",
          url: "/addtrassa",
        },
        { title: "Фильтр объектов", icon: "mdi-view-dashboard", url: "/point" },
        { title: "Список ИП", icon: "mdi-view-dashboard", url: "/spisokip" },
        {
          title: "Список ИП создание",
          icon: "mdi-view-dashboard",
          url: "/point-create",
        },
        {
          title: "Список предприятий",
          icon: "mdi-view-dashboard",
          url: "/outfit",
        },
        { title: "Распоряжения", icon: "mdi-view-dashboard", url: "/spisokko" },
        {
          title: "Форма Арендаторов",
          icon: "mdi-view-dashboard",
          url: "/formaarendatorov",
        },
        {
          title: "Список арендаторов",
          icon: "mdi-view-dashboard",
          url: "/spisokarenda",
        },
        { title: "Форма 5.1", icon: "mdi-view-dashboard", url: "/forma51" },
        { title: "Форма 5.3", icon: "mdi-view-dashboard", url: "/forma53" },
        // {
        //   title: "Список транзитных каналов",
        //   icon: "mdi-view-dashboard",
        //   url: "/spisoktk",
        // },
        { title: "Список ТПО", icon: "mdi-view-dashboard", url: "/tpo" },
      ],
      itemsDisp: [
        {
          title: "Журнал событий",
          icon: "mdi-view-dashboard",
          url: "/journalsob",
        },
        {
          title: "Список сотрудников",
          icon: "mdi-view-dashboard",
          url: "/spisoksotrud",
        },
        {
          title: "Сотрудники предприятий",
          icon: "mdi-view-dashboard",
          url: "/sotrpred",
        },
        {
          title: "Создание примечаний",
          icon: "mdi-view-dashboard",
          url: "/createcatdisp",
        },
        { title: "Отчет", icon: "mdi-view-dashboard", url: "/otchetdisp" },
        {
          title: "Справочник",
          icon: "mdi-view-dashboard",
          url: "/spravkadisp",
        },
      ],
      itemsDisp2: [
        { title: "Фильтр объектов", icon: "mdi-view-dashboard", url: "/point" },
        { title: "Список ИП", icon: "mdi-view-dashboard", url: "/spisokip" },
        {
          title: "Список ИП создание",
          icon: "mdi-view-dashboard",
          url: "/point-create",
        },
        {
          title: "Список предприятий",
          icon: "mdi-view-dashboard",
          url: "/outfit",
        },

        {
          title: "Форма Арендаторов",
          icon: "mdi-view-dashboard",
          url: "/formaarendatorov",
        },
        {
          title: "Список арендаторов",
          icon: "mdi-view-dashboard",
          url: "/spisokarenda",
        },
        { title: "Список ТПО", icon: "mdi-view-dashboard", url: "/tpo" },
        {
          title: "Список простых объектов",
          icon: "mdi-view-dashboard",
          url: "/spisokpo",
        },
      ],
      itemsAK: [
        {
          title: "Отчет дисп. службы",
          icon: "mdi-view-dashboard",
          url: "/otchetdispak",
        },
        {
          title: "Отчет АК",
          icon: "mdi-view-dashboard",
          url: "/otchetak",
        },
        {
          title: "Форма анализа качества",
          icon: "mdi-view-dashboard",
          url: "/formaak",
        },
      ],
      color: "primary",
      colors: ["primary", "blue", "success", "red", "teal"],
      right: false,
      miniVariant: false,
      expandOnHover: false,
      username: "",
      userRole: "",
      subdepartmentUser: "",
      background: true,
    };
  },
  computed: {
    bg() {
      return this.background
        ? "https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
        : undefined;
    },
  },
  watch: {
    userRole() {
      this.pushItem();
    },
  },
  mounted() {
    this.setUser();
    this.pushItem();
    bus.$on("updateNav", () => {
      this.setUser();
      this.pushItem();
    });
  },
  beforeDestroy() {
    bus.$off("updateNav")
  },
  created() {
    
  },
  methods: {
    logout(e) {
      e.preventDefault();
      this.$http
        .get(`http://0.0.0.0:8000/apps/accounts/logout/`, {
          headers: { Authorization: `Token ${localStorage.token}` },
        })
        .then((response) => {
          if (response.status == 200) {
            if (localStorage.getItem("token") != null) {
              localStorage.removeItem("idPunkt5")
              localStorage.removeItem("idSrK")
              localStorage.removeItem("idPOForEdit")
              localStorage.removeItem("idTraktForEdit")
              localStorage.removeItem("user");
              localStorage.removeItem("token");
              localStorage.removeItem("is_profile_created");
              localStorage.removeItem("userFull");
              this.$router.push("/login");
              this.pushItem()
            }
          }
          console.log(response.status);
        })
        .catch((error) => {
          console.log(error.response.data);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    setUser() {
      let user = JSON.parse(localStorage.getItem("user"));
      if (user != undefined) {
        this.username = user.username;
        console.log(user);
      }
    },
    pushItem() {
      let user = JSON.parse(localStorage.getItem("user"));
      if (user != undefined) {
      console.log(user.role);
      if (user.role == 1) {
        this.userRole = 1;
        console.log(user.role);
      } else if (user.role == 2 && user.subdepartment == 1) {
        this.userRole = 2;
        console.log(user.subdepartment);
      } else if (user.role == 2 && user.subdepartment == 2) {
        this.userRole = 3;
        console.log(this.userRole);
      } else if (user.role == 2 && user.subdepartment == 3) {
        this.userRole = 4;
        console.log(this.userRole);
      } 
      } else if (user == null || user == undefined) {
        this.userRole = 5;
        console.log(this.userRole);
      }
    },
  },
};
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>
