import request from 'umi-request';

export async function queryDataStores(params) {
  return request('/api/xadmin/v1/data_stores', {
    params,
  });
}
export async function removeDataStores(params) {
  return request(`/api/xadmin/v1/data_stores/${params}`, {
    method: 'DELETE',
  });
}
export async function addDataStores(params) {
  return request('/api/xadmin/v1/data_stores', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateDataStores(params, id) {
  return request(`/api/xadmin/v1/data_stores/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
