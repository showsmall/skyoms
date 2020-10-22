import request from 'umi-request';

export async function queryVirtualHosts(params) {
  return request('/api/xadmin/v1/virtual_hosts', {
    params,
  });
}
export async function removeVirtualHosts(params) {
  return request(`/api/xadmin/v1/virtual_hosts/${params}`, {
    method: 'DELETE',
  });
}
export async function addVirtualHosts(params) {
  return request('/api/xadmin/v1/virtual_hosts', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateVirtualHosts(params, id) {
  return request(`/api/xadmin/v1/virtual_hosts/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
