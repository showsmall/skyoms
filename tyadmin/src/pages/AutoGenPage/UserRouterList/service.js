import request from 'umi-request';

export async function queryUserRouter(params) {
  return request('/api/xadmin/v1/user_router', {
    params,
  });
}
export async function removeUserRouter(params) {
  return request(`/api/xadmin/v1/user_router/${params}`, {
    method: 'DELETE',
  });
}
export async function addUserRouter(params) {
  return request('/api/xadmin/v1/user_router', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateUserRouter(params, id) {
  return request(`/api/xadmin/v1/user_router/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
