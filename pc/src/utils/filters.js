const projectStatusFilter = (value) => {
	let statusList = ['未开始', '进行中', '已结束'];
	return statusList[value] ? statusList[value] : "--";
}
export default {
	projectStatusFilter
}
