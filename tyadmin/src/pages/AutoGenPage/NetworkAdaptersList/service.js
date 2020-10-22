import request from 'umi-request';

export async function queryNetworkAdapters(params) {
  return request('/api/xadmin/v1/network_adapters', {
    params,
  });
}
export async function removeNetworkAdapters(params) {
  return request(`/api/xadmin/v1/network_adapters/${params}`, {
    method: 'DELETE',
  });
}
export async function addNetworkAdapters(params) {
  return request('/api/xadmin/v1/network_adapters', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateNetworkAdapters(params, id) {
  return request(`/api/xadmin/v1/network_adapters/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
