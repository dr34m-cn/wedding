// 此vm参数为页面的实例，可以通过它引用vuex中的变量
import indexConfig from '@/config/index.js';
module.exports = (vm) => {
	// 初始化请求配置
	uni.$u.http.setConfig((config) => {
		/* config 为默认全局配置*/
		config.baseURL = indexConfig.baseUrl; /* 根域名 */
		return config
	})

	// 请求拦截
	uni.$u.http.interceptors.request.use((config) => { // 可使用async await 做异步操作
		// 初始化请求拦截器时，会执行此方法，此时data为undefined，赋予默认{}
		config.data = config.data || {}
		return config
	}, config => { // 可使用async await 做异步操作
		return Promise.reject(config)
	})

	// 响应拦截
	uni.$u.http.interceptors.response.use((response) => {
		/* 对响应成功做点什么 可使用async await 做异步操作*/
		const data = response.data
		if (data.code) {
			if (data.code == 401) {
				// TODO 对登录失效做点什么
				return Promise.reject(data)
			} else if (data.code != 200) {
				uni.$u.toast(data.msg || `系统接口${data.code}异常`);
				return Promise.reject(data)
			}
			return data === undefined ? {} : data
		}
		return data
	}, (response) => {
		// 对响应错误做点什么 （statusCode !== 200）
		uni.$u.toast(`系统接口${response.statusCode}异常`)
		return Promise.reject(response)
	})
}
