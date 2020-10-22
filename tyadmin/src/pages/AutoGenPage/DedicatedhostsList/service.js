import request from 'umi-request';

export async function queryDedicatedhosts(params) {
  return request('/api/xadmin/v1/dedicatedhosts', {
    params,
  });
}
export async function removeDedicatedhosts(params) {
  return request(`/api/xadmin/v1/dedicatedhosts/${params}`, {
    method: 'DELETE',
  });
}
export async function addDedicatedhosts(params) {
  return request('/api/xadmin/v1/dedicatedhosts', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateDedicatedhosts(params, id) {
  return request(`/api/xadmin/v1/dedicatedhosts/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
