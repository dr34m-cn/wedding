module.exports = {
	productionSourceMap: false,
	devServer: {
	  host: '0.0.0.0',
	  port: 80,
	  open: true,
	  proxy: {
	    [process.env.VUE_APP_BASE_API]: {
	      target: `http://118.195.232.229:9014/get`,
	      changeOrigin: true,
	      pathRewrite: {
	        ['^' + process.env.VUE_APP_BASE_API]: ''
	      }
	    }
	  },
	  disableHostCheck: true
	},
}
