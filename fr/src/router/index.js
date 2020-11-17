import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../components/Home";
import Tpo from "../components/Tpo/Tpo";
import Outfit from "../components/Outfit/Outfit";
import Login from "../components/User/Login";
import Profile from "../components/User/Profile";
import Point from "../components/SpisokIP/Point";
import Department from "../components/User/Department";
import SpisokPO from "../components/SpisokPO/SpisokPO";
import AddTrassa from "../components/AddTr/AddTrassa";
import SpisokArendatorov from "../components/SpisokArendatorov/SpisokArendatorov"
import AddPoint from "../components/SpisokIP/AddPoint"
import DepartmentNCU from "../components/User/DepartmentNCU"
import SpisokKanalov from "../components/SpisokKanalov/SpisokKanalov.vue"
import Forma51 from "../components/Forma51/Forma51.vue"
import EditData51 from "../components/Forma51/EditData51.vue"
import ReservePotoka from "../components/Forma51/ReservePotoka"
import EditPO from "../components/EditPO/EditPO"
import EditTrakt from "../components/editTrakt/EditTrakt"
import EditPG from "../components/editPG/EditPG"
import SpisokIP from "../components/IPnovyi/FiltrIP"
import Forma53 from "../components/Forma53/Forma53"
import FormaArendatorov from "../components/FormaArendatorov/FormaArendatorov"
import ObjectFiltra from "../components/FormaArendatorov/ObjectFiltra"
import CircuitFiltra from "../components/FormaArendatorov/CircuitFiltra"
import JournalSob from "../components/DispJournal/JournalSob/JournalSob"
import CreateJourn from "../components/DispJournal/CreateJour/CreateJourn"
import FiltrSotr from "../components/DispJournal/SpisokSotrudn/FiltrSotr"
import CreateCategoryForDisp from "../components/DispJournal/CreateCategoryForDisp/CreateCategoryForDisp"
import SotrPred from "../components/DispJournal/SotrPred/SotrPred"
import FiltrReport from "../components/DispJournal/Report/FiltrReport"
import FiltrOtchetDisp from "../components/AnalizKachestva/OtchetDisp/FiltrOtchetDisp"
import FiltrFormaAK from "../components/AnalizKachestva/FormaAnaliza//FiltrFormaAK"
import OtchetAK from "../components/AnalizKachestva/OtchetAK/OtchetAK"
import SrednKoef from "../components/AnalizKachestva/OtchetAK/SrednKoef/SrednKoef"
import OtchetP5 from "../components/AnalizKachestva/OtchetAK/Punkt5/Punkt5"
import OtchetP7 from "../components/AnalizKachestva/OtchetAK/Punkt7/Punkt7"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/tpo",
    name: "tpo",
    component: Tpo,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/journalsob",
    name: "journalsob",
    component: JournalSob,
    meta: {
      role3: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/createjourn",
    name: "createjourn",
    component: CreateJourn,
    meta: {
      role3: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/createcatdisp",
    name: "createcatdisp",
    component: CreateCategoryForDisp,
    meta: {
      role3: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/sotrpred",
    name: "sotrpred",
    component: SotrPred,
    meta: {
      role3: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/ncu",
    name: "departncu",
    component: DepartmentNCU,
    meta: {
      role: true,
      role2: false,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/outfit",
    name: "outfit",
    component: Outfit,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      guest: true,
    },
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/point",
    name: "point",
    component: Point,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/depart",
    name: "depart",
    component: Department,
    meta: {
      role: true,
      role2: false,
      role3: false,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/spisokpo",
    name: "spisokpo",
    component: SpisokPO,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/addtrassa",
    name: "addtrassa",
    component: AddTrassa,
    meta: {
      role2: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/otchetdisp",
    name: "otchetdisp",
    component: FiltrReport,
    meta: {
      role3: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/spisoksotrud",
    name: "spisoksotrud",
    component: FiltrSotr,
    meta: {
      role3: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/spisokarenda",
    name: "spisokarenda",
    component: SpisokArendatorov,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/spisokkanalov",
    name: "spisokkanalov",
    component: SpisokKanalov,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/objectfiltra",
    name: "objectfiltra",
    component: ObjectFiltra,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/circuitfiltra",
    name: "circuitfiltra",
    component: CircuitFiltra,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/spisokip",
    name: "spisokip",
    component: SpisokIP,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/reservepotoka",
    name: "reservepotoka",
    component: ReservePotoka,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },

  {
    path: "/forma51",
    name: "forma51",
    component: Forma51,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/forma53",
    name: "forma53",
    component: Forma53,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/editpo",
    name: "editpo",
    component: EditPO,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/edittrakt",
    name: "edittrakt",
    component: EditTrakt,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/editpgitd",
    name: "editpgitd",
    component: EditPG,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/formaarendatorov",
    name: "formaarendatorov",
    component: FormaArendatorov,
    props: true,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/editdata51",
    name: "editdata51",
    component: EditData51,
    props: true,
    meta: {
      role2: true,
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/point-create",
    name: "addpoint",
    component: AddPoint,
    meta: {
      profile: true,
      requiresAuth: true,
    },
  },
  {
    path: "/otchetdispak",
    name: "otchetdispak",
    component: FiltrOtchetDisp,
    props: true,
    meta: {
      // role2: true,
      // profile: true,
      // requiresAuth: true
    },
  },
  {
    path: "/formaak",
    name: "formaak",
    component: FiltrFormaAK,
    props: true,
    meta: {
      // role2: true,
      // profile: true,
      // requiresAuth: true
    },
  },
  {
    path: "/otchetak",
    name: "otchetak",
    component: OtchetAK,
    props: true,
    meta: {
      // role2: true,
      // profile: true,
      // requiresAuth: true
    },
  },
  {
    path: "/otchetsrk",
    name: "otchetsrk",
    component: SrednKoef,
    props: true,
    meta: {
      // role2: true,
      // profile: true,
      // requiresAuth: true
    },
  },
  {
    path: "/otchetp5",
    name: "otchetp5",
    component: OtchetP5,
    props: true,
    meta: {
      // role2: true,
      // profile: true,
      // requiresAuth: true
    },
  },
  {
    path: "/otchetp7",
    name: "otchetp7",
    component: OtchetP7,
    props: true,
    meta: {
      // role2: true,
      // profile: true,
      // requiresAuth: true
    },
  },
];

const router = new VueRouter({
  routes,
  mode: 'history'
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('token') == null) {
      next({
        path: '/login',
        params: {
          nextUrl: to.fullPath
        }
      })
    } else {
      next()
    } 
    if (to.matched.some(record => record.meta.profile)) {
      let user = JSON.parse(localStorage.getItem('is_profile_created'))
      if (user == true) {
        next()
      } else {
        next({
          name: 'profile'
        })
      }
    } else {
      next()
    }
    if (to.matched.some(record => record.meta.role)) {
      let user = JSON.parse(localStorage.getItem('user'))
      if (user.role == 1) {
        next()
      } else {
        next({
          name: 'profile'
        })
      }
    } else {
      next()
    }
    if (to.matched.some(record => record.meta.role2)) {
      let user = JSON.parse(localStorage.getItem('user'))
      if ((user.role == 2 && user.subdepartment == 1) || user.role == 1) {
        next()
      } else {
        next({
          name: 'profile'
        })
      }
    } else {
      next()
    }
    if (to.matched.some(record => record.meta.role3)) {
      let user = JSON.parse(localStorage.getItem('user'))
      if ((user.role == 2 && user.subdepartment == 2) || user.role == 1) {
        next()
      } else {
        next({
          name: 'profile'
        })
      }
    } else {
      next()
    }

  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem('token') == null) {
      next()
    } else {
      next({
        name: 'profile'
      })
    }
  } else {
    next()
  }
})


export default router