const statusFilter = (value) => {
	let val = value + '';
	switch (val) {
		case '0':
			return '暂未中奖';
		case '1':
			return '恭喜中奖！';
		default:
			return '状态异常';
	}
}

const rewordFilter = (value) => {
	let val = value + '';
	switch (val) {
		case '0':
			return '暂未中奖';
		case '1':
			return '一等奖';
		case '2':
			return '二等奖';
		case '3':
			return '三等奖';
		case '4':
			return '幸运奖';
		case '5':
			return '额外奖';
		default:
			return '状态异常';
	}
}

export default {
	statusFilter,
	rewordFilter
}
