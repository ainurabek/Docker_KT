import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import Axios from 'axios'
import DatetimePicker from 'vuetify-datetime-picker'
import JsonExcel from 'vue-json-excel'
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'
import moment from "moment";





Vue.prototype.$http = Axios;
Vue.prototype.$moment = moment;
moment.locale('ru')
Vue.use(DatetimePicker)
Vue.component('downloadExcel', JsonExcel)
Vue.use(Chartkick.use(Chart))



Vue.config.productionTip = false


export const bus = new Vue();

new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app')