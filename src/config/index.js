const CONFIG = {
    // 开发环境配置
    development: {
				baseUrl: 'https://v1.hitokoto.cn' // 后台接口请求地址
    },
    // 生产环境配置
    production: {
				baseUrl: 'https://v1.hitokoto.cn' // 后台接口请求地址
    }
};
export default CONFIG[process.env.NODE_ENV];