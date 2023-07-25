const statusFilter = (value) => {
	let val = value + '';
	switch (val) {
		case '0':
			return '未开奖';
		case '1':
			return '开奖中...';
		case '2':
			return '恭喜中奖！';
		case '3':
			return '很遗憾，您未中奖';
		default:
			return '状态异常';
	}
}

export default {
	statusFilter
}
