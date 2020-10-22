import request from 'umi-request';

export async function queryClusters(params) {
  return request('/api/xadmin/v1/clusters', {
    params,
  });
}
export async function removeClusters(params) {
  return request(`/api/xadmin/v1/clusters/${params}`, {
    method: 'DELETE',
  });
}
export async function addClusters(params) {
  return request('/api/xadmin/v1/clusters', {
    method: 'POST',
    data: { ...params, method: 'post' },
  });
}
export async function updateClusters(params, id) {
  return request(`/api/xadmin/v1/clusters/${id}`, {
    method: 'PUT',
    data: { ...params, id},
  });
}
