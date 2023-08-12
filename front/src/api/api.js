const http = uni.$u.http

export const getByJsCode = (data) => http.post('/getByJsCode', data)
export const getByOpenId = (data) => http.post('/getByOpenId', data)