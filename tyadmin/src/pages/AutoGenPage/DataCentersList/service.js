import request from 'umi-request';

export async function queryDataCenters(params) {
  return request('/api/xadmin/v1/data_centers', {
    params,
  });
}
export async function removeDataCenters(params) {
  return request(`/api/xadmin/v1/data_centers/${params}`, {
    method: 'DELETE',
  });
}
export async function addDataCenters(params) {
  return request('/api/xadmin/v1/data_centers', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateDataCenters(params, id) {
  return request(`/api/xadmin/v1/data_centers/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
