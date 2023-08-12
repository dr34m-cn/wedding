import request from '@/utils/request'

export function getAllUser(data) {
	return request({
		url: 'getAllUser',
		method: 'post',
		data
	})
}

export function setUserStatus(data) {
	return request({
		url: 'setUserStatus',
		method: 'post',
		data
	})
}

export function resetAllStatus(data) {
	return request({
		url: 'resetAllStatus',
		method: 'post',
		data
	})
}