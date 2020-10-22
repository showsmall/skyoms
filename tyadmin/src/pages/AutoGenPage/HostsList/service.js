import request from 'umi-request';

export async function queryHosts(params) {
  return request('/api/xadmin/v1/hosts', {
    params,
  });
}
export async function removeHosts(params) {
  return request(`/api/xadmin/v1/hosts/${params}`, {
    method: 'DELETE',
  });
}
export async function addHosts(params) {
  return request('/api/xadmin/v1/hosts', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateHosts(params, id) {
  return request(`/api/xadmin/v1/hosts/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
