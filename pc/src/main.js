import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import mixin from "@/store/mixin.js"

import "@/assets/style/style.scss";

import store from '@/store';
Vue.mixin(mixin);

import filters from '@/utils/filters';
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]));

import App from './App.vue'

Vue.config.productionTip = false

Vue.use(ElementUI)

new Vue({
	store,
	render: h => h(App)
}).$mount('#app')
