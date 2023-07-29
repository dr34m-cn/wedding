import request from '@/utils/request'

export function getAllUser(data) {
	return request({
		url: 'getAllUser',
		headers: {
			isMask: false
		},
		method: 'post',
		data
	})
}

export function setUserStatus(data) {
	return request({
		url: 'setUserStatus',
		headers: {
			isMask: false
		},
		method: 'post',
		data
	})
}