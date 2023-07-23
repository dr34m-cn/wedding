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
