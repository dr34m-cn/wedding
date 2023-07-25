import Vue from 'vue';

import uView from "uview-ui";
Vue.use(uView);

let vuexStore = require("@/store/$u.mixin.js");
Vue.mixin(vuexStore);

import store from '@/store';

import filters from '@/utils/filters';
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]));

import App from './App'


Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
	store,
	...App
});

// 引入请求封装，将app参数传递到配置中
require('@/utils/request.js')(app)

app.$mount()
