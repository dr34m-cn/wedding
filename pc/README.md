# 通用前端框架

本通用框架基于`ElementUI`，封装了日常开发中最常用的接口请求、数据中心、环境配置等操作，上手即用。

## 1. 运维

### 1.1 依赖安装
```shell
npm install
```

### 1.2 运行
```shell
# dev
npm run dev

# 生产
npm run serve
```

### 1.3 构建
```shell
# dev
npm run build:dev

# 生产
npm run build
```

## 2. 开发

### 2.1 启动

```shell
# 安装依赖
npm install

# dev
npm run dev

# 生产
npm run serve
```

### 2.2 说明

#### 2.2.1 配置

通用配置请放在`/.env.xxx`中，例如后端地址。

#### 2.2.2 数据中心

数据中心统一管理需要在全局使用的数据，可以临时存储（刷新页面等操作数据就会丢失）或者持久化存储。

在这里定义和存储的数据是全局动态响应的，这让您无需繁琐地写监听方法。

配置文件在`/src/store/index.js`，建议命名为`vuex_`开头，以便与页面数据区分避免冲突。

##### 2.2.2.1 定义

###### 2.2.2.1.1 临时存储

直接在`/src/store/index.js`中定义，如下边的`vuex_tmp`

```js
const store = new Vuex.Store({
	state: {
		vuex_token: lifeData.vuex_token ? lifeData.vuex_token : null,
		vuex_tmp: null
	},
	
	...
	
})
```

###### 2.2.2.1.2 持久化存储

在`/src/store/index.js`中定义，并写入`saveStateKeys`中，如下边的`vuex_token`，定义的时候格式为`vuex_token: lifeData.vuex_token ? lifeData.vuex_token : null`

```js
// 需要永久存储，且下次APP启动需要取出的，在state中的变量名
let saveStateKeys = ['vuex_token'];

...

const store = new Vuex.Store({
	state: {
		vuex_token: lifeData.vuex_token ? lifeData.vuex_token : null,
		vuex_tmp: null
	},
	
	...
	
})
```

##### 2.2.2.2 使用

###### 2.2.2.2.1 取值

* 页面`<template>`中取值`{{ vuex_token }}`
* js代码（包括`App.vue`页面）`<script>`中取值`this.vuex_token`
* 通用组件中（须获取上下文vm）取值`vm.vuex_token`
* 通用组件不能获取上下文的，如下取值

	```js
	import store from '@/store';
	store.state.vuex_token
	```

###### 2.2.2.2.2 设值

可以设定值的类型为`基本数据类型`和`可以进行序列化的对象/列表等`。

对于可以获取上下文的，如下设值

```js
// 字符串
this.$setVuex('vuex_token', "xxxxx");
// 对象
this.$setVuex('vuex_token', {
	id: 1,
	key: 'token',
	value: 'xxxxx'
});
```

对于不能获取上下文的，如下设值

```js
import store from '@/store';
store.commit('$uStore', {
	name: 'vuex_token',
	value: 'xxx'
})
```

#### 2.2.3 接口

##### 2.2.3.1 统一拦截器

接口拦截器在`/src/utils/request.js`中，可以根据需要自行修改；

对于请求：
* 凡是请求配置中未配置`header.isToken`为`false`，且当前已有`token`的（`vuex_token`有值），将自动在请求头`header.Authorization`存入已有的`token`值；
* 凡是请求配置中未配置`header.isMask`为`false`，若请求超过指定时间（暂定`100ms`）未能得到响应，则自动出现加载中蒙版，请求结束或出错后蒙版消失；

对于响应：
* 响应值`response.statusCode`非`200`的，将拦截，弹框提示并抛出异常，可在接口`catch`中捕获；
* 响应数据存在`response.data.code`字段的，判断`code`值：
	* 值为`200`的，将返回`response.data`，可在接口`then`中获取；
	* 值为`401`将拦截并抛出异常，可在接口`catch`中捕获，建议在拦截器中统一处理；
	* 值为`500`，弹框提示并抛出异常，可在接口`catch`中捕获；
	* 值非以上三种将拦截并抛出异常，可在接口`catch`中捕获；
* 响应数据不存在`response.data.code`字段的，将返回`response.data`，可在接口`then`中获取。

##### 2.2.3.2 api集中管理

在`/src/api/`目录下新建`api.js`文件，内容如下
```js
import request from '@/utils/request'

export function getData1(id) {
  return request({
    url: `/get/xxx/${id}`,
    method: 'get'
  })
}

export function getData2(params) {
  return request({
    url: '/get/xxx',
		header: {
			isMask: false
		},
    method: 'get',
		params
  })
}

export function postData(data) {
  return request({
    url: '/post/xxx',
    method: 'post',
		data
  })
}
```

##### 2.2.3.3 api使用

```js
import {
	getData1,
	getData2,
	postData
} from '@/api/api.js';

getData1(1).then(res => {
	// 经过拦截器的处理，进入到这里的请求都是成功请求，无需考虑请求失败的情况
	console.log('res',res)
}).catch(err=>{
	// 多数情况下，不需要写catch，因为拦截器已经进行了弹窗提示等操作
	// 但当页面需要对错误进行处理时（例如关闭加载动画，取消按钮loading等），就需要在catch中操作
	console.log('err',err)
})

getData2({
	id: 1
}).then(
	...
).catch(
	...
)

postData({
	id: 1
}).then(
	...
).catch(
	...
)
```

#### 2.2.4 全局过滤器

##### 2.2.4.1 定义

全局过滤器定义在`/src/utils/filters.js`中，可参照其增加自己的过滤规则，常用定义方式如下

```js
// 0-男,1-女
const sexFilter = (value) => {
	let sexList = ['男', '女'];
	return sexList[value] ? sexList[value] : "--";
}

// xx-小学及以下，cz-初中，gz-高中及以上
const educationFilter = (value) => {
	switch (value) {
		case 'xx':
			return '小学及以下';
		case 'cz':
			return '初中';
		case 'gz':
			return '高中及以上';
		default:
			return '--';
	}
}

export default {
	sexFilter,
	educationFilter
}
```

##### 2.2.4.2 使用

因为已经在`main.js`中定义如下

```js
import filters from '@/utils/filters';
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]));
```

所以页面中无需引入，如下直接使用

```html
<view>过滤器-性别：{{ sex | sexFilter }}</view>
```

效果：当`sex`为`0`，页面输出`男`；当`sex`为`1`，页面输出`女`