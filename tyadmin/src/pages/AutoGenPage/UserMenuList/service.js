import request from 'umi-request';

export async function queryUserMenu(params) {
  return request('/api/xadmin/v1/user_menu', {
    params,
  });
}
export async function removeUserMenu(params) {
  return request(`/api/xadmin/v1/user_menu/${params}`, {
    method: 'DELETE',
  });
}
export async function addUserMenu(params) {
  return request('/api/xadmin/v1/user_menu', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateUserMenu(params, id) {
  return request(`/api/xadmin/v1/user_menu/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
